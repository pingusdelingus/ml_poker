from termcolor import colored

class Range:
    def __init__(self):
        rows, cols = 15,15
        self.rangeMat = [["-" for _ in range(cols)] for _ in range(rows)]
        self.initRange()
    

    def initRange(self):
        #create range object where only pocket pairs are in range
        for index in range(2,15):
            for jdex in range(2,15):
                if index >= jdex:
                    self.rangeMat[index][jdex] = RangeNode("o", index,jdex,False)
                elif index == jdex:
                    self.rangeMat[index][jdex] = RangeNode("s", index,jdex,True)
                else:
                    self.rangeMat[index][jdex] = RangeNode("o", index,jdex,False)


    def __str__(self):
        res = ""
        for i in range(len(self.rangeMat)):
            for j in range(len(self.rangeMat[i])):
                curr = str(self.rangeMat[i][j])
                res += curr
                res += " |"
            res += "\n"
        return res


class RangeNode:
    def __init__(self, onOrOff, val1,val2, inRange):
        if val2 > val1:
            val1 , val2 = val2, val1
        
        self.suit = onOrOff
        self.val1 = val1
        self.val2 = val2
        self.inRange = inRange
        self.change = [None, None, 2,3,4,5,6,7,8,9,10,"J", "Q", "K", "A"]

    def __str__(self):
        if self.inRange is True:
            return colored(f"{self.change[self.val1]}{self.change[self.val2]}{self.suit}\033[0m", "green")
        else:
            return f"{self.change[self.val1]}{self.change[self.val2]}{self.suit}"

r = Range()
print(r)


