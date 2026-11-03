"""Replay Q5 with explicitly selected dependencies in an isolated environment."""

import hashlib
from pathlib import Path
import sys

import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split

data_path = Path(sys.argv[1])
expected_sha256 = "00a5cab178a8b7cd6e9157ee71dabc236ba7f20b1832336d358b07af14ba431f"
assert hashlib.sha256(data_path.read_bytes()).hexdigest() == expected_sha256
TARGET = "fuel_efficiency_mpg"

print(
    f"python {sys.version.split()[0]} | numpy {np.__version__} | "
    f"pandas {pd.__version__} | sklearn {sklearn.__version__}"
)

df = pd.read_csv(data_path)
feature_columns = df.columns.drop(TARGET)
df[feature_columns] = df[feature_columns].fillna(0)

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)
df_train = df_train.reset_index(drop=True)

y_train = df_train[TARGET].values
df_train = df_train.drop(columns=TARGET)

dv = DictVectorizer(sparse=True)
X_train = dv.fit_transform(df_train.to_dict(orient="records"))
feature_names = dv.get_feature_names_out()

forest = RandomForestRegressor(
    n_estimators=10, max_depth=20, random_state=1, n_jobs=-1
)
forest.fit(X_train, y_train)

importances = pd.Series(forest.feature_importances_, index=feature_names)
importances = importances.sort_values(ascending=False)
print("\nAll features (descending):")
print(importances.round(6).to_string())

candidates = ["vehicle_weight", "horsepower", "acceleration", "engine_displacement"]
candidate_importances = importances[candidates].sort_values(ascending=False)
print("\nCandidates:")
print(candidate_importances.round(6).to_string())
print(f"\nMost important candidate: {candidate_importances.index[0]}")
