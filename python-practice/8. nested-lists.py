number_of_students = int(input())
students_list = []
all_grades = []
low_score_students = []

def second_smallest(numbers_list):
    duplicate_numbers = set()
    unique_numbers = []

    for number in numbers_list:
        if number not in duplicate_numbers:
            unique_numbers.append(number)
            duplicate_numbers.add(number)
    
    unique_numbers.sort()
    return unique_numbers[1]

if (2 <= number_of_students <= 5):
    for limit in range(0, number_of_students):
        student_name = input()
        student_grade = input()
        try:
            student_grade = int(student_grade)
        except ValueError:
            student_grade = float(student_grade)
        
        inner_list = [student_name, student_grade]
        
        students_list.append(inner_list)

for inner_list in students_list:
    all_grades.append(inner_list[1])

second_lowest_score = second_smallest(all_grades)

for inner_list in students_list:
    if second_lowest_score in inner_list:
        low_score_students.append(inner_list[0])

low_score_students.sort()

for student in low_score_students:
    print(student)