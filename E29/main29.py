maxnumber = 100
counter = [0 for i in range(maxnumber)]
number = int(input())

xs = [int(x) for x in input().split()]
for x in xs:
    counter[x - 1] += 1

mn = -1
for i in range(maxnumber):
    if counter[i] > 0 and (mn == -1 or counter[mn] > counter[i]):
    	mn = i

print(mn + 1)
    
