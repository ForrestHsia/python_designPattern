import factory.frogFac as FrogFactory, factory.WizardFac as WizardFactory

class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_charactor()
        self.obstacle = factory.make_obstacle()
    
    def play(self):
        self.hero.interact_with(self.obstacle)

def validate_age(name):
    try:
        age = input(f"Welcome, {name}. How old are you?")
        
        # 年齡判定可以再優化
        
        age = int(age)
    except ValueError as err:
        print(f"Age {age} is invalid, please try again.")
        return False, age
    
    return True, age

def main():
    name = input(f"Good day, player. Please input your name:")
    valid_age = False
    while not valid_age:
        valid_age, age = validate_age(name)
    game = FrogFactory.FrogWorld if age < 18 else WizardFactory.WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()
    
if __name__ == "__main__":
    main()