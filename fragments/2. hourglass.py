# https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=false

def hourglass_sum(arr):
    sum = []


    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1]
                    [j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])

    return max(sum)


lst = [52,58,75,42,69,36]

# for _ in range(6):
#     arr.append(list(map(int, input().rstrip().split())))

# populate array
# for values in enumerate(range(0, 6)):
#     arr_ele = int((input("Enter element {0}: ".format(values[0]))))
#     lst.append(arr_ele)

result = hourglass_sum(lst)

print(result)
