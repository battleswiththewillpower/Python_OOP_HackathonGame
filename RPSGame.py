import random
# We are making a rock paper scissors game ✓
# create players in the game ✓
# we need to create three classes  ✓
# after classes are created we need to add functionality for the classes to interract
# then we need to create a hiearchy or rules that the classes follow when they interract with eachother to declare a winner
    # ie rock beats scissors, paper beats rock, scissors beats paper
        # need to add cases/rules for if we tie rock v rock etc
            # keep track of winner & loser tallies after results

# for the game 
# it will be a user vs the computer✓
# user will choose an input ie. rock paper scissors
# computer will randomly generate with random.randint(1,3)
# The game will decide the winner given the established rules/parameters
class RockPaperScissors:
    possible_action = ["Rock","Paper", "Scissors"]
    def __init__ (self, name):
        self.name = name
        

    def User_action(self, User):

        return self

    def computer_action(self, Computer):
        Computer = random.randint(0,2)
        randint = 
        print("Wowowow")
        return self

print("work plz")

# determining winner
def winner(user_action == computer_action):
    if user_action == computer_action:
        print(f"Both players chose {user_action}, it is a tie.")

Ashley = RockPaperScissors("Ashley")
Tanner = RockPaperScissors("Tanner")
Ian = RockPaperScissors("Ian")
Wendy = RockPaperScissors("Wendy")

Computer = RockPaperScissors("Opponent")










    # def rock(self): 
    #     print(f"You chose {}, {self.name} chose {}")
    #     return self

    # def paper(self):
    #     print(f"You chose {}, {self.name} chose {}")
    #     return self

    # def scissors(self):
    #     print(f"You chose {}, {self.name} chose {}")
    #     return self
