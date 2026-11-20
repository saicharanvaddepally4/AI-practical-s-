
# Logical Inference using Propositional Logic

# Facts
rain = True
road_wet = False
driving_risky = False

# Rule 1: If rain, then road is wet
if rain:
    road_wet = True

# Rule 2: If road is wet, driving is risky
if road_wet:
    driving_risky = True

# Display results
print("LOGICAL INFERENCE SYSTEM")
print("------------------------")

print("Rain:", rain)
print("Road Wet:", road_wet)
print("Driving Risky:", driving_risky)

# Final conclusion
if rain and road_wet and driving_risky:
    print("\nConclusion: Driving may be risky.")
else:
    print("\nConclusion: No risk detected.")

print("\nInference Completed Successfully!")
