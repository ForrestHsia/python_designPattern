from abc import ABCMeta, abstractmethod

class WaterHeater:
    
    def _init_(self):
        self._observers = []
        self._temperature = 25
    
    def getTemperature(self):
        return self._temperature
    
    def setTemperature(self, temperature):
        self._temperature = temperature
        print("目前溫度:" + str(self._temperature) + " ")
        self.notifies()
    
    def addObserver(self, observer):
        self._observers.append(observer)
    
    def notifies(self):
        for observer in self._observers:
            observer.update(self)

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, waterHeater):
        pass

class WashingMode(Observer):
    def update(self, waterHeater):
        if waterHeater.getTemperature() >= 50:
            