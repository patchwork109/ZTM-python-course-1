# format -> while condition: do something

counter = 0
while counter < 50:
    print(f"The count is {counter}")
    counter += 1
print("All done!")


# for vs. while loops

my_list = [1,2,3]
for item in my_list:
    print(item)

i = 0 
while i < len(my_list):
    print(my_list[i])
    i += 1