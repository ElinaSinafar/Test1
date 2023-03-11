arr = []
num = int(input())
while num != 0:
    arr.append(num)
    num = int(input())

for i in range(len(arr)-1, -1, -1):
    print(arr[i])