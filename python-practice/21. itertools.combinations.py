from itertools import combinations

S, k = input().upper().split()
print(S, k)

if(0 < int(k) <= len(S)):
    for i in range(1, int(k) + 1):
        for j in combinations(sorted(S), i):
            print("".join(j))