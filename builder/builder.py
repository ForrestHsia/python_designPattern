from enum import Enum
import time, pizza

PizzaProcess = Enum("PizzaProcess", "queued preparation baking ready")
PizzaDough = Enum("PizzaDough", "thin thick")
PizzaSauce = Enum("PizzaSauce", "tomato creme_fraiche")
PizzaTopping = Enum("PizzaTopping", "mozzarlla double_mozzarlla bacon mushrooms ham onion oregan")

STEP_DELAY = 3


class MargaritaBuilder:
    def __init__():
        self.pizza = pizza.Pizza("margarita")
        self.progress = PizzaProcess.queued
        self.bakingTime = 5 
    
    def prepare_dough(self):
        self.progress = PizzaProcess.preparation
        self.pizza.prepare_dough(PizzaDough.thin)
    
    def add_source(self):
        print(f"Adding tomato source to the {self.pizza.name}")