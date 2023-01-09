def addToInventory(inventory, addedLoot):
    for item in addedLoot:
        if item not in inventory.keys():
            inventory[item] = 1
        else:
            inventory[item] += 1

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
        print(inventory[key], key)
        item_total = item_total + inventory[key]
    print("Total number of items:", item_total)
        
inv = {'gold coin': 4, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
barbarianLoot = ['loincloth', 'dagger', 'dagger', 'hentai etching']
addToInventory(inv, barbarianLoot)
displayInventory(inv)
    