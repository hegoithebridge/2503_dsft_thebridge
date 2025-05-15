
import pandas as pd
import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def load_and_split_data():
    iris_data = load_iris()
    features = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
    target = pd.Series(iris_data.target)
    x_train, _, y_train, _ = train_test_split(
        features, target, test_size=0.2, stratify=target
    )
    return x_train, y_train

def train_and_save_model(x_train, y_train, output_path="iris_model.pkl"):
    model = RandomForestClassifier()
    model.fit(x_train, y_train)
    with open(output_path, "wb") as f:
        pickle.dump(model, f)
    print(f"Modelo guardado en {output_path}")

if __name__ == "__main__":
    x_train, y_train = load_and_split_data()
    train_and_save_model(x_train, y_train)