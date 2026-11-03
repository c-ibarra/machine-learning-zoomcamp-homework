# Homework 6 — Learning in Public draft

**Status: Draft.** Review before publishing. First confirm that the completed
notebook, documentation, and reference evidence are accessible at the repository
link. When publishing, use the platform's mention picker to tag Alexey Grigorev
or DataTalksClub, then add the published post URL to the
[delivery record](homework_06_submission.md#delivery-record).

## Post text

I completed the local analysis for Homework 6 of Machine Learning Zoomcamp 2026:
decision trees, random forests, and XGBoost for car fuel-efficiency regression.

A few lessons from the experiments:

- A 10-tree random forest achieved 1.839 MPG validation RMSE, compared with
  2.960 MPG for a predictor that always uses the training mean.
- Depth 10 had the lowest average validation RMSE among the four tested depths.
- A smaller XGBoost learning rate delayed overfitting in this experiment.
  With eta 0.1, validation RMSE was 1.725 MPG after 100 rounds.
- Reproducibility needs more than a seed: 100 and 150 trees tied at three
  decimals in my current environment, while an archived run with the course
  reference versions favored 150. I documented both results.
- Feature importance describes how a model uses its inputs; it does not
  establish causality.

The test set stayed reserved throughout model selection. The notebook includes
the calculations, an answer dashboard, environment versions, and the Q3
reference evidence.

Notebook and documentation:
https://github.com/c-ibarra/machine-learning-zoomcamp-homework

Thanks to Alexey Grigorev and DataTalksClub for the course.

#mlzoomcamp
