# one time, anonymous function (doesn't have a name)
# format -> lambda param: action on the param

my_list = [1,2,3]

def multiply_by_2(num):
    return num * 2

print(list(map(multiply_by_2, my_list)))

# method using lambda instead of a standard function
print(list(map(lambda num: num * 2, my_list)))