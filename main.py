import Tool, Item

if __name__ =="__main__":
    print("Starting ... ")

    pAxe = Tool.PickAxe("PickAxe", True, 12.97, "Tool used for mining rocks", 100)
    pAxeName = pAxe._toolName

    blueberry = Item.Fruit("Blueberry", 1, 2)
    raspberry = Item.Fruit("Raspberry",1, 2)
    apple = Item.Fruit("Apple", 3, 8)

    print(f"Found {pAxeName}")
    print(f"Found {apple.itemName}")