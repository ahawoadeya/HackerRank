loop_limit = int(input())

if (1 <= loop_limit <= 150):
    for iterator in range(1, (loop_limit + 1)):
        print(iterator, end='')