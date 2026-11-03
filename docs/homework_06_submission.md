# Homework 6 submission guide

**Machine Learning Zoomcamp 2026 — Decision Trees and Ensemble Learning**

The local analysis and answer review are complete. All 12 code cells in
[homework_06.ipynb](../homework_06.ipynb) ran in order from a fresh kernel on
2 November 2026 (America/Montevideo), using the project's `.venv`, with no errors.
Official submission and grading have not been confirmed.

## Final answers and evidence

RMSE values are in miles per gallon (MPG). Values below are displayed rounded;
calculations retain full precision unless the assignment requires rounding.

| Question | Selected option | Computed evidence | Reason |
| --- | --- | --- | --- |
| Q1: Decision tree split | `model_year` | Root split: `model_year <= 1997.5`; leaf means: `28.614` MPG (2,716 rows) and `31.168` MPG (3,284 rows). | This is the original column used by the depth-1 tree. |
| Q2: Random forest baseline | `1.837` | Validation RMSE: `1.839383` (`1.8394` at four decimals); constant-mean baseline: `2.9600`. | `1.837` is the closest numerical option under the online submission rule. |
| Q3: Number of trees | `150` | Current environment: 100 and 150 trees both round to `1.768`. Archived reference run: 100 gives `1.769`, 150 gives `1.768`. | `150` is the unique minimum at three decimals in the archived reference environment. |
| Q4: Tree depth | `10` | Mean validation RMSE by depth: 10 → `1.754133`; 15 → `1.783670`; 20 → `1.787846`; 25 → `1.786675`. | Depth 10 has the lowest mean over the four forest sizes. |
| Q5: Feature importance | `vehicle_weight` | Candidate importances: weight `0.203067`, horsepower `0.078468`, displacement `0.061152`, acceleration `0.055342`. | Weight ranks first among the four candidates; `model_year` ranks first overall. |
| Q6: XGBoost learning rate | `0.1` | Round-100 validation RMSE: `1.724810` at eta 0.1 vs `1.826458` at eta 0.3. Minimum RMSE: `1.712171` at round 40 vs `1.732048` at round 11. | Both the final-round and minimum-RMSE comparisons favor eta 0.1. |

### Q3: environment-sensitive ranking

The current environment's unrounded RMSE is lower with 100 trees (`1.767643`)
than with 150 (`1.768109`), but both round to `1.768`. The assignment asks for a
three-decimal comparison and supplies no rule for tied model scores.

The [archived reference-environment evidence](../evidence/homework_06/reference_replay.md)
preserves output recovered from an earlier successful diagnostic execution,
including versions and a reproduction script. In that environment, 150 trees
is the unique minimum at three decimals. This evidence supports the selected
option; it does not confirm how the platform grades the question.

The reference run was not repeated during the final notebook verification.
Choosing the larger forest is not used as a tie-break.

### Assignment sources and numerical options

The [official online assignment](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/06-trees/homework.md)
is the source for submission rules. Its submission note permits the nearest
numerical option and chooses the higher option only when the computed value
is exactly halfway between two numerical options. This rule supports Q2 and
does not resolve Q3's tie between model scores.

The local course copy requires an exact numerical match and omits the online
Learning in Public section. These differences are recorded explicitly rather
than combined into a new rule.

## Reproduce the notebook

From the repository root, install the existing locked environment:

```bash
uv sync --locked
```

Open [homework_06.ipynb](../homework_06.ipynb) in a notebook-capable editor,
select the root `.venv` interpreter, set the working directory to the repository
root, restart the kernel, and execute all cells in order. The project declares
`ipykernel`; a standalone Jupyter server or notebook execution CLI is not assumed.

### Dataset and preparation

- Use only `data/car_fuel_efficiency_2026.csv`; the notebook checks its SHA-256
  before loading it:
  `00a5cab178a8b7cd6e9157ee71dabc236ba7f20b1832336d358b07af14ba431f`.
- Shape: 10,000 rows and 11 columns. Predict `fuel_efficiency_mpg` using the
  remaining 10 columns. The target has no missing values.
- Fill the 877 missing horsepower values and 264 missing acceleration values
  with zero, as prescribed. Keep the source CSV unchanged.
- Use the exact split calls below. They produce 6,000 training, 2,000 validation,
  and 2,000 test rows.

```python
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(
    df_full_train, test_size=0.25, random_state=1
)
```

Fit `DictVectorizer(sparse=True)` on training records only. It creates 16
features: seven numerical columns and nine one-hot columns. Transform validation
and test with the same vectorizer. Test was not evaluated or used for selection.

### Model settings

