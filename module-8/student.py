# Amit Rizal
# Assignment Module-B: JSON Student List Update
# Purpose: Load, modify, and update a JSON file of student records.

import json

# Function to print student list
def print_student_list(student_list, message):
    print(f"\n{message}")
    for student in student_list:
        print(f"{student['F_Name']}, {student['L_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")

# Load JSON data into a class list
json_file = "student.json"

try:
    with open(json_file, "r") as file:
        students = json.load(file)
except FileNotFoundError:
    print(f"Error: The file '{json_file}' was not found.")
    students = []

# Print original list
print_student_list(students, "Original Student List:")

# Add Nitika Timalsina to the student list
new_student = {
    "F_Name": "Nitika",
    "L_Name": "Timalsina",
    "Student_ID": 5067,
    "Email": "Niti8499@gmail.com"
}

# Check if Nitika Timalsina is already in the list to avoid duplicates
exists = any(
    student["F_Name"] == "Nitika" and student["L_Name"] == "Timalsina"
    for student in students
)
if not exists:
    students.append(new_student)
    print("\nNitika Timalsina has been added to the student list.")
else:
    print("\nNitika Timalsina is already in the student list.")

# Print updated list
print_student_list(students, "Updated Student List:")

# Save updated list back to JSON file
with open(json_file, "w") as file:
    json.dump(students, file, indent=4)

print("\nThe JSON file has been updated.")
