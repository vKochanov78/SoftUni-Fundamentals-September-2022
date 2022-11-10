# academy = {}
# number_of_students = int(input())
#
# for student in range(number_of_students):
#     name = input()
#     grade = float(input())
#
#     if name not in academy:
#         academy[name] = grade
#     elif name in academy:
#         list_of_grades = [academy[name], grade]
#         academy[student] = list_of_grades
#
# for student, grades in academy.items():
#     if type(grades) == list:
#         average_grade = sum(grades) / len(grades)
#     else:
#         average_grade = grades
#     if average_grade >= 4.5:
#         print(student, f'-> {average_grade:.2f}')


students = int(input())
students_grades = {}
for current_student in range(students):
    student_name = input()
    grade = float(input())
    if student_name not in students_grades:
        students_grades[student_name] = grade
    elif student_name in students_grades:
        list_grades = [students_grades[student_name], grade]
        students_grades[student_name] = list_grades

for student, grades in students_grades.items():
    if type(grades) == list:
        average_grade = sum(grades) / len(grades)
    else:
        average_grade = grades
    if average_grade >= 4.5:
        print(student, f'-> {average_grade:.2f}')

