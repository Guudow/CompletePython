try:
    age = int(input("Age:"))
except ValueError:
    print("you didn't enter a valid age")
else:
    print("No exceptions were thrown.")
print("Excution continues.")

try:
    age = int(input("Age:"))
except ValueError as ex:
    print("you didn't enter a valid age")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown.")
print("Excution continues.")