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


#methods - the plan is to call them going down each other so I dont have to worry about the ones below like I know its not trips so i dont have to code that in

def full_house(player, table_cards):
    trip_card = three_of_a_kind(player, table_cards)

    if trip_card != False:
        print("working")
        cards = player.getCards()
        cards.extend(table_cards)
        other_cards = []
        for card in cards:
            if card.getValue() != trip_card[1]:
                other_cards.append(card)
        high_pair = two_pair_for_method(other_cards)
        if (high_pair != False):
            return [player.getId(), trip_card[1], high_pair[1]]
        else:
            return False
    else:
        return False

def flush(player, table_cards):
    cards = player.getCards()
    cards.extend(table_cards)

    suits = []
    for card in cards:
        suits.append(card.getSuit())
    
    flush = False
    count = [0, 0, 0, 0]
    for card in cards:
        if card.getSuit() == "Diamonds":
            count[0] += 1
            if (count[0] == 5):
                flush = "Diamonds"
                break
        elif card.getSuit() == "Hearts": 
            count[1] += 1
            if (count[1] == 5):
                flush = "Hearts"
                break
        elif card.getSuit() == "Clubs":
            count[2] += 1
            if (count[2] == 5):
                flush = "Clubs"
                break
        else:
            count[3] += 1
            if (count[3] == 5):
                flush = "Spades"
                break
    if flush != False:
        flush_cards = []
        for card in cards:
            if (card.getSuit() == flush):
                flush_cards.append(card.getValue())
        flush_cards.sort(reverse=True)
        return [player.getId(), flush_cards[0]]
    else:
        return False


def straight(player, table_cards):
    #sort the cards in descending order
    cards = player.getCards()
    cards.extend(table_cards)
    card_values = []
    for card in cards:
        card_values.append(card.getValue())
    card_values.sort(reverse=True)
    print (card_values)
    #find the highest card of the straight while going through
    highest_card = -1
    straight_count = 0
    prev_value = card_values[0] + 1
    for value in card_values:
        if (prev_value-value == 1):
            if (straight_count == 1):
                highest_card = prev_value
            straight_count += 1
        else:
            straight_count = 1
        if (value == 2 and card_values[0] == 14 and straight_count==4):
            return [player.getId(), highest_card]
        elif (straight_count == 5):
            return [player.getId(), highest_card] 
        prev_value = value
    return False


def three_of_a_kind(player, table_cards):
    cards = player.getCards()
    cards.extend(table_cards)
    for card in cards:
        pair_found = 0
        for reference in cards:
            if reference.getValue() == card.getValue() and reference.getId() != card.getId() and pair_found == 1:
                return [player.getId(), card.getValue()]
            
            elif reference.getValue() == card.getValue() and reference.getId() != card.getId():
                pair_found = 1
    return False

#for a two pair finding through a player
def two_pair(player, table_cards):
    cards = player.getCards()
    cards.extend(table_cards)
    compare_cards = cards
    is_pair = False
    highest_pair = -1
    for card in cards:
        for reference in compare_cards:
            if card.getValue() == reference.getValue() and card.getId() != reference.getId():
               # return (player.getId(), card.getValue())
               is_pair == True
               if card.getValue() > highest_pair:
                   highest_pair = card.getValue()
            
    if (is_pair):
        return [player.getId(), highest_pair]
    else:
        return False

#to determine two pair through a different method (for full house)
def two_pair_for_method(cards):
    is_pair = False
    highest_pair = -1
    
    for card in cards:
        for reference in cards:
            print(card.getId())
            print(reference.getId())
            if card.getValue() == reference.getValue() and card.getId() != reference.getId():
               # return (player.getId(), card.getValue())
               is_pair == True
               if card.getValue() > highest_pair:
                   highest_pair = card.getValue()
            
    if (is_pair):
        return [player.getId(), highest_pair]
    else:
        return False
    
#to determine the highest card in the hand of someone, can also enter
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
        
        card = Card(count, value, suit)
        count += 1
        cards.append(card)

#method to shuffle all of the cards before the game
#random.shuffle(cards)
    

#with shuffled 

#make table cards
table_cards = [cards[0],cards[13],cards[1], cards[5], cards[18]]

#pick two random cards for hands (make two hands)
#players = [Hand(1,cards[0],cards[1]), Hand(2,cards[51],cards[34]), Hand(3, cards[18], cards[15])]
players = [Hand(1,cards[26],cards[14])]

find_high_card = []
hand_high_card = []

for player in players:
    #finding high card
    hand_high_card = [player.getId(), high_card_in_hand(player, table_cards)]
    find_high_card.append(hand_high_card)

    #finding pairs
    pairs = two_pair(player, table_cards)
    #finding trips
    trips = three_of_a_kind(player, table_cards)
    print(trips)
    #finding straights
    straights = straight(player, table_cards)
    #finding flushes
    flushes = flush(player, table_cards)
    #finding full houses
    full_houses = full_house(player, table_cards)
    print(full_houses)

    

