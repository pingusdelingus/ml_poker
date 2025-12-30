from Card import Card

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.d = []
        for j in range(len(suits)):
            currSuit = suits[j]
            for i in range(2,15,1):
                val = i
                new_card = Card(currSuit,int(val))
                self.d.append(new_card)
        from random import shuffle
        shuffle(self.d)
        self.d_len = len(self.d)

    def shuffle(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.d = []
        for j in range(len(suits)):
            currSuit = suits[j]
            for i in range(2,15,1):
                val = i
                new_card = Card(currSuit,int(val))
                self.d.append(new_card)
        from random import shuffle
        shuffle(self.d)
        self.d_len = len(self.d)
    
    def __len__(self):
        return len(self.d)
    def __str__(self):
        ans = []
        for card in self.d:
            ans.append(str(card) + ", ")

        return "".join(ans)

    def deal_one(self):
        if self.d_len  < 1:
            print("problem, deck has less than 1 card in it ")
            return None
        from random import randint
        choice = randint(0,self.d_len - 1)

        res = self.d.pop(choice)
        self.d_len = len(self.d)
        return res
        
    def deal_one_safe(self):
        if self.d_len  < 1:
            self.shuffle()

        from random import randint
        choice = randint(0,self.d_len - 1)

        res = self.d.pop(choice)
        self.d_len = len(self.d)
        return res


            

