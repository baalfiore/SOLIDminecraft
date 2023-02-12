import Tool, Item
import ItemTypes

if __name__ =="__main__":
    print("Starting ... ")

    pAxe = Tool.PickAxe("PickAxe", True, 12.97, "Tool used for mining rocks", 100)
    pAxeName = pAxe._toolName

    blueberry = Item.Fruit("Blueberry", 1,4)
    raspberry = Item.Fruit("Raspberry",1,5)
    apple = Item.Fruit("Apple", 3, 6)

    print(f"Found {pAxeName}")
    print(f"Found {apple.itemName}")
    #print(f"printing item types {apple.itemTypes}")
    apple.listAllItemTypes()