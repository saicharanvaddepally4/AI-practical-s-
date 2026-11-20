
import math

# Training dataset
data = [
    ([1, 1], "A"),
    ([2, 2], "A"),
    ([3, 2], "A"),
    ([6, 6], "B"),
    ([7, 7], "B"),
    ([8, 7], "B")
]

# KNN prediction function
def knn_predict(test, k=3):
    distances = []

    for point, label in data:
        d = math.sqrt(
            (test[0] - point[0]) ** 2 +
            (test[1] - point[1]) ** 2
        )
        distances.append((d, label))

    distances.sort()

    nearest = distances[:k]
    count_a = sum(1 for d, label in nearest if label == "A")
    count_b = sum(1 for d, label in nearest if label == "B")

    return "A" if count_a >= count_b else "B"

# Test dataset
tests = [
    ([2, 1], "A"),
    ([7, 6], "B"),
    ([3, 3], "A"),
    ([6, 7], "B")
]

correct = 0

print("KNN Classification Results")
print("--------------------------")

for point, actual in tests:
    predicted = knn_predict(point)
    print("Input:", point)
    print("Actual:", actual)
    print("Predicted:", predicted)
    print()

    if predicted == actual:
        correct += 1

accuracy = (correct / len(tests)) * 100

print("Correct Predictions:", correct)
print("Accuracy:", accuracy, "%")
