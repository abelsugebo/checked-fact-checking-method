"""Turn rows of factcheck_record.csv into schema.org ClaimReview JSON-LD.

ClaimReview is the structured-data format search engines and platforms read
to recognise published fact-checks. This script also checks each rating
against ratings/ratings.csv.

Usage:
    python scripts/to_claimreview.py templates/factcheck_record.csv --publisher "HaqCheck" --publisher-url https://haqcheck.org

Prints one JSON-LD block per row. Uses only the Python standard library.
"""

import argparse
import csv
import json
import sys
from pathlib import Path

RATINGS_FILE = Path(__file__).resolve().parent.parent / "ratings" / "ratings.csv"


def load_ratings():
    with open(RATINGS_FILE, newline="", encoding="utf-8") as f:
        return {row["rating"]: row["claimreview_alternateName"] for row in csv.DictReader(f)}


def to_claimreview(row, ratings, publisher, publisher_url):
    claim = {
        "@type": "Claim",
        "author": {"@type": "Organization", "name": row["claimant"]},
    }
    if row.get("claim_date"):
        claim["datePublished"] = row["claim_date"]
    if row.get("claim_appearance_url"):
        claim["appearance"] = {"@type": "CreativeWork", "url": row["claim_appearance_url"]}

    return {
        "@context": "https://schema.org",
        "@type": "ClaimReview",
        "url": row["published_url"],
        "claimReviewed": row["claim_text"],
        "datePublished": row["date_published"],
        "inLanguage": row.get("language", ""),
        "author": {"@type": "Organization", "name": publisher, "url": publisher_url},
        "itemReviewed": claim,
        "reviewRating": {"@type": "Rating", "alternateName": ratings[row["rating"]]},
    }


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("records")
    p.add_argument("--publisher", required=True)
    p.add_argument("--publisher-url", required=True)
    args = p.parse_args()

    ratings = load_ratings()
    errors = 0
    with open(args.records, newline="", encoding="utf-8") as f:
        for n, row in enumerate(csv.DictReader(f), start=2):
            missing = [k for k in ("claim_text", "claimant", "rating", "published_url", "date_published") if not row.get(k)]
            if missing:
                print(f"line {n}: missing {', '.join(missing)}", file=sys.stderr)
                errors += 1
                continue
            if row["rating"] not in ratings:
                print(f"line {n}: rating '{row['rating']}' is not one of: {', '.join(ratings)}", file=sys.stderr)
                errors += 1
                continue
            print(json.dumps(to_claimreview(row, ratings, args.publisher, args.publisher_url), indent=2, ensure_ascii=False))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
