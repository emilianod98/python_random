### Python For Loops ###

# Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


# Looping Through a String
for x in "banana":
    print(x)


# The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


# The range() Function
for x in range(6):
    print(x)

for x in range(2, 30, 3):
    print(x) # Imprime desde el 2 hasta el 30 en saltos de 3


# Else in For Loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")


# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


# The pass Statement
for x in [0, 1, 2]:
    pass