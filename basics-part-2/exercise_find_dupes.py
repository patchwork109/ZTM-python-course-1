# Check for duplicates in the list
my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

def duplicate_checker(a_list):
    unique_list = []
    dupe_list = []
    for item in a_list:
        if item not in unique_list:
            unique_list.append(item)
        else:
            dupe_list.append(item)
            print(f"This {item} is a dupe!")
    print(f"Dupes: {dupe_list}")
    print(f"Uniques: {unique_list}")

duplicate_checker(my_list)


def duplicate_checker2(a_list):
    dupe_list = []
    for item in a_list:
        if a_list.count(item) > 1 and item not in dupe_list:
            dupe_list.append(item)
    print(dupe_list)

duplicate_checker2(my_list)


# Check for duplicates in a string
my_string = 'hellllooo'
def duplicate_checker3(any_string):
    dupe_list = []
    for letter in any_string:
        if any_string.count(letter) > 1 and letter not in dupe_list:
            dupe_list.append(letter)
    return dupe_list

print(duplicate_checker3(my_string))


# other method using sets instead of looping
def duplicate_checker4(any_string):
    if len(any_string) != len(set(any_string)):
        print("We have dupes!")
        return True
    
print(duplicate_checker4(my_string))