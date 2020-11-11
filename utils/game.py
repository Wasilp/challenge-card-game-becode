from utils.player import Player, Deck


class Board:
    """Board Class"""

    def __init__(self):
        """initialize Board

        Args:
            players (list, optional): list of objPlayer. Defaults to [].
            active_cards (list, optional): list of last cards played by each players from last turn. Defaults to [].
            history_cards (list, optional): list of cards that were played by all players . Defaults to [].
        """
        self.players = []
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []

    def start_game(self):
        """start game
        Ask the user for number of player
        Build deck and fill it
        save the number of cards who need to be distribute among all players in var nbDiv
        loop on number of player to get each name and create all playerObj
        Distribute cards
        Save playerObj in self.players
        """
        print(
            "\x1b[0;30;44m"
            + "**************************************************"
            + "\x1b[0m"
        )
        print(
            "\x1b[0;30;44m"
            + "***             WE TAKE YOUR MONEY             ***"
            + "\x1b[0m"
        )
        print(
            "\x1b[0;30;44m"
            + "***               A Becode Project             ***"
            + "\x1b[0m"
        )
        print(
            "\x1b[0;30;44m"
            + "**************************************************"
            + "\x1b[0m"
        )
        print("\n")
        nbPlayer = int(input("Enter the number of player please.. "))
        deck = Deck()
        deck.fill_deck()
        nbDiv = len(deck.cards) // nbPlayer
        for nb in range(1, nbPlayer + 1):
            playerName = input("Enter the name of player " + str(nb) + ".. ")
            playerObj = Player(playerName)
            deck.distribute(nbPlayer, nbDiv, playerObj)
            self.players.append(playerObj)

        while all(player.number_of_cards > 0 for player in self.players):
            """While player have more than 0 cards
            i loop on the list self.players to know if they played
            if the number of turn is smaller or equal than the Board turn count
            i return the la card played from Player and print it
            then i make playing the player and increment his number of turn and decrement his number of cards
            i update the value of active_cards and history_cards
            print all the value of the operation
            and increment the global counter of the game
            """
            for player in self.players:
                res = playerObj.play(player.name)
                print(res, "I M THE LAST CARD PLAYED")
                player.turn_count += 1
                player.number_of_cards -= 1
                self.active_cards.append(res)
            self.turn_count += 1
            print(player.turn_count, self.active_cards, len(self.history_cards))
            self.history_cards.extend(self.active_cards)
            self.active_cards.clear()

    def __str__(self):
        return self.turn_count


board = Board()
board.start_game()
