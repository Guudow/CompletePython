#Sets are used to store multiple items in a single variable
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}
# second.add(5)
# second.remove(5)
# len(second)
#(uniques)

print(first | second)
print(first & second) # only will print first and second
print(first - second)
print(first ^ second)

