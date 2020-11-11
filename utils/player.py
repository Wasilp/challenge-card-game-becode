from utils.card import Card
import random


# Class Player representation of a player
class Player:
    def __init__(
        self, name: str, cards=[], number_of_cards:int = 0, history=[], turn_count: int = 0
    ):
        """[Class Player representation of a player]

        Args:
            name (str): Attribute name who is inherited from Symbol
            cards (list, optional): cards who is list of cards of the Player. Defaults to [].
            number_of_cards (int, optional): Attribute number_of_cards who is number of cards of the Player. Defaults to 0.
            history (list, optional): history who is the history of played card by the Player. Defaults to [].
            turn_count (int, optional): turn_count is the the count of played turn by the Player. Defaults to 0.
        """
        self.name = name
        self.cards = cards
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history

    # instance method play
    # Function who make the user play by picking a random card of his cards list
    # And remove it from it, then append it to his history
    # return the "played card"
    def play(self, name):
        myCard = random.choice(self.cards)
        self.cards.remove(myCard)
        self.history.append(myCard)
        print(name, str(self.turn_count) + " played: " + str(myCard.value), myCard.icon)
        return "card {} {}".format(myCard.value, myCard.icon)

    def __str__(self):
        return self.name


# Class Player representation of a player
# Attribute cards who is the cards from the Deck
class Deck:
    # instance attributes
    # self.cards is the deck itself
    def __init__(self):
        self.cards = []

    # instance method fill_deck
    # Function who fill the main board deck with 52 cards
    def fill_deck(self):
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        icons = ["♥", "♦", "♣", "♠"]
        for i in range(0, 4):
            for v in range(0, 13):
                self.cards.append(Card(values[v], icons[i]))

    # instance method shuffle
    # Function who shuffle the generated deck
    def shuffle(self):
        random.shuffle(self.cards)

    # instance method distribute
    # Function who distribute the deck among all players
    # pop the cards distributed from the deck
    # append the cards to the players cards
    def distribute(self, nbPLayer, nbDiv, playerObj):
        playerObj.number_of_cards = nbDiv
        for i in range(playerObj.number_of_cards):
            deal = self.cards.pop()
            playerObj.cards.append(deal)

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s += str(self.cards[i])
        return s
