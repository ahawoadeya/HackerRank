if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    # or use list comprehension
    # arr = [int(x) for x in input().split()]

    if (2<= n <= 10):
        if(len(arr) == n):
            if(all(-100 <= score <= 100 for score in arr)):
                duplicate_scores = set()
                unique_scores = []

                for score in arr:
                    if score not in duplicate_scores:
                        unique_scores.append(score)
                        duplicate_scores.add(score)

                unique_scores.sort()

                print(unique_scores[-2])
