# note: dictionary keys must be immutable and unique!

dictionary = {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
}

list_of_dicts = [
    {
        'a': 1,
        'b': 'hello',
        'c': [4,5,6]
    },
    {
        'a': 2,
        'b': 'hiya',
        'c': [7,8,9]
    },
]

print(dictionary['a'])
print(list_of_dicts[0]['c'][2])
print(list_of_dicts[1]['b'])