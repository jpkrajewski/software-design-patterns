class MenuItem:
    def __init__(self, name, price, dish_type):
        self.name = name
        self.price = price
        self.dish_type = dish_type


class MCDonald:
    menu_items = {}

    def __init__(self, localization):
        self.profit = 0
        self.localization = localization

    def sell(self, name):
        self.profit += self.menu_items[name].price
