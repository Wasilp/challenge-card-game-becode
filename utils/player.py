from card import Card,Symbol
import random

class Player:
    turn_count = 0 
    def __init__(self,name,cards = 0,turn_count = 0,number_of_cards = 0,history = []):
        self.name = []
        self.cards = cards
        self.turn_count = Player.turn_count
        self.number_of_cards = number_of_cards
        self.history = history
    # instance method 
    def play(self, sayMyName):
      print(sayMyName)
      self.name = sayMyName
      myCard = random.choice(self.cards)
      print(myCard)
      self.history.append(myCard)
      self.turn_count += 1
      print (self.name,self.turn_count +'played:'+ myCard.value,myCard.icon)
      return 'card {}'.format(myCard)

class Deck():
# instance attributes
# self.cards is the deck itself
  def __init__(self):
   self.cards = []

  def fill_deck(self):
   values = [ 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K' ]
   icons = ['♥', '♦', '♣', '♠']
   for i in range(0,4):
      for v in range(0,13):
        self.cards.append(Card(values[v],icons[i]))

  def shuffle(self):
    random.shuffle(self.cards)
    print(self.cards)
  
  def distribute(self,nbPLayer,nbDiv):
      Player.number_of_cards = nbDiv
      print(Player.number_of_cards)
      for i in range(Player.number_of_cards):
        deal = self.cards.pop()
        Player.cards = deal
        print(Player.cards)
    
  # def __str__(self):
  #   s = ""
  #   for i in range(len(self.cards)):
  #     s += str(self.cards[i])
  #   return s