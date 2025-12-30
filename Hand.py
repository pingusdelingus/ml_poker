
class TableHand:
    def __init__(self,numPlayers=4):
        cols = numPlayers
        rows = 6 # position, pre-flop, flop, turn, river, cards info
        self.HandInfo = [[0 for _ in range(cols)] for _ in range(rows)]
        #first index is player, second is data, data is a linked list

   
class PlayerAction:
    def __init__(self, action, next=None):
        self.data = action
        #next is of type PlayerAction or None if player only makes 1 action that hand i.e folds
        self.next = next
        self.currentIndex = 0


    def getCurrentAction(self):
        curr = self
        # go through the linked list currentIndex number of times
        for index in range(self.currentIndex):
            curr = curr.next
        return curr.data


            






