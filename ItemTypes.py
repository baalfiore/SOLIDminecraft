from enum import IntEnum

class ItemType(IntEnum):
    HARVESTABLE = 1
    KILLABLE = 2
    CONSUMABLE = 3
    THROWABLE = 4
    PLANTABLE =5

    def __str__():
        return IntEnum.name