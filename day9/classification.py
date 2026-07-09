from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()

model.fit(x_train, y_train)

sample = [
    [5.1, 3.5, 1.4, 0.2],
    [6.5, 3.0, 5.2, 2.0]
]

pred = model.predict(sample)

print(iris.target_names[pred[0]])
print(iris.target_names[pred[1]])