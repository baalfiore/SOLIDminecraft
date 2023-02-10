from ItemTypes import ItemType

class Item(object):
    def __init__(self, itemName):
        self._itemName = itemName
        self.type = None
    
    @property
    def itemName(self):
        return self._itemName
    
    @itemName.setter
    def itemName(self, val):
        self._itemName = val

    @property
    def itemTypes(self):
        if self.itemTypes == None:
            print("Empty list!")
        else:
            return self._itemTypes

    def listAllItemTypes(self):
        for i in self.itemTypes:
            print(i.name)


    @itemTypes.setter
    def itemTypes(self, val):
        self._itemTypes.append(val)
    
class Food(Item):
    def __init__(self, itemName:str):
        Item.__init__(Item,itemName)
        self._itemTypes = [ItemType.CONSUMABLE, ItemType.THROWABLE] 
        Item.itemTypes = self._itemTypes
        self._charges = 0
    
    def consume(self):
        print(f"Eating {super()._itemName}")

    @property
    def charges(self):
        return self._charges

    @charges.setter
    def charges(self, val):
        self._charges = val

class Seed(Item):
    def __init__(self, itemName: str, stageLimit: int):
        self._I = Item.__init__(self, itemName)
        self._stages = 0
        self._stageLimit = stageLimit
        self._fullYield = 0
        self._currYield = 0
        self._itemtypes = [ItemType.HARVESTABLE , ItemType.THROWABLE , ItemType.CONSUMABLE , ItemType.PLANTABLE]

    def plant_seed(self):
        print("Planting Seed")

    @property
    def currYield(self):
        return self._currYield
    
    @currYield.setter
    def currYield(self, value):
        self._currYield = value

    @property
    def fullYield(self):
        return self._currYield
    
    @fullYield.setter
    def fullYield(self, value):
        self._fullYield = value

    def grow(self):
        if (self._stages >=0 and self._stages <= self._stageLimit):
            self._stages += 1
        else:
            print("Plant has came to fruition!")

class Fruit(Food):
    def __init__(self, itemName:str, bites:int):
        super().__init__(itemName)
        self._usesLeft = bites
        Item.itemTypes.append(ItemType.HARVESTABLE)
        #Food.itemTypes = Food.itemTypes.append(ItemType.HARVESTABLE)
    
        #self._itemtypes = ItemType.HARVESTABLE | ItemType.CONSUMABLE

    def acquire_seed(self):
        return Seed