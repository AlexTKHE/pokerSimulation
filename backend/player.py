class Card():
    def __init__ (self, id, value, suit):
        self.id = id
        self.value = value
        self.suit = suit
        
    def getId(self):
        return self.id
    
    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit 

class Hand():
    def __init__ (self, id, card_1, card_2):
        self.id = id
        self.card_1 = card_1
        self.card_2 = card_2
        
    def getId(self):
        return self.id
    
    def getCard_1(self):
        return self.card_1

    def getCard_2(self):
        return self.card_2 
    
    def getCards(self):
        cards = list()
        cards.append(self.card_1)
        cards.append(self.card_2)
        return cards