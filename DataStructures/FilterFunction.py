items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 19),
    ("Product4", 13),
]

filtred = list(filter(lambda item: item[1] >= 10, items))
print(filtred)