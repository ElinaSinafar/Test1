number = int(input())
answer = 0
for i in range(number):
    s = input()
    distinct_characters = len(s)
    
    for j in range(len(s)):
        d = 0
        for k in range(j):
            if s[j] == s[k]:
                d= 1
        distinct_characters -= d
    
    if distinct_characters > answer:
        answer = distinct_characters

print(answer)
