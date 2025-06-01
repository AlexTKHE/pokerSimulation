#initiliaze all cards
import random
from player import Card
from player import Hand

suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
card_values_for_deck = list(range(2,15))

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
    isFlush = flush(player,table_cards)
    if isFlush == False:
        return False
    else:
        cards[:] = [card for card in cards if card.getSuit() == isFlush[2]]
    cards.sort(key=lambda x: x.getValue(), reverse = True)
    card_vals = []
    for card in cards:
        card_vals.append(card.getValue())
   
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
        elif prev_value == value:
            continue
        else:
            straight_flush_count = 1
        if card.getValue() == 2 and cards[0].getValue() == 14 and straight_flush_count==4 and prev_suit == cards[0].getSuit():
            return [player.getId(), highest_card + 140]
        elif (straight_flush_count == 5):
            return [player.getId(), highest_card + 140] 
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
                cards[:] = [four_of_a_kind_card for four_of_a_kind_card in cards if four_of_a_kind_card.getValue() != card.getValue()]
                return [player.getId(), card.getValue() + 120 + high_card_method(cards, 1)]
            
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
            if card.getValue() != trip_card[2]:
                other_cards.append(card)
        high_pair = two_pair_for_method(other_cards)
        if (high_pair != False):
            return [player.getId(), trip_card[2] + 100 +  high_pair[1]/100]
        else:
            return False
    else:
        return False

def flush(player, table_cards):
    cards = player.getCards()
    cards.extend(table_cards)
    scale = 100000000

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
        return [player.getId(), flush_cards[0] + 80, flush]
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
    #find the highest card of the straight while going through
    highest_card = -1
    straight_count = 0
    prev_value = card_values[0] + 1
    for value in card_values:
        if (prev_value-value == 1):
            if (straight_count == 1):
                highest_card = prev_value
            straight_count += 1
        elif prev_value == value:
            continue
        else:
            straight_count = 1
        if (value == 2 and card_values[0] == 14 and straight_count==4):
            return [player.getId(), 60 + highest_card]
        elif (straight_count == 5):
            return [player.getId(), 60 + highest_card] 
        prev_value = value
    return False


def three_of_a_kind(player, table_cards):
    cards = player.getCards()
    cards.extend(table_cards)
    trips = []
    
    for card in cards:
        skip = False
        for trip in trips:
            if trip[1] == card.getValue():
                skip = True
        if (skip):
            continue
        pair_found = 0
        for reference in cards:
            if reference.getValue() == card.getValue() and reference.getId() != card.getId() and pair_found == 1:
                trips.append([player.getId(), card.getValue()])
                break
            
            elif reference.getValue() == card.getValue() and reference.getId() != card.getId():
                pair_found = 1
    if len(trips) > 0:
        highest_value = -1
        for trip in trips:
            if trip[1] > highest_value:
                highest_value = trip[1]
        cards[:] = [card for card in cards if card.getValue() != highest_value]
        return_value = highest_value + 40
        return_value += high_card_method(cards, 2)
        return [player.getId(), return_value, highest_value]
    else:
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

        return_value = highest_pair + 20 + second_highest_pair/100
        cards[:] = [card for card in cards if card.getValue() != highest_pair and card.getValue != second_highest_pair]
        return_value += high_card_method(cards, 1)/100
        return [player.getId(), return_value]
    else:
        return False




#for a two pair finding through a player
def two_pair(player, table_cards):
    cards = player.getCards()
    cards.extend(table_cards)
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
        return_value = highest_pair
        cards[:] = [card for card in cards if card.getValue() != highest_pair]
        #three other cards than the pair
        return_value += high_card_method(cards, 3)
        return [player.getId(), return_value]
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
    cards = cards[:5]
    count = 1
    for card in cards:
        count = count * 100
        return_value += card.getValue()/count
    return [player.getId(), return_value]

def high_card_method(cards, amount_kicker):
    return_value = 0
    cards.sort(key=lambda x: x.getValue(), reverse = True)
    cards = cards[:amount_kicker]
    count = 1
    for card in cards:
        count = count * 100
        return_value += card.getValue()/count
    return return_value



count = 0
for suit in suits:
    for value in card_values_for_deck:
        #create an array with every card in it and give everyone a specific ID.
        
        card = Card(count, value, suit)
        count += 1
        cards.append(card)

#method to shuffle all of the cards before the game
#random.shuffle(cards)
    

#with shuffled 

#make table cards
#table_cards = [cards[0],cards[8],cards[2], cards[21], cards[16]]

#pick two random cards for hands (make two hands)
#players = [Hand(1,cards[7],cards[4]), Hand(2,cards[31],cards[30]), Hand(3, cards[26], cards[30])]

#tests
table_cards = [cards[0], cards[3], cards[5], cards[8], cards[10]]  # All diamonds: 2♦, 5♦, 7♦, 10♦, Q♦
players = [
    Hand(1, cards[2], cards[4]),    # 4♦, 6♦ → flush
    Hand(2, cards[20], cards[30]),  # random non-diamond cards
    Hand(3, cards[45], cards[46])   # clubs: 6♣, 7♣
]
# Winner: Player 1 (flush)

#check for winner with
scores = []

for player in players:
    cards = player.getCards()
    cards.extend(table_cards)
    card_value = []
    for card in cards:
        card_value.append(card.getValue())
    print(card_value)
    if straight_flush(player, table_cards) != False:
        scores.append(straight_flush(player, table_cards))
    elif four_of_a_kind(player, table_cards) != False:
        scores.append(four_of_a_kind(player, table_cards))
    elif full_house(player, table_cards) != False:
        scores.append(full_house(player,table_cards))
    elif flush(player, table_cards) != False:
        scores.append(flush(player, table_cards))
    elif straight(player, table_cards) != False:
        scores.append(straight(player,table_cards))
    elif three_of_a_kind(player, table_cards) != False:
        scores.append(three_of_a_kind(player, table_cards))
    elif two_two_pairs(player, table_cards) != False:
        scores.append(two_two_pairs(player, table_cards))
    elif two_pair(player,table_cards) != False:
        scores.append(two_pair(player,table_cards))
    else:
        scores.append(high_card(player, table_cards))

winners = []
winning_score = -1
print(scores)
for score in scores:
    if score[1] > winning_score:
        winners.clear()
        winners.append(score[0])
        winning_score = score[1]
    elif score[1] == winning_score:
        winners.append(score[0])

print(winners)