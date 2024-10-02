import functools

student_dict = {} 
 
# Validate number of students (it should be a positive integer)
while True:
    try:
        n = int(input("Enter the number of students: "))
        if n > 0:
            break
        else:
            print("The number of students must be a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of students.")
  
for i in range(n): 
    # Get roll number and ensure it does not repeat
    while True:
        roll_number = input("Enter the student roll number: ") 
        if roll_number in student_dict:
            print(f"Roll number {roll_number} already exists. Please enter a different roll number.")
        else:
            break 
    
    # Validate name input (it should be a string)
    while True:
        name = input("Enter the student name: ")
        if name.isalpha():  # Check if the name only contains letters
            break
        else:
            print("Invalid name. Please enter a valid string for the name.")

    # Validate age input (it should be an integer)
    while True:
        try:
            age = int(input("Enter the age of the student: "))
            if age > 0:  # Check if the age is positive
                break
            else:
                print("Age must be a positive integer.")
        except ValueError:
            print("Invalid input for age. Please enter a valid integer.")

    # Validate grade input (it should be a float)
    while True:
        try:
            grades = float(input("Enter the grade: "))
            if 0 <= grades <= 100:  # Assuming grades are between 0 and 100
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input for grades. Please enter a valid floating-point number.")

    # Store the validated inputs in the dictionary
    student_dict[roll_number] = {'name': name, 'age': age, 'grade': grades} 

print("Student Dictionary:")
print(student_dict)

student_roll_names = list(map(lambda item: (item[0], item[1]['name']), student_dict.items()))
print("List of Roll Numbers and Student Names:", student_roll_names)

student_roll_ages = list(map(lambda item: (item[0], item[1]['age']), student_dict.items()))
print("List of Roll Numbers and Student Ages:", student_roll_ages)

student_roll_grades = list(map(lambda item: (item[0], item[1]['grade']), student_dict.items()))
print("List of Roll Numbers and Student Grades:", student_roll_grades)

threshold = float(input("\nEnter the grade threshold: "))

# Loop to ensure a valid comparison operator is entered
while True:
    comparison = input("Do you want to find students with grades (>= / <= / ==)? ").strip().lower()
    if comparison in [">=", "<=", "=="]:
        break  
    else:
        print("Invalid comparison option. Please enter one of: >=, <=, ==")


def check_grade(student, threshold, comparison):
    if comparison == ">=":
        return student["grade"] >= threshold  
    elif comparison == "<=":
        return student["grade"] <= threshold  
    elif comparison == "==":
        return student["grade"] == threshold
    else:
        print("Invalid comparison option.")
        return False


filtered_students = list(filter(lambda roll_num: check_grade(student_dict[roll_num], threshold, comparison), student_dict))

print("\nStudents matching your criteria:")
for roll_num in filtered_students:
    student = student_dict[roll_num]
    print(f"Roll Number: {roll_num}, Name: {student['name']}, Grade: {student['grade']}")  # Changed "marks" to "grade"


grades = list(map(lambda student : student['grade'], student_dict.values()))
grades_total = functools.reduce(lambda a, b: a+b, grades)
max_grade = functools.reduce(lambda a, b: a if a > b else b, grades)
print("\nThe sum of the grades : ", grades_total)



for roll_num, student in student_dict.items():
    if student['grade'] == max_grade:
        print(f"Roll Number: {roll_num}, Name: {student['name']}, Grade: {student['grade']}")


total_passed_grades = functools.reduce(lambda a, b: a + b,
    map(lambda roll_num: student_dict[roll_num]['grade'],  
        filter(lambda roll_num: check_grade(student_dict[roll_num], threshold, comparison), student_dict)))

print("\nThe highest grade among the students : ", max_grade)