from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()

model.fit(x_train, y_train)

pred = model.predict(x_test)

acc = accuracy_score(y_test, pred)

print("Accuracy")
print(acc)

print("Confusion Matrix")
print(confusion_matrix(y_test, pred))

print("Classification Report")
print(classification_report(y_test, pred))