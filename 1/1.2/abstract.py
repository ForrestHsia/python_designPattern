from abc import ABCMeta, abstractmethod

class Oberserver(metaclass=ABCmeta):
    @abstractmethod
    def update(self, observable, object):
        pass
    
class Observable: