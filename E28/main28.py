N = input("")
numbers = [int(x) for x in N.split()]
if(0 < numbers[0] and numbers[1] and numbers[2] < 1000000000000000 and len(numbers) == 3):
   counter = {}
   for i in numbers:
      if i in counter:
            counter[i] += 1
      else:
            counter[i] = 1
   max = max(counter.values())
   minTransformations = 3 - max
   print(minTransformations)
else:
   print("Please enter 3 numbers between 0 and 10^15")