# *args and **kwargs
# allows functions to take as many arguments and keyword arguments w/o 
# explicitly listing every arg as a parameter

def super_function(*args, **kwargs):
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + total

print(super_function(1,2,3,4,5, num1=5, num2=10))