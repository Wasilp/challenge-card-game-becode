from player import Player,Deck


class Board(Player):
    '''  '''
    turn_count = 0
    def __init__(self,players = 0, active_cards = 0, history_cards = []):
        '''Initializes the data.'''
        self.players = players
        self.turn_count = Board.turn_count
        self.active_cards = active_cards
        self.history_cards = history_cards


    def start_game(self):
        '''start game'''
        nbPlayer = input("Enter the number of player ")
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        self.players = int(nbPlayer)
        for nb in nbPlayer:
            sayMyName = input("Enter player n° "+ nb + " name ")
            Player(sayMyName)
            deck.distribute(nbPlayer)
        self.turn_count += 1

board = Board()
board.start_game()