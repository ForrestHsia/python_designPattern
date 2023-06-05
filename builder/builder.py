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