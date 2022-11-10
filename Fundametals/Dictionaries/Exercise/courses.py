courses = {}

while True:
    command = input()
    if command == "end":
        break

    course_name, student_name = command.split(" : ")

    if course_name not in courses.keys():
        courses[course_name] = [student_name]

    else:
        courses[course_name].append(student_name)

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    print("--", '\n-- '.join(value))

