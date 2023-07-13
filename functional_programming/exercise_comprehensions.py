# Check for duplicates in the list using comprehensions
my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

dupes = list({item for item in my_list if my_list.count(item) > 1})
print(dupes)