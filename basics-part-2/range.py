print(range(100))
print(range(0, 100)) # same as the above line

for num in range(0, 10):
    print(num)

for _ in range(0, 10, 2):
    print("Sending email!")
# using _ as the variable since it's not being used elsewhere
# range has a start, stop, and stepover
