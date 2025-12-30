# must be able to :
# 1. give an action
#
# 2. give an action with a value
#
class Input():
    def __init__(self, action, value=None):
        self.action = action
        self.value = value

    def getAction(self):
        return self.action if self.action != None else "action is null"

    def getValue(self):
        return self.value if self.value != None else "vavlue is null"
    
    #
class KeyboardInput(Input):

    def setAction(self):
        act = input("enter an action: (x-Check, c-Call, r-Raise, f-Fold, a-All in")
        while act.upper() not in ["X", "C", "R", "F", "A"]:
            print("pleaase enter a valid action")
            act = input("enter an action: (x-Check, c-Call, r-Raise, f-Fold, a-All in")
        
        if act == "R":
            try:
                raiseVale = int(input("enter raise value"))
            except Exception as e:
                while isinstance(raiseVale, int) != True:
                    try:
                        raiseVale = int(input("enter raise value"))
                    except Exception as e:

        self.value = raiseVale



