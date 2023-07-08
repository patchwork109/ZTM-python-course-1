# iterable -> list, dictionary, tuple, set, string
# iterate -> check each item in the collection one by one

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user:
    print(item)
# name
# age
# can_swim

for item in user.items():
    print(item)
# ('name', 'Golem')
# ('age', 5006)
# ('can_swim', False)

for item in user.values():
    print(item)
# Golem
# 5006
# False

for item in user.keys():
    print(item)
# name
# age
# can_swim

for key, value in user.items():
    print(key, value)
# name Golem
# age 5006
# can_swim False

for key, value in user.items():
    print(f"key: {key}, value: {value}")