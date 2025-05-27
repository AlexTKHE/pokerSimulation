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