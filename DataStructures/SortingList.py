numbers = [3, 51, 124, 2, 8, 6, 10]
numbers.sort()
print(numbers)

#Descending order
#numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))
print(numbers)

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 19),
    ("Product4", 13),
]

#def sort_item(item):
 #   return item[1]
#a lamda function can only have one expression
items.sort(key=lambda item: item[1])
print(items)