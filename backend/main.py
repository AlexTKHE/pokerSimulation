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

def straight_flush(player, table_cards):
    #sort the cards in descending order
    cards = player.getCards()
    cards.extend(table_cards)
   
    cards.sort(key=lambda x: x.getValue(), reverse = True)
   
    #find the highest card of the straight while going through
    highest_card = -1
    straight_flush_count = 0
    prev_suit =  cards[0].getSuit()
    prev_value = cards[0].getValue() + 1
    for card in cards:
        if (prev_value-card.getValue()) == 1 and prev_suit == card.getSuit():
            if (straight_flush_count == 1):
                highest_card = prev_value
            straight_flush_count += 1
        else:
            straight_flush_count = 1
        if card == 2 and cards[0].getValue() == 14 and straight_flush_count==4 and prev_suit == cards[0].getSuit():
            return [player.getId(), highest_card]
        elif (straight_flush_count == 5):
            return [player.getId(), highest_card] 
        prev_value = card.getValue()
        prev_suit = card.getSuit()
    return False
    

def four_of_a_kind(player, table_cards):
    cards = player.getCards()
    cards.extend(table_cards)
    for card in cards:
        pair_found = 0
        for reference in cards:
            if reference.getValue() == card.getValue() and reference.getId() != card.getId() and pair_found == 2:
                return [player.getId(), card.getValue()]
            
            elif reference.getValue() == card.getValue() and reference.getId() != card.getId():
                pair_found += 1
    return False


def full_house(player, table_cards):
    trip_card = three_of_a_kind(player, table_cards)

    if trip_card != False:
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
    print (card_values)
    card_values.sort(reverse=True)

 
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

#method for checking if theres a pair with the same value already found
def not_find_pair(pairs, card):
    for pair in pairs:
        if pair == card.getValue():
            return False
    return True

#for finding if something has two pairs
def two_two_pairs(player, table_cards):
    cards = player.getCards()
    cards.extend(table_cards)
    compare_cards = cards
    pairs = []
    pair_found = 0
    for card in cards:
        for reference in compare_cards:
            if card.getValue() == reference.getValue() and card.getId() != reference.getId() and not_find_pair(pairs, card):
               # return (player.getId(), card.getValue())
               pairs.append(card.getValue())
               pair_found +=1
            
    if (pair_found >= 2):
        highest_pair = -1
        second_highest_pair = -1
        for pair in pairs:
            if pair>highest_pair:
                second_highest_pair = highest_pair
                highest_pair=pair
            elif pair > second_highest_pair:
                second_highest_pair = pair
        return [player.getId(), highest_pair, second_highest_pair]
    else:
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
            if card.getValue() == reference.getValue() and card.getId() != reference.getId():
               # return (player.getId(), card.getValue())
               is_pair = True
               if card.getValue() > highest_pair:
                   highest_pair = card.getValue()
            
    if (is_pair):
        return [player.getId(), highest_pair]
    else:
        return False


#will be passed through one card and hand id, this will be the highest card in the hand that is not used in others the kickcer
def high_card(player, table_cards):
    return_value = 0
    cards = player.getCards()
    cards.extend(table_cards)
    cards.sort(key=lambda x: x.getValue(), reverse = True)
    card_values = []
    for card in cards:
        card_values.append(card.getValue())
    print (card_values)
    cards = cards[:5]
    count = 1
    for card in cards:
        count = count * 100
        print(count)
        return_value += card.getValue()/count
    return [player.getId(), return_value]




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
table_cards = [cards[0],cards[13],cards[1], cards[17], cards[2]]

#pick two random cards for hands (make two hands)
players = [Hand(1,cards[3],cards[4]), Hand(2,cards[51],cards[34]), Hand(3, cards[14], cards[17])]
    
for player in players:
    print(high_card(player,table_cards))