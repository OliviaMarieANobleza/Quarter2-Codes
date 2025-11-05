num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

total_class_average = 0  # to store total of all students' averages


for student in range(1, num_students + 1):
    print(f"\nStudent {student}")
    total_student = 0  # total score for this student

    for subject in range(1, num_subjects + 1):
        score = float(input(f"Enter score {subject}: "))
        total_student += score

    student_average = total_student / num_subjects
    print(f"Average for Student {student} = {student_average:.1f}")

    total_class_average += student_average

class_average = total_class_average / num_students
print(f"\nClass Average = {class_average:.1f}")


