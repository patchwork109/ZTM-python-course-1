#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def name_capitalizer(name_list):
    capitalized_names = []
    for name in name_list:
        capitalized_names.append(name.capitalize())
    return capitalized_names

print(name_capitalizer(my_pets))


def name_capitalizer2(name):
    return name.capitalize()

print(list(map(name_capitalizer2, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def score_filter(score_list):
    over_fifty = []
    for num in score_list:
        if num > 50:
            over_fifty.append(num)
    return sorted(over_fifty)

print(score_filter(scores))


def score_filter2(score):
    return score > 50

print(list(filter(score_filter2, sorted(scores))))
