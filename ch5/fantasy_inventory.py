example = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inv):
    print("Inventory:")
    gc = 0
    for k, v in inv.items():
        print(v, k)
        gc += v
    print("Total number of items: %d" % gc)

displayInventory(example)

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i not in inventory:
            inventory[i] = 1
        else:
            inventory[i] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

