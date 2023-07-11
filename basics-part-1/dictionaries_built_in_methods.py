user = {
    'name': 'Sam',
    'basket': ['grapes', 'bananas', 'cheese'],
    'age': 31
}

print(user.get('name')) # -> Sam
print('Sam' in user.values()) # -> True
print(user.values()) # -> (['Sam', ['grapes', 'bananas', 'cheese'], 31])
print(user.keys()) # -> (['name', 'basket', 'age'])
print(user.items()) # -> ([('name', 'Sam'), ('basket', ['grapes', 'bananas', 'cheese']), ('age', 31)])

print(user.pop('age'))
print(user) # no longer includes age

print(user.update({'age': 30}))
print(user) # adds age as a key with the value of 30
