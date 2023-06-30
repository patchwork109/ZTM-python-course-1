# one way to write a function
def multiply_by_2(a_list):
    multiplied_nums = []
    for num in a_list:
        multiplied_nums.append(num * 2)
    return multiplied_nums

print(multiply_by_2([1,2,3]))

# method of writing the same function using map()
def multiply_by_2_again(num):
    return num * 2  

print(list(map(multiply_by_2_again, [1,2,3])))
# note: must convert it to a list or else will get a map object