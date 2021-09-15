from itertools import permutations

S, k = input().upper().split()
print(S, k)

if(0 < int(k) <= len(S)):
    print(*[''.join(i) for i in permutations(sorted(S), int(k))], sep="\n")