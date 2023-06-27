is_cool = True
is_cool = False

print(bool(-0))
print(bool(0))
print(bool(1))
print(bool(0.5))
print(bool('0'))
print(bool('True'))
print(bool('False'))
print(bool(False))
print(bool('any random thing'))


def add_counter():
    counter = 1
    print(f"{counter}. {bool(-0)}")
    counter += 1
    print(f"{counter}. {bool(0)}")
    counter += 1
    print(f"{counter}. {bool(1)}")
    counter += 1
    print(f"{counter}. {bool(0.5)}")
    counter += 1
    print(f"{counter}. {bool('0')}")
    counter += 1
    print(f"{counter}. {bool('True')}")
    counter += 1
    print(f"{counter}. {bool('False')}")
    counter += 1
    print(f"{counter}. {bool(False)}")
    counter += 1
    print(f"{counter}. {bool('any random thing')}")

add_counter()
