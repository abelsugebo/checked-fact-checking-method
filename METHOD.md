# The CHECKED workflow, step by step

This is an operational reading of the [published HaqCheck policy](policy/haqcheck-policy-2024-12-19.md). For each step it names who acts, what is decided, and which record the step leaves behind. Roles and rules come from the policy; the record columns refer to the templates in [`templates/`](templates/).

| Step | Who acts | What happens | Record it produces |
|---|---|---|---|
| **C** Claim Selection | Fact-checking Desk | Monitor diverse media and user submissions; assess each candidate claim for verifiability, relevance, and possible public impact. A claim is taken on only by unanimous decision. | `claim_intake_log.csv`: one row per candidate, with the decision and reason |
| **H** Hear | Fact-checker | Contact the person or organization that made the claim for context, evidence, or clarification. If there is no response, record observations on the claim's likely intent from the text and other available information. | `factcheck_record.csv`: `claimant_contacted`, `claimant_response`, `intent_observations` |
| **E** Evidence | Fact-checker | Collect evidence, prioritizing primary sources (official documents, data, direct statements). Use credible secondary sources only when primary sources are unavailable, and document why. Cross-check everything. | `factcheck_record.csv`: `primary_sources`, `secondary_sources`, `secondary_source_reason` |
| **C** Consult | Fact-checker | Discuss evidence with specialist experts, especially on technical topics. Quote only experts willing to go on the record; no anonymous sources. | `factcheck_record.csv`: `experts_consulted` |
| **K** Knowledge | Fact-checker, then Lead Fact-checker | Draft the report: claim, context, evidence, analysis, conclusion. The Lead Fact-checker reviews it for accuracy, clarity, and impartiality. | `factcheck_record.csv`: `draft_reviewed_by` |
| **E** Edit | Editors, Lead Fact-checker, social media curator | Editors refine language, verify source attributions, and check editorial standards. The Lead Fact-checker rechecks accuracy before publication. The social media curator publishes on the website and social platforms. | `factcheck_record.csv`: `rating`, `rating_cross_checked_by`, `published_url`, `date_published` |
| **D** Develop | Team | Monitor audience feedback through comments, messages, and other channels; assess impact; refine the process. Corrections and updates are logged. | `corrections_log.csv` |

## Rating decisions

Fact-checkers propose a rating once they have the best publicly available evidence. The research editor cross-checks it. If they disagree, the team discusses it and votes. The seven ratings and their definitions are in [`ratings/ratings.csv`](ratings/ratings.csv).

## Sources and safety

All important sources are listed and linked where possible so readers can verify the work. If naming a source would put that person at risk, give as much detail as possible without compromising their safety.

## Corrections versus updates

| Type | When | How it is shown |
|---|---|---|
| Correction | A factual mistake was published | Fixed promptly; the note explains what was wrong and how it was addressed |
| Update | New information changes the context or improves clarity | Labeled distinctly; explains the new information and how it affects understanding |

All changes are noted directly in the content. Substantial updates or ethical concerns get an editor's note.

## Nonpartisanship

Staff stay independent of political affiliations or movements and avoid advocacy or policy opinions that could affect perceived impartiality. Relevant interests of sources and commercial relationships that could affect evidence are disclosed. Staff receive regular training, and compliance is checked through systematic audits.

## What this method does not specify

The published policy names the selection criteria (verifiability, relevance, possible public impact) but does not define a numeric scoring scheme. The intake template records the assessment in plain text rather than inventing weights. Teams adopting the method can add their own scoring and should document it.
