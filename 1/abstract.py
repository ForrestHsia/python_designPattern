from abc import ABCMeta, abstractmethod

class Oberserver(metaclass=ABCmeta):
    @abstractmethod
    def update(self, observable, object):
        pass
    
class Observable:
    
    def __init__(self):
       self.__observers = []
    
    def addObservers(self, observer):
        self.__observers.append(observer)
        
    def removeObservers(self, observer):
        self.__observers.remove(observer)
    
    def notifyObservers(self, object = 0):
        for o in self.__observers:
            o.update(self, object)