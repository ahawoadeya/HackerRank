# initialize empty array
arr = []
# specify array length
arr_count = int(input("Enter number of array elements: ").strip())

# populate array
for values in enumerate(range(0, arr_count)):
    arr_ele = int((input("Enter element {0}: ".format(values[0]))))
    arr.append(arr_ele)
# arr = list(map(int, input("Enter a number string e.g 37648937: ").rstrip().split()))
print("Original array: {}".format(arr))

# reverse method 1. slicing
# print("Reversed array: {0}".format(arr[::-1]))

# method 1 - using the reversed() built-in function
print("Reversed array: {0}".format(list(reversed(arr))))
#[ele for ele in reversed(a)]
