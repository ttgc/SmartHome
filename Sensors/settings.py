
class Settings:
    def __init__(self, HouseName = "SmartHome2", ClimOn = 30, ClimOff = 23, HeatOn = 15, HeatOff = 20, TempUnit = 'C'):
        self.house_name = HouseName
        self.clim_on = ClimOn
        self.clim_off = ClimOff
        self.heat_on = HeatOn
        self.heat_off = HeatOff
        self.temperature_unit = TempUnit

    def setUnit(self, u):
        if u == "C" or u == "F" :
            self.temperature_unit = u
        else:
            print("Unknown unit : " + str(u))

    def setHouseName(self, name):
        self.house_name = name

    def setClimOn(self, v):
        self.clim_on = v

    def setClimOff(self, v):
        self.clim_off = v

    def setHeatOn(self, v):
        self.heat_on = v

    def setHeatOff(self, v):
        self.heat_off = v
