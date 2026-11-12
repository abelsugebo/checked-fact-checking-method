# CHECKED: An Open Fact-Checking Method

The editorial workflow, rating scale, and correction policy behind [HaqCheck](https://haqcheck.org), Ethiopia's first IFCN Verified Signatory fact-checking platform, released as reusable documentation, templates, and a small script.

**Author:** Abel W. Sugebo, founder of Inform Africa and HaqCheck
**Source policy:** [haqcheck.org/our-policy](https://haqcheck.org/our-policy/) (updated 19 December 2024)

## What CHECKED is

A seven-step workflow that takes a claim from monitoring to publication and follow-up:

| | Step | In one line |
|---|---|---|
| **C** | Claim Selection | The desk assesses verifiability, relevance, and possible public impact; claims are taken on unanimously |
| **H** | Hear | The claimant is contacted for context; outreach and observations are documented |
| **E** | Evidence | Primary sources first; secondary sources only with a documented reason; everything cross-checked |
| **C** | Consult | Specialist experts, on the record only |
| **K** | Knowledge | Draft with claim, context, evidence, analysis, and conclusion; reviewed by the Lead Fact-checker |
| **E** | Edit | Editors verify attributions; the Lead Fact-checker rechecks; then publication |
| **D** | Develop | Audience feedback and impact feed back into the process |

Full detail, with roles and the record each step produces: [METHOD.md](METHOD.md).

## What is in this repository

```
METHOD.md                    The workflow as an operational guide
policy/                      The published HaqCheck policy, reproduced unchanged
ratings/ratings.csv          The seven ratings with definitions and ClaimReview labels
templates/
  claim_intake_log.csv       Candidate claims and the desk's decision
  factcheck_record.csv       One row per fact-check, following the CHECKED steps
  corrections_log.csv        Corrections and updates after publication
scripts/to_claimreview.py    Converts fact-check records to schema.org ClaimReview JSON-LD
```

## Ratings

False, True, Misleading, Satire, Altered, Partly False, Scam. Definitions are in [`ratings/ratings.csv`](ratings/ratings.csv). Ratings are proposed by the fact-checker, cross-checked by the research editor, and settled by team discussion and vote when there is disagreement.

## From record to ClaimReview

Platforms and search engines recognise fact-checks through [ClaimReview](https://schema.org/ClaimReview) structured data. The script turns a completed record into that format and rejects ratings that are not on the scale:

```bash
python scripts/to_claimreview.py templates/factcheck_record.csv --publisher "HaqCheck" --publisher-url https://haqcheck.org
```

The template contains one clearly marked synthetic row so the script can be tried immediately.

## Related work

- [disarm-case-coding](https://github.com/abelsugebo/disarm-case-coding): fact-checking handles individual claims; this companion toolkit codes the influence-operation behavior behind them with the DISARM framework.
- [Using the DISARM Framework in Research](https://data-knowledge-hub.com/docs/data-analysis/04_04_disarm-framework/) (Data Knowledge Hub, 2025)

## License

© Inform Africa / HaqCheck. Released under [CC BY 4.0](LICENSE.md). Adapt it for your own newsroom or trust and safety team, with attribution.

## Contact

[abelsugebo.com](https://abelsugebo.com) · [LinkedIn](https://www.linkedin.com/in/abel-wabella-sugebo/)
