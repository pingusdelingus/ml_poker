class Hand:
    def __init__(self,numPlayers=4):
        cols = numPlayers
        rows = 6 # position, pre-flop, flop, turn, river, cards info
        self.HandInfo = [[0 for _ in range(cols)] for _ in range(rows)]
        #first index is player, second is data

   
class Node:
    def __init__(self, prev=None, data, next=None):
        self.prev = prev
        self.data = data
        self.next = next
    def getPrev():
        return self.prev
    def getNext():
        return self.next

class StreetActionNode(Node):



class StreetAction:
    def __init__(self):
        self.StreetInfo = 


