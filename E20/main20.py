def gcd(x,y):
    for i in range(x,0,-1):
        if x % i == 0 and y % i == 0:
            return i
def lcm(x,y):
    return x * y // gcd(x,y)
n = int(input())
ans = 1
for i in range(1,n):
    if gcd(i,n) == 1:
        ans = lcm(ans,i)
print(ans)
