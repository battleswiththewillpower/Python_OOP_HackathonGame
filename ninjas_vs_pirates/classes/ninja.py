from classes.characters import Character

class Ninja(Character):

    def __init__( self , name ):
        self.name = name
        self.strength = 14
        self.speed = 9
        self.health = 90
    
    # def show_stats( self ):
    #     print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    # def attack( self , pirate ):
    #     pirate.health -= self.strength
    #     return self

    # def throw (self, pirate):
    #     pirate.health -= self.speed
    #     return self
    
    # def kick (self, pirate):
    #     pirate.health -= self.strength