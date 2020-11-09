class Symbol:
    color = ('red','black')
    def __init__(self,icon):
        self.icon = icon

# child class
class Card(Symbol): 
    def __init__(self,value,icon):
        Symbol.__init__(self,icon)
        self.value = value

    def __str__(self):
        return ' {0} of {1} '.format(self.value,self.icon)