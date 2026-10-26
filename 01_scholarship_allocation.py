
# University Scholarship Allocation

name = input("Enter student name: ")
marks = float(input("Enter aggregate marks (%): "))
attendance = float(input("Enter attendance (%): "))
income = float(input("Enter family annual income: "))

print("\n--- Scholarship Result ---")
print("Student Name:", name)

if marks >= 85 and attendance >= 75 and income <= 200000:
    print("Status: Eligible for Scholarship")
else:
    print("Status: Not Eligible for Scholarship")
