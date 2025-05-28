#initiliaze all cards
import random
from player import Card
from player import Hand

suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
card_values = list(range(2,15))

#deck
cards = list()

#players
hands = list()
table_cards = list()

def is_duplicate_or_unused(hand, table_cards):
    cards = []
    for card in hand:
        cards.append(card)
    for table_card in table_cards:
        cards.append(table_card)
    


#methods

def high_card_in_hand(player, table_cards):
    highest_value = -1
    cards = player.getCards()
    cards.extend(table_cards)
    for card in cards:
        if card.getValue() > highest_value:
            highest_value = card.getValue()

    return highest_value

#will be passed through one card and hand id, this will be the highest card in the hand that is not used in others the kickcer
def high_card(hands_highest_card):
    high_card = -1
    high_index = -1
    tie_index = [0]

    for hand in hands_highest_card:
        id = hand[0]
        value = hand[1]

        if (value > high_card):
            high_card = value
            tie_index.clear()
            high_index = id
        elif (value == high_card):
           
            tie_index.append(id)
    
    if(len(tie_index) > 0):
        tie_index.append(high_index)
        return tie_index
    else: 
        return high_index





count = 0
for suit in suits:
    for value in card_values:
        #create an array with every card in it and give everyone a specific ID.
        count += 1
        card = Card(count, value, suit)
        cards.append(card)

#method to shuffle all of the cards before the game
#random.shuffle(cards)
    

#with shuffled 

#make table cards
table_cards = [cards[1],cards[2],cards[3]]

#pick two random cards for hands (make two hands)
players = [Hand(1,cards[5],cards[6]), Hand(2,cards[7],cards[4]), Hand(3, cards[9], cards[15])]



find_high_card = []
hand_high_card = []

for player in players:
    hand_high_card = [player.getId(), high_card_in_hand(player, table_cards)]
    find_high_card.append(hand_high_card)

print(high_card(find_high_card))


