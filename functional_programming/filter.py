# one way to write a function
def check_odd(a_list):
    odd_nums = []
    for num in a_list:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums

print(check_odd([1,2,3,4]))


# method of writing the same function using filter()
def check_odd2(num):
    return num % 2 != 0

print(list(filter(check_odd2, [1,2,3,4])))
# note: must convert it to a list or else will get a filter object