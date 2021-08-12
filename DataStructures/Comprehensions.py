items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 19),
    ("Product4", 13),
]

prices = list(map(lambda item: item[1], items))
# this is comprehension list
prices = [item[1] for item in items]

filtred = list(filter(lambda item: item[1] >= 10, items))
# this is comprehension list
filtred = [item for item in items if item[1] >= 10]