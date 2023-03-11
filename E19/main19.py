a = int(input())
b = int(input())

if a == 1 and b == 1:
    pass
elif a == 1 and b == 2:
    print(2)
elif a == 2 and b == 2:
    print(2)
else:
    if a == 1 or a == 2:
        print(2)
    if a % 2 == 0:
        start = a+1
    else:
        if a == 1:
            start = 3
        else:
            start = a
    if b % 2 == 0:
        end = b-1
    else:
        end = b

    for i in range(start,end+1, 2):
        is_prime = True
        for j in range(3, int(i**0.5)+1, 2):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)