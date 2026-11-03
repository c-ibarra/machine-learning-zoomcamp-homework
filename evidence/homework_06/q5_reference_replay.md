# Homework 6 Q5 reference-environment evidence

See the [submission guide](../../docs/homework_06_submission.md) for the full
answer table and delivery record.

The output below was produced by running the companion
[q5_replay.py](q5_replay.py) in an isolated environment with the course
reference versions. The script uses the same data preparation, split calls,
sparse vectorizer, and forest parameters as the notebook's Q5 cell. It does not
use the test set. The same script run in the project's environment reproduces
the values stored in the notebook.

Dataset: `data/car_fuel_efficiency_2026.csv`

SHA-256: `00a5cab178a8b7cd6e9157ee71dabc236ba7f20b1832336d358b07af14ba431f`

## Captured output (reference environment)

```text
python 3.11.15 | numpy 2.3.3 | pandas 2.3.2 | sklearn 1.7.2

All features (descending):
model_year                      0.295702
vehicle_weight                  0.203202
fuel_type=Gasoline              0.160713
horsepower                      0.078251
engine_displacement             0.061106
acceleration                    0.055486
origin=USA                      0.042223
drivetrain=Front-wheel drive    0.020106
num_doors                       0.019425
fuel_type=Hybrid                0.018041
fuel_type=Diesel                0.014809
drivetrain=All-wheel drive      0.007844
num_cylinders                   0.007509
origin=Asia                     0.006173
drivetrain=Rear-wheel drive     0.005693
origin=Europe                   0.003717

Candidates:
vehicle_weight         0.203202
horsepower             0.078251
engine_displacement    0.061106
acceleration           0.055486

Most important candidate: vehicle_weight
```

## Comparison with the notebook's environment

| Candidate | Notebook (Python 3.14.6, scikit-learn 1.9.1) | Reference (Python 3.11.15, scikit-learn 1.7.2) |
| --- | ---: | ---: |
| `vehicle_weight` | 0.203067 | 0.203202 |
| `horsepower` | 0.078468 | 0.078251 |
| `engine_displacement` | 0.061152 | 0.061106 |
| `acceleration` | 0.055342 | 0.055486 |

`vehicle_weight` is the most important of the four candidates in both
environments, the ranking of the candidates is identical, and each candidate
value differs by less than 0.0003. The six most important features also keep
the same order. The one-hot columns `fuel_type=Diesel` and `fuel_type=Hybrid`
swap places in the ranking (about 0.018 and 0.015); they are outside the four
candidates and do not affect the answer.

These importances come from a single forest of 10 trees, so small differences
between library versions are expected. This evidence does not establish how the
course platform grades the question.

## Reproduction

From the repository root, an isolated replay can be requested with the
following command. It may download Python and dependencies; it does not replace
the project's locked environment.

```bash
uv run --no-project --python 3.11.15 \
  --with numpy==2.3.3 --with pandas==2.3.2 --with scikit-learn==1.7.2 \
  python -I evidence/homework_06/q5_replay.py data/car_fuel_efficiency_2026.csv
```

Full-precision values are retained during computation; the captured output
displays six decimal places. XGBoost is not part of this Q5 replay.
