![Machine Learning Zoomcamp 2026 — c-ibarra. Data exploration, machine learning models, and API deployment.](assets/project-banner.jpg)

# Machine Learning Zoomcamp 2026

**Carlos Ibarra ([c-ibarra](https://github.com/c-ibarra)) · Applied machine learning, model evaluation, and containerized inference**

A portfolio of coursework covering data exploration, regression, classification, and model serving. The repository connects statistical reasoning with executable Python: inspecting missing data, comparing models on reproducible splits, evaluating decision thresholds, and running a lead-conversion API in Docker.

Two datasets anchor the work: car fuel efficiency for regression and course lead conversion for classification. The notebooks include explanations, visualizations, and saved results alongside the calculations.

## Course progress

**As of 27 October 2026: 5 of 9 homeworks have local completion evidence; 4 remain pending in this repository.** Dates and module numbering follow the [2026 cohort syllabus](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/README.md). Deadlines are at **23:00 UTC** (**20:00 in Uruguay**).

“Completed locally” describes the work available here and the deployment checks performed. **Official submission and grading on the course platform have not been confirmed.** This table does not mark local work as officially submitted.

| Homework | Topic | Local status | Evidence / remaining work | Submission deadline |
| --- | --- | --- | --- | --- |
| 01 | Introduction to Machine Learning | Completed locally | [Notebook](homework_01.ipynb): exploration, missing values, and linear algebra. | 21 Sep 2026 |
| 02 | Machine Learning for Regression | Completed locally | [Notebook](homework_02.ipynb): imputation, Ridge regression, and final test RMSE. | 28 Sep 2026 |
| 03 | Machine Learning for Classification | Completed locally | [Notebook](homework_03.ipynb): feature analysis, logistic regression, and regularization. | 5 Oct 2026 |
| 04 | Evaluation Metrics for Classification | Completed locally | [Notebook](homework_04.ipynb): assignment answers, threshold analysis, and cross-validation. | 12 Oct 2026 |
| 05 | Deploying Machine Learning Models | Verified locally | [Deployment files](05-deployment/): direct inference, API requests, Docker build, and container health/inference checks. | 19 Oct 2026 |
| 06 | Decision Trees and Ensemble Learning | Pending | Implement the homework; no solution files found in this repository. | 26 Oct 2026 |
| 08 | Neural Networks and Deep Learning | Pending | Implement the homework; no solution files found in this repository. | 23 Nov 2026 |
| 09 | Serverless Deep Learning | Pending | Implement the homework; no solution files found in this repository. | 30 Nov 2026 |
| 10 | Kubernetes and TensorFlow Serving | Pending | Implement the homework; no solution files found in this repository. | 7 Dec 2026 |

The syllabus moves from Homework 6 to the midterm project and then Homework 8; it does not list a separate Homework 7. The final held-out evaluation mentioned below for Homework 4 is a further-work item, not an unanswered assignment question.

### Projects and peer reviews

No project deliverables or peer-review records were found in this repository. Their local status is therefore pending; work or submissions elsewhere are not verified.

| Project opportunity | Local status | Project deadline | Peer-review deadline |
| --- | --- | --- | --- |
| Midterm | Pending | 9 Nov 2026 | 16 Nov 2026 |
| Capstone 1 | Pending | 4 Jan 2027 | 11 Jan 2027 |
| Capstone 2 | Pending | 18 Jan 2027 | 25 Jan 2027 |

The [cohort requirements](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/README.md#deadlines) call for two passing projects: the midterm and one capstone, or both capstones. Each submitted project also requires reviewing three other students’ projects. An article is listed as an optional activity.

## Start here

| Review goal | Recommended entry point | What to inspect |
| --- | --- | --- |
| Understand modeling decisions | [Model evaluation notebook](homework_04.ipynb) | ROC AUC, precision–recall tradeoffs, threshold selection, and five-fold cross-validation. |
| Inspect ML fundamentals | [Regression notebook](homework_02.ipynb) | NumPy implementations of linear and Ridge regression, imputation comparisons, and held-out evaluation. |
| Review the serving workflow | [Prediction API](05-deployment/predict.py) and [Dockerfile](05-deployment/Dockerfile) | Typed inputs, preprocessing, artifact loading, health checks, and a reproducible container build. |

## Technical work

| Area | Implementation and evidence |
| --- | --- |
| Data preparation | Missing-value audits, categorical exploration, correlations, and comparisons of imputation strategies. |
| Regression | Analytical linear and Ridge regression with NumPy; RMSE comparisons and sensitivity to random splits. |
| Classification | `DictVectorizer`, logistic regression, mutual information, feature elimination, and regularization search. |
| Evaluation | Train/validation/test separation; vectorizers fitted within training partitions and individual CV folds; accuracy, ROC AUC, precision, recall, and F1. |
| Model serving | FastAPI endpoints returning conversion probabilities and decisions, with SHA-256 checksums for the model and preprocessing defaults. |
| Reproducibility | Committed `uv.lock` files, prescribed seeds, bundled cohort datasets, and container base images pinned by digest. |

**Stack:** Python, NumPy, pandas, matplotlib, seaborn, scikit-learn, Jupyter notebooks, uv, FastAPI, Uvicorn, and Docker.

## Selected results

These values are recorded in the notebooks. Each metric is tied to its evaluation scope; the regression and classification tasks use different targets and cannot be compared directly.

| Experiment | Recorded result | Evaluation scope |
| --- | --- | --- |
| Fuel-efficiency regression | **2.236 RMSE** | Homework 2 final test split, after fitting on combined training and validation data. |
| Lead-conversion baseline, `C=1` | **0.732 ROC AUC** | Homework 4 validation split: 1,000 observations. |
| Lead-conversion regularization search, selected `C=0.001` | **0.749 mean ROC AUC**, **0.010 fold standard deviation** | Homework 4 five-fold CV on 4,000 full-training observations; final test evaluation is pending. |

The evaluation notebook also shows why threshold choice matters. For its baseline model, threshold `0.41` gives validation F1 `0.758`, precision `0.619`, and recall `0.976`. These are baseline validation results; the deployed reference API uses its own model and a fixed `0.5` decision threshold.

## Repository map

| Path | Contents |
| --- | --- |
| [homework_01.ipynb](homework_01.ipynb) | Data exploration, imputation effects, and NumPy linear algebra. |
| [homework_02.ipynb](homework_02.ipynb) | Regression, regularization, split stability, and test RMSE. |
| [homework_03.ipynb](homework_03.ipynb) | Classification, feature analysis, and validation accuracy. |
| [homework_04.ipynb](homework_04.ipynb) | Evaluation metrics, threshold curves, cross-validation, and a results dashboard. |
| [data/](data/) | The 2026 car-fuel-efficiency and course-lead-scoring CSV datasets. |
| [05-deployment/](05-deployment/) | Reference model, API, Dockerfile, inference client, and a separate locked environment. |
| [pyproject.toml](pyproject.toml) / [uv.lock](uv.lock) | Notebook dependencies and their resolved versions. |

## Run the containerized API

Prerequisite: Docker with its engine running and port `9696` available. Run from the repository root:

```bash
docker build -t zoomcamp-model:2026-hw5 ./05-deployment
docker run --rm -d --name zoomcamp-hw5 -p 9696:9696 zoomcamp-model:2026-hw5
```

Once the API has started, check its health:

```bash
curl --fail --silent --show-error http://localhost:9696/health
```

The response includes `"status": "ok"`, `model_sha256`, and `feature_defaults_sha256`. Expected artifact checksums are recorded in [model_metadata.json](05-deployment/model_metadata.json).

Send a lead for inference:

```bash
curl --fail --silent --show-error http://localhost:9696/predict \
  -H 'Content-Type: application/json' \
  -d '{
    "lead_source": "organic_search",
    "industry": "technology",
    "employment_status": "employed",
    "location": "europe",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0,
    "interaction_count": 7,
    "lead_score": 0.74
  }'
```

Response verified against the Docker container:

```json
{
  "conversion_probability": 0.769799,
  "conversion": true
}
```

This is an inference example, not a model-performance metric. The probability rounds to `0.770`; `conversion` is `true` when the unrounded probability is at least `0.5`.

Stop the container when finished:

```bash
docker stop zoomcamp-hw5
```

### Serving design and provenance

The request flows through a FastAPI input model, missing-value normalization, and a serialized `DictVectorizer` + `LogisticRegression` pipeline. Missing numerical values use the supplied training medians; missing categories use `NA`.

The Homework 5 serving files and trained artifact were copied from the course reference directory, `cohorts/2026/homework/05-deployment/`. The exercise here covers environment inspection, direct inference, HTTP requests, container construction, and artifact verification. The reference pipeline is separate from the models evaluated in the notebooks; this directory does not include its training script.

The serving environment pins **Python 3.11.15**, **scikit-learn 1.7.2**, **FastAPI 0.119.1**, and **Uvicorn 0.38.0**. The Dockerfile uses Debian 12 Bookworm through `python:3.11.15-slim-bookworm` and pins both the Python and uv images by digest.

For local execution without Docker, see the [deployment instructions](05-deployment/README.md). The provided [q6_test.py](05-deployment/q6_test.py) sends an HTTP request and checks the prediction response structure.

## Run the notebooks

Prerequisites: Python 3.11 or newer, uv, and a notebook-capable editor such as PyCharm or VS Code. From the repository root:

```bash
uv sync --locked
```

Select the root `.venv` interpreter as the notebook kernel. Keep the working directory at the repository root so the relative `data/` paths resolve, then execute cells in order from a fresh kernel. The project includes `ipykernel`; it does not declare a Jupyter server dependency.

The notebooks and the deployment service have **separate `pyproject.toml` and `uv.lock` files**. Use the environment belonging to the directory you are running: the serving artifact expects its pinned scikit-learn version.

## Scope and next steps

This is an educational portfolio and local deployment exercise. The verified Docker health check and inference request demonstrate that the packaged service runs; they do not establish predictive quality or production readiness.

Further work would include a final held-out evaluation of the Homework 4 selected model, threshold evaluation for that model, and service tests covering missing and invalid inputs. Authentication, operational monitoring, and CI are outside the current implementation.
