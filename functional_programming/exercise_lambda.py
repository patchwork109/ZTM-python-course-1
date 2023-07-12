# Exercise 1: square each number in 'my_list'
my_list = [3,4,5]

# solved using a standard function
def squared(num_list):
    squared_nums = []
    for num in num_list:
        squared_nums.append(num**2)
    return squared_nums

print(squared(my_list))

# solved using a lambda expression
print(list(map(lambda num: num**2, my_list)))


# Exercise 2: sort the list by the second number in each tuple
list_of_tuples = [(0,2), (4,3), (10,-1), (9,9)]

# def sorted_list(a_list):
#     sorted_list_of_tuples = []
#     for each_tuple in a_list:
#         sorted_list_of_tuples.append(each_tuple)
#     return sorted(sorted_list_of_tuples)

# print(sorted_list(list_of_tuples))

list_of_tuples.sort(key=lambda x: x[1])
print(list_of_tuples)
