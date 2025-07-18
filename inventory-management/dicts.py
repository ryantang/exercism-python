"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    
    return {item: items.count(item) for item in set(items)}


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    return {
        item: inventory.get(item, 0) + items.count(item)
        for item in set(inventory) | set(items)
    }


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    return {
        item: max(inventory.get(item, 0) - items.count(item), 0)
        for item in set(inventory)
    }

    return inventory    

    for item in set(inventory):
        if item in inventory and inventory[item] > items.count(item):
            inventory[item] -= items.count(item)
        elif item in inventory:
            inventory[item] = 0 

    return inventory    


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    inventory.pop(item, None)
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [(item, qty) for item, qty in inventory.items() if qty > 0]