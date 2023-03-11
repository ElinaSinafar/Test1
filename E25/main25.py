num = int(input()) - 1
inpt = input().split()
result = ""
for i in range(num, -1, -1):
    result += inpt[i] + ' '

print(result)
