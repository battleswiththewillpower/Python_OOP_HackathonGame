from classes.characters import Character

class Pirate(Character):

    def __init__( self , name ):
        self.name = name
        self.strength = 20
        self.speed = 5
        self.health = 125

    # def show_stats( self ):
    #     print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    # def attack ( self , ninja ):
    #     ninja.health -= self.strength
    #     return self

    # def throw (self, ninja):
    #     ninja.health -= self.strength
    #     return self

    # def kick (self, ninja):
    #     ninja.health -= self.speed
    #     return self


