s = input()
vowels = "AEIOU"

kevin_score = 0
stuart_score = 0

for char in range(len(s)):
    if s[char] in vowels:
        kevin_score += (len(s) - char)
    else:
        stuart_score += (len(s) - char)

if kevin_score > stuart_score:
    print("Kevin", kevin_score)
elif kevin_score < stuart_score:
    print("Stuart", stuart_score)
else:
    print("Draw")