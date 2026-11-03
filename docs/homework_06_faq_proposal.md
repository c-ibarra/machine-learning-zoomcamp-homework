# Homework 6 FAQ contribution proposal

Status: Published as [FAQ proposal issue #545](https://github.com/DataTalksClub/faq/issues/545)
by `c-ibarra` on 3 November 2026 at 02:29:58 UTC. Maintainer review is pending.
The issue is open. The `faq-proposal` label was not applied: GitHub rejected
the label update because this account lacks the repository permission required
to add labels. A maintainer needs to apply it for label-based automation.

## Candidate comparison

| Candidate | Value to students | Existing coverage | Recommendation |
| --- | --- | --- | --- |
| How to calculate mean RMSE per depth in Q4 | Prevents selecting the best individual forest instead of comparing depth-level means. Explains why averaging RMSE differs from averaging predictions or pooling errors. | No matching entry found in the current Module 6 FAQ or the issue/PR searches described below. | Recommended new FAQ proposal. |
| Why seed-1 Random Forest results or rounded rankings differ between environments | Helps students diagnose dataset, matrix-format, version, and rounding differences. | [Issue #528](https://github.com/DataTalksClub/faq/issues/528) already discusses Q3 ranking differences; the FAQ also contains general reproducibility entries. | Add carefully scoped evidence to the existing discussion rather than open a competing Q3 proposal. |
| How to compare final-round and minimum XGBoost validation RMSE | Makes the comparison criterion explicit and prevents mixing final scores with best-round scores. | An [existing entry](https://github.com/DataTalksClub/faq/blob/main/_questions/machine-learning-zoomcamp/module-6/004_7ec4b76943_how-to-get-the-training-and-validation-metrics-fro.md) already covers metric logging with `evals_result`. | Consider extending that entry; ask maintainers to clarify any assignment-specific ambiguity. |

The duplicate check covered the current Module 6 and Module 6 Homework entries,
relevant general reproducibility entries by title, and repository issue/PR
searches for `Homework 6`, `random forest`, `random_state`, `max_depth`,
`mean RMSE`, and rounding. This is a targeted search, not a guarantee against
every possible duplicate. The FAQ bot and maintainers perform their own review.

## Recommended submission route

The [contribution guide](https://github.com/DataTalksClub/faq/blob/main/CONTRIBUTING.md)
directs new entries through the
[FAQ Proposal form](https://github.com/DataTalksClub/faq/issues/new?template=faq-proposal.yml).
The form collects a course, question, answer, and checklist. The automation
reviews proposals for placement and duplication and may generate a PR for
maintainer review. Existing entries can instead be edited through a direct PR.

Use the fields below in the proposal form. Before submission, review the links
and confirm the checklist yourself. After an issue is actually created, copy its
real `https://github.com/DataTalksClub/faq/issues/<number>` URL into the course
form's FAQ contribution field. The new-issue form URL is not a submitted
contribution URL. Acceptance or leaderboard credit is not guaranteed.

## Proposed title

```text
[FAQ] Homework 6 Q4: How do I calculate mean RMSE when selecting max_depth?
```

## Course

```text
machine-learning-zoomcamp
```

## Question

How do I calculate mean RMSE when selecting `max_depth` in Homework 6 Q4? Should
I choose the best individual forest, average predictions, or average the RMSE
scores for each depth?

## Answer

Average the **four validation RMSE scores for each fixed depth**, then select
the depth with the lowest mean. Keep the individual RMSE values at full
precision until after calculating the mean.

In the 2026 assignment, each `max_depth` in `[10, 15, 20, 25]` is evaluated with
`n_estimators` in `[10, 50, 100, 150]`, with `random_state=1`. This produces
16 models, four validation RMSE values per depth, and four depth-level means.
Use the same prepared training and validation data for every model.

For a fixed depth `d`, the comparison score is:

```text
mean_rmse(d) = (rmse(d, 10) + rmse(d, 50) + rmse(d, 100) + rmse(d, 150)) / 4
```

Here is a small, runnable example using **hypothetical scores and a smaller
grid**, not the homework results:

```python
import pandas as pd

scores = pd.DataFrame([
    {"max_depth": 2, "n_estimators": 5, "val_rmse": 2.1},
    {"max_depth": 2, "n_estimators": 15, "val_rmse": 2.3},
    {"max_depth": 3, "n_estimators": 5, "val_rmse": 1.8},
    {"max_depth": 3, "n_estimators": 15, "val_rmse": 2.8},
])

mean_rmse = scores.groupby("max_depth")["val_rmse"].mean()
print(mean_rmse.round(6))  # Round only for display.
```

The illustrative means are 2.2 for depth 2 and 2.3 for depth 3. Although depth 3
contains the best individual model (RMSE 1.8), depth 2 has the lower mean.

Do not replace this calculation with:

- The minimum RMSE for each depth, or the best single depth/size combination.
- The mean of the predictions from several forests; that evaluates a different
  ensemble model.
- The square root of the mean of the four MSE values; the square root is
  nonlinear, so this generally differs from the arithmetic mean of four RMSEs.

If depth-level means tie, report the tie and follow any explicit assignment or
maintainer guidance. The example above intentionally has a unique minimum.

Source: [2026 Homework 6, Question 4](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/06-trees/homework.md#question-4).

## Checklist to review in GitHub

- I have searched existing FAQs and this question is not already answered.
- The answer provides accurate, helpful information.
- I have included a runnable example and the official assignment link.

## Related material considered

- [Current ML Zoomcamp FAQ](https://datatalks.club/faq/machine-learning-zoomcamp.html).
- [Existing Q3 FAQ](https://github.com/DataTalksClub/faq/blob/main/_questions/machine-learning-zoomcamp/module-6-homework/001_66c3aaa71f_homework-q3-what-does-it-mean-that-rmse-stops-impr.md): explains a plateau in RMSE, not Q4's averaging rule.
- [Q3 matrix-format discussion, issue #528](https://github.com/DataTalksClub/faq/issues/528): related to a different question; its proposed answer is not used as an authoritative grading rule here.
- [FAQ contribution instructions](https://datatalks.club/docs/courses/faq/).

## Contribution record

| Item | Status |
| --- | --- |
| Proposal | Published in English |
| Hypothetical example | Executed successfully with the project interpreter; means 2.2 and 2.3 verified |
| Published issue or PR URL | https://github.com/DataTalksClub/faq/issues/545 |
| FAQ automation label | Pending; adding `faq-proposal` requires maintainer permissions |
| Maintainer review | Pending |
| Course form FAQ contribution URL | Pending |
