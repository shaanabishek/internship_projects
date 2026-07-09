import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame

print(df.to_string())

print(df[df["sepal length (cm)"] > 5.0])

print(df[["sepal length (cm)", "petal length (cm)"]])

print(df.isnull().sum())

print(df.describe())

print(df.dtypes)
# or
print(df.info())

df.to_csv("iris_dataset.csv", index=False)