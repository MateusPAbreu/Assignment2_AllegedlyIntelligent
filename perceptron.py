import random
from typing import List, Tuple, Dict


# Read  mushroom training data

def read_train_file(path: str) -> List[List[str]]:
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(line.split(","))
    return data


# Read the unknown mushroom data
# These rows contain only attributes
def read_unknown_file(path: str) -> List[List[str]]:
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(line.split(","))
    return data


# Convert mushroom class labels into numbers for perceptron training
# edible = 1, poisonous = -1
def label_to_int(label: str) -> int:
    return 1 if label == "e" else -1


# positive becomes edible, negative becomes poisonous
def int_to_label(value: int) -> str:
    return "e" if value >= 0 else "p"


# Turn categorical mushroom attributes into binary features for the perceptron work with the dataset
class onehotencoding:
    def __init__(self):
        self.feature_map: Dict[Tuple[int, str], int] = {}
        self.num_features = 0

    def fit(self, rows: List[List[str]]) -> None:
        index = 0
        for row in rows:
            for col_i, value in enumerate(row):
                key = (col_i, value)
                if key not in self.feature_map:
                    self.feature_map[key] = index
                    index += 1
        self.num_features = index

    def transform_one(self, row: List[str]) -> List[int]:
        vector = [0] * self.num_features
        for col_i, value in enumerate(row):
            key = (col_i, value)
            if key in self.feature_map:
                vector[self.feature_map[key]] = 1
        return vector

    def transform(self, rows: List[List[str]]) -> List[List[int]]:
        return [self.transform_one(row) for row in rows]



# Perceptron classifier
# learns weights that separate edible and poisonous mushrooms
class Perceptron:
    def __init__(self, learning_rate: float = 0.1, epochs: int = 20):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights: List[float] = []
        self.bias: float = 0.0

    def predict_raw(self, x: List[int]) -> float:
        total = self.bias
        for w, xi in zip(self.weights, x):
            total += w * xi
        return total

    def predict(self, x: List[int]) -> int:
        return 1 if self.predict_raw(x) >= 0 else -1

    def fit(self, X: List[List[int]], y: List[int]) -> None:
        if not X:
            return

        self.weights = [0.0] * len(X[0])
        self.bias = 0.0

        for epoch in range(self.epochs):
            combined = list(zip(X, y))
            random.shuffle(combined)

            mistakes = 0
            for x_i, y_i in combined:
                prediction = self.predict(x_i)
                if prediction != y_i:
                    update = self.learning_rate * y_i
                    for j in range(len(self.weights)):
                        self.weights[j] += update * x_i[j]
                    self.bias += update
                    mistakes += 1

            print(f"Epoch {epoch + 1}/{self.epochs} - Mistakes: {mistakes}")

            # Stop training early if the model classifies every training example correctly
            if mistakes == 0:
                print("Training done early.")
                break


# Measure how many test mushrooms were classified correctly
def accuracy_score(y_true: List[int], y_pred: List[int]) -> float:
    correct = 0
    for actual, predicted in zip(y_true, y_pred):
        if actual == predicted:
            correct += 1
    return correct / len(y_true) if y_true else 0.0



# confusion matrix for the test results
# tp = edible predicted as edible
# tn = poisonous predicted as poisonous
# fp = poisonous predicted as edible
# fn = edible predicted as poisonous

def confusion_matrix(y_true: List[int], y_pred: List[int]) -> Tuple[int, int, int, int]:
    tp = tn = fp = fn = 0

    for actual, predicted in zip(y_true, y_pred):
        if actual == 1 and predicted == 1:
            tp += 1
        elif actual == -1 and predicted == -1:
            tn += 1
        elif actual == -1 and predicted == 1:
            fp += 1
        elif actual == 1 and predicted == -1:
            fn += 1

    return tp, tn, fp, fn


def print_confusion_matrix(tp: int, tn: int, fp: int, fn: int) -> None:
    print("\nConfusion Matrix")
    print("                     Predicted")
    print("                 Edible    Poisonous")
    print(f"Actual Edible     {tp:<9} {fn:<9}")
    print(f"Actual Poisonous  {fp:<9} {tn:<9}")


#  split the labeled dataset into training data and test data

def train_test_split(data: List[List[str]], test_ratio: float = 0.2):
    shuffled = data[:]
    random.shuffle(shuffled)
    split_index = int(len(shuffled) * (1 - test_ratio))
    return shuffled[:split_index], shuffled[split_index:]


def main():
    random.seed(42)

    training_file = "MushroomData_8000.txt"
    unknown_file = "MushroomData_Unknwon_100.txt"

    learning_rate = 0.1
    epochs = 20
    test_ratio = 0.2

    training_rows = read_train_file(training_file)
    unknown_rows = read_unknown_file(unknown_file)

    train_rows, test_rows = train_test_split(training_rows, test_ratio=test_ratio)

    # Split the labeled training rows into class labels and mushroom attributes
    y_train = [label_to_int(row[0]) for row in train_rows]
    X_train_raw = [row[1:] for row in train_rows]

    y_test = [label_to_int(row[0]) for row in test_rows]
    X_test_raw = [row[1:] for row in test_rows]

    X_unknown_raw = unknown_rows

    # Learn the encoding from the training data, then apply it to datasets
    encoder = onehotencoding()
    encoder.fit(X_train_raw)

    X_train = encoder.transform(X_train_raw)
    X_test = encoder.transform(X_test_raw)
    X_unknown = encoder.transform(X_unknown_raw)

    # Train the perceptron using the encoded mushroom training data
    model = Perceptron(learning_rate=learning_rate, epochs=epochs)
    model.fit(X_train, y_train)

    # Test the perceptron on the heldout test set
    test_predictions = [model.predict(x) for x in X_test]
    acc = accuracy_score(y_test, test_predictions)
    tp, tn, fp, fn = confusion_matrix(y_test, test_predictions)

    print("\nPerceptron Results")
    print(f"Training samples: {len(X_train)}")
    print(f"Test samples: {len(X_test)}")
    print(f"Number of encoded features: {encoder.num_features}")
    print(f"Learning rate: {learning_rate}")
    print(f"Epochs: {epochs}")
    print(f"Perceptron test accuracy: {acc * 100:.2f}%")

    print_confusion_matrix(tp, tn, fp, fn)

    # Predict the class of the 100 unknown mushrooms
    unknown_predictions = [int_to_label(model.predict(x)) for x in X_unknown]

    # Save the predictions 
    with open("predictionResultPER.txt", "w", encoding="utf-8") as f:
        for pred in unknown_predictions:
            f.write(pred + "\n")

    print("\npredictionResultPER.txt is created.")


if __name__ == "__main__":
    main()