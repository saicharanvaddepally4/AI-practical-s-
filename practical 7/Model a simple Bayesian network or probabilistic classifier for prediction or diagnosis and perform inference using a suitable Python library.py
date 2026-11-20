
# Naive Bayes Classifier without external libraries

# Training data
data = [
    (20, 30, 'No'),
    (22, 35, 'No'),
    (25, 40, 'No'),
    (27, 45, 'No'),
    (30, 70, 'Yes'),
    (32, 75, 'Yes'),
    (35, 80, 'Yes'),
    (37, 85, 'Yes')
]

# Count classes
yes = sum(1 for x in data if x[2] == 'Yes')
no = sum(1 for x in data if x[2] == 'No')

# Prediction
temperature = 33
humidity = 78

# Calculate class probabilities
p_yes = yes / len(data)
p_no = no / len(data)

# Calculate average values
avg_yes = [sum(x[i] for x in data if x[2] == 'Yes') / yes for i in range(2)]
avg_no = [sum(x[i] for x in data if x[2] == 'No') / no for i in range(2)]

print("NAIVE BAYES CLASSIFIER")
print("----------------------")
print("Temperature:", temperature)
print("Humidity:", humidity)

print("\nProbability of Yes:", p_yes)
print("Probability of No:", p_no)

print("\nAverage Yes:", avg_yes)
print("Average No:", avg_no)

if temperature > avg_yes[0] and humidity > avg_yes[1]:
    print("\nPrediction: YES")
else:
    print("\nPrediction: NO")

print("Inference Completed!")
