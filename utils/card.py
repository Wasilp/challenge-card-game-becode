# Mother class
# Attribute icon who is the icon of a card
class Symbol:
    color = ("red", "black")

    def __init__(self, icon: str):
        self.icon = icon


# child class
# Attribute icon who is inherited from Symbol
# Attribute value who is the value of a card
class Card(Symbol):
    def __init__(self, value: str, icon: str):
        Symbol.__init__(self, icon)
        self.value = value

    def __str__(self):
        return " {0} of {1} ".format(self.value, self.icon)
