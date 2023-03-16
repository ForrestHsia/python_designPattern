class Frog:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def interact_with(self, obstacle):
        print(f"{self.name} the Frog encounters {obstacle} and {obstacle.action()}!!")
        

class Bug:
    def __str__(self):
        return "A Bug"
    
    def action(self):
        return "Eats it"
    
class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    
    def __str__(self):
        return "\n\n\t+++++++++ Welcome to the Frog World +++++++++"
    
    def make_charactor(self):
        return Frog(self.player_name)
    
    def make_obstacle(self):
        # obstacle的生成，要再更 random 與多元
        return Bug()
    