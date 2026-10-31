---
name: plant-peer-review
description: "Evidence-anchored independent-style peer review, scientific critique, revision planning, and re-review of plant-science original research and review articles. Trigger for 审稿, 模拟审稿, reviewer, 投稿前评审, 复审, or rebuttal planning."
---

# Plant Peer Review | 植物科学论文审稿

## Scope and routing
- Accept an entire manuscript, review article, abstract, figure/legend, Methods or Results section, reviewer comments, or revised version. Review only supplied scope and mark missing evidence **NOT_ASSESSABLE**.
- Standalone peer-review requests come directly here. Full-manuscript writing workflows in `plant-research-article` and `plant-review-article` call this skill after the polished draft and citation/data audits. Do not duplicate reviewer engines inside either writing skill.
- Review reports follow the user's requested language; when generating a full bilingual manuscript package, provide appropriately aligned English and professional-academic-Chinese reviewer reports when requested by the package.
- Read `references/review-protocol.md`, `references/issue-ledger.md`, and the applicable `references/plant-specific-checks.md`. Invoke `reading-literature` for external claim or citation checks when evidence is accessible.

## Reviewer contract
1. Freeze the exact submitted manuscript version and assessment boundary. Distinguish author-supplied facts, independently checked sources, and unverified assertions.
2. Check scientific significance and positioning, novelty against identifiable prior work, plant biology, evidence hierarchy, method and statistical validity, figure/source-data consistency, interpretation and limitations, clarity, ethics/reporting.
3. If genuinely separate contexts are available, generate three blinded-to-one-another viewpoint reports from the same immutable evidence packet: (1) plant biology/mechanisms, (2) methods/statistics and data integrity, (3) novelty/argumentation/reader significance. Freeze before aggregation. If isolated contexts are **not** available, describe them as distinct review perspectives from one AI, never as independent or mutually blinded reviewers.
4. Every material issue has a stable ID, severity, manuscript claim/location, evidence anchor or "not provided", precise concern, scientific consequence, actionable resolution criterion, and status. Do not invent page/line numbers or methods.
5. Separate confirmed inconsistency from a plausible risk and from missing input. Assess numeric, figure, language and source consistency independently of the review perspectives. Do not call suspected image reuse proof without source examination.
6. Return an editorial synthesis with ordered **blocking / major / minor** issues, genuine disagreements, and a prioritized revision plan; do not fabricate reviewer consensus, quotas, or an accept/reject decision.
7. If asked to revise, preserve manuscript meaning and link each issue to an exact change. If asked for a response letter, draft replies against **real reviewer comments** or clearly labeled simulated comments; never imply external reviewers have spoken.
8. Re-review the specified revised version by comparing reported changes against actual revised content. Unfixed critical defects remain OPEN.

## Scientific boundaries
- Never fabricate observations, p-values, controls, references, novelty claims, methods, identities, reviewer credentials, acceptance outcomes, or institutional approvals.
- Material unsupported causal/functional claims, pseudoreplication, missing indispensable controls and contradictions can be BLOCK, but a missing PDF alone may mean NOT_ASSESSABLE rather than proof of error.
- "More experiments" is not the default answer: first examine whether a narrower accurate claim, reanalysis, better reporting or an essential discriminating test resolves the concern.
- Journal-specific fit or requirements are verified from the journal's current official source. Without these, mark journal fit provisional.
- Explain the remaining limitations and hand back to the originating manuscript skill for author-approved changes.