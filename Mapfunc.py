def printValAdd(x):
    return x+x

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(printValAdd, numbers)
print(list(result))