def reverse_array(a):
    # method 1 - using the reversed() built-in function
    # return [ele for ele in reversed(a)]

    # method 2 - using slicing technique
    return a[::-1]


# specify array length
arr_count = int(input().strip())

# declare array variable
arr = list(map(int, input().rstrip().split()))
print("Original array: {}".format(arr))

# reversed result
res = reverse_array(arr)

# display reversed result
print("Reversed array: {}".format(res))