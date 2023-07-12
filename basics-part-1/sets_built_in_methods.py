my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set)) # -> {1,2,3}
print(your_set.difference(my_set)) # -> {6, 7, 8, 9, 10}

print(my_set.discard(5))
print(my_set) # modifies the set, no longer has 5 -> {1,2,3,4}

print(my_set.add(5))
print(my_set)

print(my_set.difference_update(your_set))
print(my_set) # modifies the set with the difference between the sets

both_sets = my_set.union(your_set) 
print(both_sets) # -> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#or
both_sets2 = my_set | your_set
print(both_sets2) # -> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
