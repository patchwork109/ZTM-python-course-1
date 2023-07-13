class Player:

    membership = True # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('running!')

player1 = Player('Sam', 30)
player2 = Player('Tom', 32)

print(f"Player 1's name is {player1.name}")
print(player2.age)
print(player1.run())
print(player2.membership)


class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

garfield = Cat('Garfield', 4)
figaro = Cat('Figaro', 8)
felix = Cat('Felix', 2)

cats = [garfield, figaro, felix]

def find_oldest_cat(cats):
    oldest_cat = None
    max_age = -1

    for each_cat in cats:
        if each_cat.age > max_age:
            oldest_cat = each_cat
            max_age = each_cat.age
    return oldest_cat

print(f"The oldest cat is {find_oldest_cat(cats).name}")