# non-list comprehension method
my_list = []

for char in 'hellllo':
    my_list.append(char)

print(my_list)

# same output using list comprehension
# format -> [expression for variable in iterable]
another_list = [char for char in 'hellllo']
print(another_list)


another_list2 = [num for num in range(100)]
another_list3 = [num ** 2 for num in range(100)]
another_list4 = [num ** 2 for num in range(100) if num % 2 == 0]
print(another_list4)

# examples of set comprehensions (just change the brackets to curly brackets!)
my_set = {num for num in range(100)}
my_set2 = {num ** 2 for num in range(100)}
my_set3 = {num ** 2 for num in range(100) if num % 2 == 0}
print(my_set3)