| Question | Settings |
| --- | --- |
| Q1 | `DecisionTreeRegressor(max_depth=1)` |
| Q2 | `RandomForestRegressor(n_estimators=10, random_state=1, n_jobs=-1)` |
| Q3 | Forest sizes `[10, 50, 100, 150]`; `random_state=1`, `n_jobs=-1`, other settings fixed. |
| Q4 | Depths `[10, 15, 20, 25]` × forest sizes `[10, 50, 100, 150]`; `random_state=1`, `n_jobs=-1`. Average four full-precision validation RMSE values per depth. |
| Q5 | `RandomForestRegressor(n_estimators=10, max_depth=20, random_state=1, n_jobs=-1)`; pair `feature_importances_` with vectorizer names. |
| Q6 | Two separate 100-round `xgb.train` runs; eta 0.3 and 0.1; depth 6; `min_child_weight=1`; `objective="reg:squarederror"`; `nthread=8`; `seed=1`; `verbosity=1`. Log train/validation RMSE; no early stopping or other tuning. |

### Verified environment and limits

| Component | Final notebook verification | Archived Q3 reference run |
| --- | --- | --- |
| Python | 3.14.6, free-threaded CPython on macOS ARM64 | 3.11.15 |
| NumPy | 2.4.6 | 2.3.3 |
| pandas | 3.0.6 | 2.3.2 |
| scikit-learn | 1.9.1 | 1.7.2 |
| XGBoost | 3.4.1 | Not used for Q3 |

The release documentation lists XGBoost 3.2.0 as reference context; Q6 was not
replayed with that version. The lockfile resolves dependencies for supported
Python versions, so using a different interpreter may select different versions
and change results. The setup command alone does not guarantee the same
numerical results on every interpreter or platform. The notebook prints its
actual interpreter and library versions.

The completed verification confirmed valid notebook JSON and structure, all
31 cell IDs and their order preserved, execution counts 1–12, zero error outputs,
and no changes to the source dataset. Execution timestamps were refreshed.
The Q3 diagnostic script was preserved for reproduction, not rerun in the final
verification. This documentation update did not rerun model training.

## Prepare the repository for delivery

Review the existing changes and the new files in the editor:

```bash
git status --short
git diff -- README.md pyproject.toml uv.lock
```

After reviewing, stage the delivery files explicitly:

```bash
git add README.md pyproject.toml uv.lock homework_06.ipynb \
  docs/homework_06_submission.md docs/homework_06_learning_in_public.md \
  evidence/homework_06/reference_replay.md evidence/homework_06/q3_replay.py
git diff --cached --check
git diff --cached --stat
```

Inspect the staged content, including the notebook's saved outputs, before
committing. Keep environments, caches, checkpoints, IDE files, local prompts,
and unrelated work out of the delivery commit. Suggested commit command:

```bash
git commit -m "Add completed Homework 6 ensemble learning analysis"
```

Push the reviewed commit to the intended remote branch. Then open the published
notebook and documentation on GitHub and copy the commit permalink into the
submission record below. The configured repository is
[c-ibarra/machine-learning-zoomcamp-homework](https://github.com/c-ibarra/machine-learning-zoomcamp-homework).

## Submit and record confirmation

1. Open the [Homework 6 submission page](https://courses.datatalks.club/ml-zoomcamp-2026/homework/hw06)
   while signed in. Confirm that it accepts a submission. The page could not be
   inspected with the browsing tool, so its current fields and availability are
   unverified.
2. Transfer the six selected options from the answer table. Add the repository
   or notebook link wherever the form requests it.
3. Review and publish the [Learning in Public draft](homework_06_learning_in_public.md).
   The online assignment asks for a short post, chart, or notebook excerpt with
   `#mlzoomcamp`, a tag for Alexey Grigorev or DataTalksClub, and the post link
   included with the homework. Confirm the mention with the platform's picker.
4. Review the filled form, submit it, and save its confirmation or receipt.
5. Record the published links, actual submission time, and later grading result.
   Update local status only after the corresponding evidence exists.

## Delivery record

| Item | Status / value |
| --- | --- |
| Local analysis | Complete |
| Fresh-kernel verification | Passed, 2 November 2026 (America/Montevideo) |
| Answer review | Complete; Q3 uses documented archived reference evidence |
| Repository commit permalink | Pending |
| Published notebook URL | Pending |
| Learning in Public post URL | Pending |
| Course submission timestamp and timezone | Pending |
| Submission receipt or confirmation | Pending |
| Grading result | Pending |

The submission record tracks external delivery separately from completed local
analysis. No submission, publication, or grading is asserted by this document.
