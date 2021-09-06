student_records = int(input())
student_marks = {}

for limit in range(0, student_records):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()
marks_list_queried = student_marks[query_name]

avarage = sum(marks_list_queried) / len(marks_list_queried)
print("{:.2f}".format(avarage))