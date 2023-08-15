import random
import pygame

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.suit}{self.rank}"


class Deck:
    def __init__(self):
        self.cards = []

        for suit in SUITS:
            for rank in RANKS:
                new_card = Card(suit, rank)
                self.cards.append(new_card)

    def __str__(self):
        cards_str = ', '.join(str(card) for card in self.cards)
        return f'Deck of {len(self.cards)} cards: {cards_str}'

    def shuffle(self):
        random.shuffle(self.cards)


class Player:
    def __init__(self, name):
        self.name = input("Please enter your name: ")
        self.hand = []  # ['A♠, 2♥']

    def display_hand(self):
        print(f"{self.name} has: {', '.join(str(card) for card in self.hand)}")


class Dealer(Player):
    def __init__(self):
        self.name = "Dealer"
        self.hand = []
    #  super().__init__(name)

    def __str__(self):
        return 


class Game():
    def __init__(self):
        self.player_count = 0
        self.name = 'BLACKJACK'
        self.player = Player("Miles")
        self.dealer = Dealer()
        self.deck = Deck()
        self.deck.shuffle()
        print(self.deck)

    def __str__(self):
        return self.name
    
    def add_players(self, player):
        self.players.append(player)
        self.player_count += 1

    def deal_card(self, player):
        if self.deck.cards:
            card = self.deck.cards.pop(0)
            player.hand.append(card)
        else:
            print("Out of Cards!")

    def play_hand(self):
        # for _ in range(2):
        #     for player in self.players:
        #         self.deal_card(self.deck, player)
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.player)
        self.deal_card(self.dealer)

    def play_game(self):
        print(f'Welcome to {self.name}')
        self.play_hand()
        print(self.player.display_hand)
        print(self.dealer.display_hand)



# new_deck = Deck()
# print(new_deck)

# p1 = Player('Miles')
# p2 = Player('Ethan')
# p3 = Dealer()
# p1.display_hand()
# p2.display_hand()
# p3.display_hand()
# new_deck.shuffle()
# print(new_deck)

new_game = Game()
new_game.play_game()

# new_game.deal_cards(new_deck, p1)
# new_game.deal_cards(new_deck, p2)
# new_game.deal_cards(new_deck, p3)
# new_game.deal_cards(new_deck, p1)
# new_game.deal_cards(new_deck, p2)
# new_game.deal_cards(new_deck, p3)
# p1.display_hand()
# p2.display_hand()
# p3.display_hand()