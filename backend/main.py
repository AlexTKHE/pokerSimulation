#initiliaze all cards
from card import Card

suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
card_values = list(range(2,15))
print(card_values)
cards = list()
count = 0

for suit in suits:
    for value in card_values:
        #create an array with every card in it and give everyone a specific ID.
        count += 1
        card = Card(count, value, suit)
        cards.append(card)

print(len(cards))
    