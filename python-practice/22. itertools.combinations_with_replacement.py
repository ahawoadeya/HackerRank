from itertools import combinations_with_replacement

S, k = input().upper().split()
print(S, k)

if(0 < int(k) <= len(S)):
    for c in combinations_with_replacement(sorted(S), int(k)):
        print("".join(c))
