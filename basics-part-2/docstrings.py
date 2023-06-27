def test_function(a):
    '''
    Info: this function prints parameter 'a'
    '''
    print(a)

test_function('!!!')
# in the pop-up box when you call the function, the docstring w/ helper text shows

help(test_function)
# in the pop-up box, the docstring w/ helper text shows

print(test_function.__doc__)
# prints -> Info: this function prints parameter 'a'
