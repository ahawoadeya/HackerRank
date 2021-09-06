import textwrap

def wrap(string, max_width):
    # textwrap.wrap returns a list
    return "\n".join(textwrap.wrap(string, max_width))

string = input("Enter string: ")
max_width = int(input("Enter a desired width - (an integer): "))

result = wrap(string, max_width)
print(result)

#  another way to do it without textwrap package

# string = input()
# width = int(input())
# truncated_strings = []

# for index in range(0, len(string), width):
#     truncated_strings.append(string[index : index + width])


# print(truncated_strings)