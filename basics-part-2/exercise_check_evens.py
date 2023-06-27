def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False

print(is_even(20))
print(is_even(31))

# other ways to write the function to clean up code

def is_even2(num):
    if num % 2 == 0:
        return True
    else: 
        return False
    
def is_even3(num):
    if num % 2 == 0:
        return True
    return False

def is_even4(num):
    return num % 2 == 0 # this evaluates to True / False directly
