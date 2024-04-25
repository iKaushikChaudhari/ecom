import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint

from sklearn.tree import export_graphviz
from IPython.display import Image
import graphviz
import joblib

# Read original dataset
df=pd.read_csv("/content/Train (1).csv")


# selecting features and target data
X_df = df[df.columns[:-1]].values
y_df = df[df.columns[-1]].values

oversampler = RandomOverSampler(random_state=42)

X_resampled_df, y_resampled_df = oversampler.fit_resample(X_df, y_df)

X_train_df, X_temp_df, y_train_df, y_temp_df = train_test_split(X_resampled_df, y_resampled_df, test_size=0.2, random_state=42)
X_val_df, X_test_df, y_val_df, y_test_df = train_test_split(X_temp_df, y_temp_df, test_size=0.5, random_state=42)

rf = RandomForestClassifier(random_state=42)
rf.fit(X_train_df, y_train_df)

y_prediction_rf = rf.predict(X_test_df)
print(classification_report(y_test_df, y_prediction_rf))

# save the model to disk
joblib.dump(rf, "rf_model.sav")
