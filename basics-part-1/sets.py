# unordered collections of unique objects
# cannot access values via indices

my_set = {1,2,3,4,5}

my_set.add(100)
my_set.add(2) 
print(my_set) # note: 2 is not added b/c it exists already

my_list = [1,2,3,4,5,5]
print(list(set(my_list))) # creates a list w/o duplicates
