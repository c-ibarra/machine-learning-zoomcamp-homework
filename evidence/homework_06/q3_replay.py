"""Replay Q3 with explicitly selected dependencies in an isolated environment."""

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
df_val = df_val.reset_index(drop=True)

y_train = df_train[TARGET].values
y_val = df_val[TARGET].values
df_train = df_train.drop(columns=TARGET)
df_val = df_val.drop(columns=TARGET)

dv = DictVectorizer(sparse=True)
X_train = dv.fit_transform(df_train.to_dict(orient="records"))
X_val = dv.transform(df_val.to_dict(orient="records"))
print(
    f"X_train {X_train.shape} | X_val {X_val.shape} | "
    f"features {list(dv.get_feature_names_out())[:3]}..."
)


def rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_true - y_pred) ** 2))


for n_estimators in [10, 50, 100, 150]:
    forest = RandomForestRegressor(
        n_estimators=n_estimators, random_state=1, n_jobs=-1
    )
    forest.fit(X_train, y_train)
    value = rmse(y_val, forest.predict(X_val))
    print(
        f"n_estimators={n_estimators:>3}  rmse={value:.6f}  "
        f"3dp={round(value, 3):.3f}"
    )
