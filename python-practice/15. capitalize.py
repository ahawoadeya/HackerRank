s = input().split(' ')
new_s = []

for each in s:
    new_s.append(each.capitalize())

capitalized_name = " ".join(new_s)
print(capitalized_name)