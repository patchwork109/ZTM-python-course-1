# 1. Start w/ local
# 2. Is there a parent local?
# 3. Global
# 4. Built-in Python functions

a = 1

def confusion():
    a = 5
    return a

print(a) # -> 1, pulling from global scope
print(confusion()) # -> 5, pulling from local scope