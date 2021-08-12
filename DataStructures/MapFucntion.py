items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 19),
    ("Product4", 13),
]

prices = []
for item in items:
    prices.append(item[1])
print(prices)

# another way to do
x = map(lambda item: item[1], items)
for item in x:
    print(item)

#convert this map object into i list object
price = list(map(lambda item: item[1], items))
print(price)