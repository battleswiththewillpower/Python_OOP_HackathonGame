import random



class Character:
    all_character = []
    def __init__(self, name, health=100, strength=10, speed=1):
        self.name = name
        self.health = health
        self.strength = strength
        self.speed = speed
        Character.all_characters.append(self)

    def show_stats(self):
        print(f"{self.name}")
        print(f"{self.health}")
        print(f"{self.speed}")
        print(f"{self.strength}")
        return self

    def changing_health(self, amount):
        self.health += amount
        return self

    def kick(self, attackee):
        print(f"{self.name} is kicking {attackee.name}")
        connect_roll = random.randint(1, 30)
        if connect_roll > attackee.speed:
            print(f"{self.name} kicked {attackee.name}")
            self.changing_health(-attackee.speed)
            # print(f"{attackee} has taken {self.changing_health}")
            # try and show how much damage was taken after each successful action if possible
        else:
            print("missed")
            return self

    def throw(self, attackee):
        print(f"{self.name} is trying to throw {attackee}")
        connect_roll = random.randint(1, 40)
        if connect_roll > attackee.strength:
            print(f"{self.name} threw {attackee}")
            self.changing_health(-attackee.speed)
        else:
            print(f"{attackee} is too heavy")

    def gaurd(self, attacker):
        print(f"{self.name} is gaurding against {attacker.name}")
        block_roll = random.int(1, 13)
        if block_roll<self.speed:
            return False
        else:
            damage = random.randint(0, attacker.strength)
            print(f"{self.name} took {damage} amount of damage")
            self.changing_health(-attacker.strength)
        return self

