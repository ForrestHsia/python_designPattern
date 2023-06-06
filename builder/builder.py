from enum import Enum
import time, pizza

PizzaProcess = Enum("PizzaProcess", "queued preparation baking ready")
PizzaDough = Enum("PizzaDough", "thin thick")
PizzaSauce = Enum("PizzaSauce", "tomato creme_fraiche")
PizzaTopping = Enum("PizzaTopping", "mozzarella double_mozzarella bacon mushrooms ham onion oregano")

STEP_DELAY = 3


class MargaritaBuilder:
    def __init__(self):
        self.pizza = pizza.Pizza("margarita")
        self.progress = PizzaProcess.queued
        self.bakingTime = 5 
    
    def prepare_dough(self):
        self.progress = PizzaProcess.preparation
        self.pizza.prepare_dough(PizzaDough.thin)
    
    def add_source(self):
        print(f"Adding tomato source to the {self.pizza.name}")
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print(f"Adding {self.pizza.sauce} is done.")
        
    def add_topping(self):
        print(f"Adding topping to the {self.pizza.name}")
        self.pizza.topping.append([i for i in (PizzaTopping.double_mozzarella, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print(f"Adding {self.pizza.sauce} is done.")
        
    def bake(self):
        self.progress = PizzaProcess.baking
        print(f"baking {self.pizza.name} for {self.bakingTime} secs")
        self.progress = PizzaProcess.ready
        print(f"{self.pizza.name} is done.")


class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = pizza.Pizza("creamyBacon")
        self.progress = PizzaProcess.queued
        self.bakingTime = 15
    
    def prepare_dough(self):
        self.progress = PizzaProcess.preparation
        self.pizza.prepare_dough(PizzaDough.thick)
    
    def add_source(self):
        print(f"Adding creme_fraiche to the {self.pizza.name}")
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print(f"Adding {self.pizza.sauce} is done.")
        
    def add_topping(self):
        print(f"Adding topping to the {self.pizza.name}")
        self.pizza.topping.append([i for i in (PizzaTopping.mozzarella, PizzaTopping.bacon, PizzaTopping.ham, PizzaTopping.mushrooms, PizzaTopping.onion, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print(f"Adding {self.pizza.sauce} is done.")
        
    def bake(self):
        self.progress = PizzaProcess.baking
        print(f"baking {self.pizza.name} for {self.bakingTime} secs")
        self.progress = PizzaProcess.ready
        print(f"{self.pizza.name} is done.")

class Waiter:
    def __init__(self):
        self.builder = None
    
    def contruct_pizza(self, builder):
        self.builder = builder
        [step() for step in (builder.prepare_dough, builder.add_source, builder.add_topping, builder.bake)]
    
    @property
    def pizza(self):
        return self.builder.pizza
    
def validate_style(builders):
    valid_input = False
    try:
        pizza_style = input("choose one, [m]argarita or [c]reamyBacon?")
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError as err:
        print("hey, fucker, we have only two options, [m]argarita and [c]reamyBacon.")
        return(valid_input, None)
    return (valid_input, builder)

def main():
    builders = dict(m=MargaritaBuilder,c= CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print()
    waiter = Waiter()
    waiter.contruct_pizza(builder)
    pizza = waiter.pizza
    print()
    print(f"enjoy your {pizza}!!")
    
if __name__ == '__main__':
    main()