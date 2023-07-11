# https://www.w3schools.com/python/python_ref_string.asp

quote = 'to be or not to be'
quote2 = 'TO BE OR NOT TO BE'

print(quote.upper()) # -> TO BE OR NOT TO BE
print(quote.capitalize()) # -> To be or not to be
print(quote2.lower()) # -> to be or not to be
print(quote.find('be')) # -> 3 (e.g. starts at an index of 3)
print(quote.replace('be', 'me')) # -> to me or not to me
print(quote.count('be')) # -> 2
