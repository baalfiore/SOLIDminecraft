# THis program is to demonstrate SOLID principles in terms of mine craft.

"""
SOLID Principles:
Single purpose responsibility:
Each tool is designed for a specific purpose
"""

class Tool:
    def __init__(self, tName: str, craftablility:bool, cost:float, description:str):
        self._cost = cost
        self._toolName = tName
        self._isCraftable = craftablility
        self._description = description

    @property
    def toolName(self)-> str:
        return self._toolName
    
    @toolName.setter
    def toolName(self, newTname)-> None:
        self._toolName=newTname

    def use(self):
        print(f"Using {self.toolName}")
    
class PickAxe(Tool):
    def __init__(self, tName: str, craftablility: bool, cost: float, description: str, durability:int):
        super().__init__(tName, craftablility, cost, description)
        self.durability = durability

    def use(self, object):
        if(object.type == "Mineral"):
            return super().use()
        else:
            print(f"Can't use {self.toolName} on {object.Name}")

class GardenHoe(Tool):
    def __init__(self, tName: str, craftablility: bool, cost: float, description: str, durability:int):
        super().__init__(tName, craftablility, cost, description)
        self.durability = durability

