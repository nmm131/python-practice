"""
Created on Mar 14, 2021

@author: N8
"""

from random import shuffle


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]