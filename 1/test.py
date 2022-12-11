import config

heater = config.WaterHeater()
washingObsv = config.WashingMode()
drinkingObsv = config.DrinkingMode()

heater.addObserver(washingObsv)
heater.addObserver(drinkingObsv)

for i in range(35, 103):
    if i > 100:
        print(f"你８７喔，水都超過100度了啦怎麼可能會超過100度啦")
        break
    heater.setTemperature(i)