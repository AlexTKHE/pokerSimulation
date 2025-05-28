#initiliaze all cards
import random
from backend.player import Card
from backend.player import Hand

suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
card_values = list(range(2,15))
print(card_values)

#deck
cards = list()

#players
hands = list()
table_cards = list()

#methods
def high_card(hands, table_cards):
    high_index = -1
    high_card = 0
    for card in table_cards:
        if card > high_card:
            high_card = card
    for hand in hands:
        for card in hand:
            if card.getValue() > high_card:
                high_card = card.getValue()
                high_index = 




count = 0
for suit in suits:
    for value in card_values:
        #create an array with every card in it and give everyone a specific ID.
        count += 1
        card = Card(count, value, suit)
        cards.append(card)

#method to shuffle all of the cards before the game
random.shuffle(cards)
    

#with shuffled 