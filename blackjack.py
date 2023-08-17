import random
import pygame
from pygame import mixer
import os
import colorama
from colorama import Fore, Style, Back
from card_values import CARD_VALUES

SUITS = [
    f'{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}', f'{Fore.RED}{Style.BRIGHT}♥{Fore.WHITE}{Style.NORMAL}', f'{Fore.RED}{Style.BRIGHT}♦{Fore.WHITE}{Style.NORMAL}', f'{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank}{self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.used_cards = []

        for suit in SUITS:
            for rank in RANKS:
                new_card = Card(rank, suit)
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

    def __str__(self):
        return 


class Game():
    def __init__(self):
        os.system('clear')
        self.player_count = 0
        self.name = 'BLACKJACK'
        self.player = Player("Miles")
        self.dealer = Dealer()
        self.deck = Deck()
        self.deck.shuffle()  # Where i shuffle
        #  print(self.deck)

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
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.player)
        self.deal_card(self.dealer)

    def eval_hand(self, player):
        total = 0
        
        for card in player.hand:
            rank = card.rank
            if rank in CARD_VALUES:
                total += CARD_VALUES[rank]
                if rank == 'A' and total >= 22:
                    total -= 10

        return total

    def hand_compare(self, player_total, dealer_total):  # contains my checks for winner, run after loops and all game data is collected
        if player_total > 21:
            print("Dealer Wins!\n")
        elif dealer_total > player_total:
            print(f"{self.player.name} Wins!\n")
        elif player_total > dealer_total:
            print(f"{self.player.name} Wins!\n")
        elif dealer_total > player_total:
            print("Dealer Wins!\n")
        else:
            print("Yikes its a Tie!\n")

    def clear_hand(self):
        self.deck.used_cards.extend(self.player.hand)
        self.deck.used_cards.extend(self.dealer.hand)
        self.player.hand.clear()
        self.dealer.hand.clear()

    def play_game(self):
        play_flag = True

        while play_flag:
            # pygame.mixer.init()
            # pygame.mixer.music.load('music/Song1-Motor-Skills.mp3')
            # pygame.mixer.music.set_volume(0.2)
            # pygame.mixer.music.play(-1)
            print(f'\nWelcome to {self.name}\n')
            self.play_hand()  # This is where im calling my methods to fill and display hands
            self.player.display_hand()
            player_total = self.eval_hand(self.player)  # totaling hands
            print(f"{self.player.name}'s total: {player_total}\n") #  displaying totals

            self.dealer.display_hand()
            dealer_total = self.eval_hand(self.dealer)
            print(f"{self.dealer.name}'s total: {dealer_total}\n")
            
            if player_total == 21:  # checking for blackjack from deal
                print("Congrats! Black Jack! You Win!")
                break
            
            while player_total < 21:  # loop to determine if you can accept a hit
                hit_me = input('Do you want another card? Type: (y/n) ->').lower().strip()
                
                if hit_me == 'n':  # no hit
                    print("Bye!")
                    break

                elif hit_me == 'y': # if yes hit - deal player another card-display new hand-total new hand-print new total
                    os.system('clear')
                    self.deal_card(self.player)
                    self.player.display_hand()
                    player_total = self.eval_hand(self.player)
                    print(f"{self.player.name}'s total: {player_total}\n")
                    self.dealer.display_hand()
                    print(f"{self.dealer.name}'s total: {dealer_total}\n")
                    if player_total == 21:  # check for blackjack from hits
                        print("Congrats!\nBlack Jack!\nYou Win!\n")
                        break
                    
                    elif player_total > 21:  # check for bust
                        print(f"Sucks!\n{self.player.name} Busted!\n")
                        break

                else:
                    print("Please enter (y/n)")
            
            while dealer_total <= 16:  # loop to clean up dealer total
                self.deal_card(self.dealer)
                dealer_total = self.eval_hand(self.dealer)
                self.dealer.display_hand()
                print(f"{self.dealer.name}'s total: {dealer_total}\n")
                if dealer_total == 21:
                    print("Dealer has Black Jack, Sucks for the Table!")
            
            self.hand_compare(player_total, dealer_total)
            
            while True:
                play_again = input("Do you want to play another hand? (y/n) -> ").lower().strip()
                if play_again == 'n':
                    print("Thanks for Playing!!")
                    play_flag = False
                    break
                if play_again == 'y':
                    self.clear_hand()
                    player_total = 0
                    dealer_total = 0
                    break
                else:
                    print("Please enter (y/n)")
                    
# class Menu():
#     def __init__(self):

#     pass

new_game = Game()
new_game.play_game()