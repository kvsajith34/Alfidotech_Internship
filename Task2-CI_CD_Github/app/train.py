import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_model():
    # Load dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Train
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    acc = accuracy_score(y_test, model.predict(X_test))
    print(f"Model Accuracy: {acc:.4f}")

    # Save
    with open("app/model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model saved to app/model.pkl")
    return acc

if __name__ == "__main__":
    train_model()
