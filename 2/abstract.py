from abc import ABCMeta, abstractmethod

class Water:
    def __init__(self, state):
        self.__temperature = 25
        self.__state = state
        
    def setState(self, state):
        self.__state = state
        
    def changeState(self, state):
        if (self.__state and self.__state.getName() != state.getName()):
            print("由" + self.__state.getName() + "變成" + state.getName())
        elif (self.__state and self.__state.getName() == state.getName()):
            print("狀態沒有改變，依舊是" + self.__state.getName())
        else:
            print("初狀態為 " + state.getName())
        self.__state = state
    
    def getTemperature(self):
        return self.__temperature
    
    def setTemperature(self, temperature):
        self.__temperature = temperature
        if(self.__temperature <= 0):
            self.changeState(SolidState("固態"))
        elif(self.__temperature <= 100):
            self.changeState(LiquidState("液態"))
        else:
            self.changeState(GaseousState("氣態"))
    
    def riseTemperature(self, step):
        self.setTemperature(self.__temperature + step)
    
    def reduceTemperature(self, step):
        self.setTemperature(self.__temperature - step)
    
    def behavior(self):
        self.__state.behavior(self)

class State(metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name
        
    def getName(self):
        return self.__name
    
    @abstractmethod
    def behavior(self, water):
        pass

class SolidState(State):
    def __init__(self, name):
        super().__init__(name)
    def behavior(self, water):
        print("固態，目前溫度：" + str(water.getTemperature()) + "度")
        
class LiquidState(State):
    def __init__(self, name):
        super().__init__(name)
    def behavior(self, water):
        print("液態，目前溫度：" + str(water.getTemperature()) + "度")

class GaseousState(State):
    def __init__(self, name):
        super().__init__(name)
    def behavior(self, water):
        print("氣態，目前溫度：" + str(water.getTemperature()) + "度")
        
def testState():
    water = Water(LiquidState("液液液液液液"))
    water.behavior()