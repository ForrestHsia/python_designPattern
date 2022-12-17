from abc import ABCMeta, abstractmethod

class WaterHeater:
    
    def __init__(self):
        self.__observers = []
        self.__temperature = 25
    
    def getTemperature(self):
        return self.__temperature
    
    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("目前溫度:" + str(self.__temperature) + " ")
        self.notifies()
    
    def addObserver(self, observer):
        self.__observers.append(observer)
    
    def notifies(self):
        for observer in self.__observers:
            observer.update(self)

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, WaterHeater):
        pass

class WashingMode(Observer):
    def __init__(self):
        self.__calling = 0
    
    def update(self, waterHeater):
        if waterHeater.getTemperature() >= 40 and waterHeater.getTemperature() < 50:
            if self.__calling < 4:
                self.__calling += 1
                print("可以洗澡了！！趕快滾去洗！！！！")
            elif self.__calling >= 4:
                self.__calling += 1
                print("叫很多遍了！！趕快去洗澡！！！！")
        elif waterHeater.getTemperature() >= 50 and waterHeater.getTemperature() < 70:
            if self.__calling < 20:
                self.__calling += 1
                print("這麼燙沒辦法洗啦！！！！！")
        elif waterHeater.getTemperature() >= 70:
            print(f"幹真的太燙了啦{waterHeater.getTemperature()}度了誒！！！！！")
            
            

class DrinkingMode(Observer):
    def update(self, waterHeater):
        if waterHeater.getTemperature() > 100:
            print("水燒開了！！可以喝了！！")
            
