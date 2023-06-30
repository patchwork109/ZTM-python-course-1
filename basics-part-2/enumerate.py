for index, char in enumerate("hellllooo"):
    print(index, char)
# 0 h
# 1 e
# 2 l
# 3 l
# 4 l
# 5 l
# 6 o
# 7 o
# 8 o

for index, char in enumerate(list(range(100))):
    if char == 50:
        print(f"We've reached the index of {index} for {char}!")