from random import randint
from .wetness_reporter import Style_Text
import sys

color = Style_Text()

wetnesses = dict([
    [1, color.add_color('Very Wet', color.CYAN)],
    [2, color.add_color('So Skwoooooosh', color.GREEN)],
    [3, color.add_color('Slosh Slosh Slosh', color.PURPLE)],
    [4, color.add_color('The Essence of Wetness', color.BLUE)],
    [5, color.add_color('moist', color.YELLOW)],
    [6, None]
])

def setModule(value):
    sys.modules[__name__] = value
    
class Foot:
    def __init__(self, position):
        self.__moisture = wetnesses[randint(1, 6)]
        self.position = position
    
    def release_moisture(self):
        self.__moisture = None
        print(f'{color.add_color(self.position, color.BOLD)} foot wetness {color.add_color("released", color.RED)}')
    
    def observe_moisture(self):
        if self.__moisture is None:
            print(f'{color.add_color(self.position, color.BOLD)} foot wetness is currently {color.add_color("dry", color.UNDER)} :(((')
        else:
            print(f'{color.add_color(self.position, color.BOLD)} foot wetness is currently {self.__moisture}')
    
    def get_water(self):
        if self.__moisture is None:
            return self.__moisture
        else:
            return dict(release_moisture=self.release_moisture, observe_moisture=self.observe_moisture)
    
    def set_water(self, value: str):
        self.__moisture = value
    
    def del_water(self):
        self.__moisture = None
    
    water = property(get_water, set_water, del_water)

# in the foot module
class FootModule:
    def __init__(self):
        feetNames = ['front-right', 'front-left', 'hind-right', 'hind-left']
        feet = self.makeFootDict(feetNames)
        setModule(feet)
    
    def makeFootDict(self, feetNames: list[str]) -> dict[str, Foot]:
        feet = {}
        for footName in feetNames:
            feet[footName] = Foot(footName)
        return feet

FootModule()