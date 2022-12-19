import abstract as abs

def testState():
    water = abs.Water(abs.LiquidState("液態"))
    water.behavior()
    
    water.reduceTemperature(-4)
    water.behavior()
    
    water.setTemperature(-4)
    water.behavior()
    
    water.setTemperature(114)
    water.behavior()   
    
    water.riseTemperature(37)
    water.behavior()
    
   
    
    
    
testState()