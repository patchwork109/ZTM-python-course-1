is_magician = True
is_expert = False 

def magic_checker():
    if is_magician and is_expert:
        print("You are a master magician!")
    elif is_magician and not is_expert:
        print("You're getting there.")
    else:
        print("You need magic powers.")

magic_checker()