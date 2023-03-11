from operator import add
import numpy as np
N = int(input("")) #Enter number of elements
if(0 <= N <= 100):
    str1 = input("") #Enter elements of first array 
    str2 = input("") #Enter elements of second array
    a = [int(x) for x in str1.split()]
    b = [int(x) for x in str2.split()]
    if(len(a) and len(b) == N):
        output = list( map(add, a, b) )
        for i in range(len(output)):
            print(output[i], end=" ")

    else:
        print("Number of elements in your array is not equal to " + str(N) + " or elements is not between 0 and 100")
else:
    print("Number of elements is not between 0 and 100")