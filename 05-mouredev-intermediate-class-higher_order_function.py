### HIGHER ORDER FUNCTIONS ###

def sum_one (a):
    return a + 1

def sum_five (a):
    return a + 5

################################
def sum_two_values_and_one (a,b):
    return sum_one(a + b)

print (sum_two_values_and_one(5,2))

################################
def sum_two (a, b ,funcion):
    return funcion(a+b)

print(sum_two(5,2,sum_one))
print(sum_two(5,2,sum_five))


### CLOSURES ###
def make_adder (n):
    def adder (a):
        return a + n
    return adder

add_five = make_adder(5)
print(add_five(10))


print(make_adder(5)(10))


### BUILT-IN HIGHER ORDERFUNCTIONS ###

numbers = [2, 5, 10, 21, 30]

# MAP 
def multiply_two(numbers):
    return numbers*2

print(list(map(multiply_two, numbers)))
print(list(map(lambda x: x*2, numbers)))

# FILTER
def filter_greater_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_ten,numbers)))
print(list(filter(lambda number: number > 10,numbers)))
