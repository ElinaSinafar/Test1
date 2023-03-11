string = input().split()
keeper = []

i = 0
while i < len(string):
    if i < 2:
        keeper.append(str(1 - int(string[i])))

    elif i < 5:
        keeper.append(str(2 - int(string[i])))

    else:
        keeper.append(str(8 - int(string[i])))
    i += 1

print(" ".join(keeper))
