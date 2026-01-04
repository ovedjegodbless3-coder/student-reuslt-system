name = input("Enter student name: ")
score = int(input("Enter score: "))

if score >= 70:
    grade = "A"
    status = "Passed"
elif score >= 50:
    grade = "B"
    status = "Passed"
elif score >= 40:
    grade = "C"
    status = "Passed"
else:
    grade = "F"
    status = "Failed"

print("\n--- RESULT ---")
print("Name:", name)
print("Score:", score)
print("Grade:", grade)
print("Status:", status)
