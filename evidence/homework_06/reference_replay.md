# Homework 6 reference-environment evidence

See the [submission guide](../../docs/homework_06_submission.md) for the full
answer table, current-environment verification, and delivery record.

The following Q3 output was recovered from the successful execution record of
the earlier diagnostic run on 2 November 2026. It is archived evidence, not a
new execution in the notebook's current environment. The diagnostic used the
same data preparation, split calls, sparse vectorizer, and forest parameters
as the notebook. It did not use the test set for evaluation.

Dataset: `data/car_fuel_efficiency_2026.csv`

SHA-256: `00a5cab178a8b7cd6e9157ee71dabc236ba7f20b1832336d358b07af14ba431f`

## Captured diagnostic output

```text
python 3.11.15 | numpy 2.3.3 | pandas 2.3.2 | sklearn 1.7.2
X_train (6000, 16) | X_val (2000, 16) | features ['acceleration', 'drivetrain=All-wheel drive', 'drivetrain=Front-wheel drive']...
n_estimators= 10  rmse=1.843032  3dp=1.843
n_estimators= 50  rmse=1.773650  3dp=1.774
n_estimators=100  rmse=1.768922  3dp=1.769
n_estimators=150  rmse=1.768196  3dp=1.768
```

The unique minimum at three decimals is 150 trees in this reference environment.
The notebook's current environment instead ties 100 and 150 at three decimals;
100 has the lower unrounded RMSE there. The selected option `150` is supported
by the archived reference run, not by an invented tie-breaking rule. This does
not establish the course platform's grading behavior.

## Reproduction

The companion [q3_replay.py](q3_replay.py) retains the diagnostic calculations
and adds a dataset checksum assertion. From the repository root, an isolated
replay can be requested with the following command. It may download Python
and dependencies; it does not replace the project's locked environment.

```bash
uv run --no-project --python 3.11.15 \
  --with numpy==2.3.3 --with pandas==2.3.2 --with scikit-learn==1.7.2 \
  python -I evidence/homework_06/q3_replay.py data/car_fuel_efficiency_2026.csv
```

Full-precision values are retained during computation; the captured output
displays six decimal places and the assignment's three-decimal comparison.
XGBoost is not part of this Q3 replay.
