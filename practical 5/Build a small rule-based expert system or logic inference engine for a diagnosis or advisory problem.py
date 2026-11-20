
# Rule-Based Expert System

print("MEDICAL EXPERT SYSTEM")
print("---------------------")

fever = input("Do you have fever? (yes/no): ").lower()
cough = input("Do you have cough? (yes/no): ").lower()
cold = input("Do you have cold? (yes/no): ").lower()
headache = input("Do you have headache? (yes/no): ").lower()

# Rule-based inference
if fever == "yes" and cough == "yes" and cold == "yes":
    print("\nResult: Flu-like symptoms")
    print("Advice: Rest and drink plenty of water.")

elif fever == "yes" and headache == "yes":
    print("\nResult: Fever with headache")
    print("Advice: Monitor temperature and consult a doctor.")

elif cough == "yes" and cold == "yes":
    print("\nResult: Common cold-like symptoms")
    print("Advice: Take rest and drink warm fluids.")

elif headache == "yes":
    print("\nResult: Headache")
    print("Advice: Rest and seek medical advice if needed.")

else:
    print("\nResult: No matching rule found.")
    print("Advice: Consult a healthcare professional if unwell.")

print("\nExpert System Completed!")
