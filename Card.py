

#TODO: Recall that Ace's self.value is always 14, make sure you check if value is 14 in methods that check hands

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def getValue(self):
        assert isinstance(self.value ,int)
        return self.value

    def getSuit(self):
        return self.suit
    def __eq__(self, other):
        return (self.suit == other.suit and self.value == other.value)

    def __le__(self, other):
        if isinstance(other, Card):
            return self.value <= other.value
        else:
            return TypeError


    def __str__(self):
        v = ""
        if self.value <= 10:
            return f"{self.value} of {self.suit}"
        elif self.value == 11:
            v = "Jack"
        elif self.value == 12:
            v = "Queen"
        elif self.value == 13:
            v = "King"
        elif self.value == 14:
            v = "Ace"
        return f"{v} of {self.suit}"
                
            



    
