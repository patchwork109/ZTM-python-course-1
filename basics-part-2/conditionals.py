is_old = True
is_licensed = True

if is_old:
    print("You are old enough to drive!")
elif is_licensed:
    print("You can drive now!")
else:
    print("You are not old enough to drive!")
print("Checks done!")


if is_old and is_licensed:
    print("You are old enough to drive and have a license!")
else:
    print("You cannot drive!")
print("Checks done!")