# student_grades_dict.py

# Create a dictionary of 5 students and their corresponding grades
student_grades = {
    'Student1': 'B',
    'Student2': 'C',
    'Student3': 'A',
    'Student4': 'B',
    'Student5': 'D'
}

# Print the entire dictionary
print("Student Grades:", student_grades)

# Access and print the grade of the 3rd student
print("Grade of third student:", student_grades['Student3'])

# Update the grade of the 2nd student
student_grades['Student2'] = 'A'

# Delete the entry of the 5th student
del student_grades['Student5']

# Print the last key-value pair in the dictionary
last_item = list(student_grades.items())[-1]
print("Last key-value pair:", last_item)
