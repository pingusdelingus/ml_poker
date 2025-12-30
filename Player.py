class Player:
    def __init__(self,cards,actions,pos=None):
        self.cards = cards #list of Card objs
        self.actions = actions #list of Action objs
        self.position = pos #int where 0 is sb, 1 is bb, 2 is utd etc etc.
    def __str__(self):
        card_str = ', '.join(str(c) for c in self.cards)
        action_str = ', '.join(str(a) for a in self.actions)
        if not self.actions:
            action_str = "No Actions"
        if not self.cards:
            card_str = "No Cards"

        return f"player has : {card_str} and has : {action_str}"
    
    def accept_card(self, newCard):
        if len(self.cards) > 2:
            print("too many cards in hand, can't have more than 2")
            return
    
        self.cards.append(newCard)

    def kill_hand(self):
        self.cards = []


def make_action(self, BetToCall=None):
    """
    Ask the user for a poker action:
      - Check (only if no bet to call)
      - Call (if there is a bet)
      - Raise (must be at least 2x BetToCall if BetToCall is given)
      - Fold
      - Exit
    """
    while True:
        usrInput = input("(C)heck/(Call), (R)aise, (F)old, e(X)it: ").strip().lower()
        
        # --- CHECK / CALL ---
        if usrInput == "c":
            if BetToCall is not None and BetToCall > 0:
                return f"call {BetToCall}"
            else:
                return "check"

        # --- RAISE ---
        elif usrInput == "r":
            if BetToCall is None:
                BetToCall = 0  # safe default if no one has bet yet
            while True:
                try:
                    raiseAmount = float(input("How much would you like to raise to? "))
                    if raiseAmount < 2 * BetToCall:
                        print(f"Raise must be at least {2 * BetToCall}. Try again.")
                    else:
                        return f"raise {raiseAmount}"
                except ValueError:
                    print("Please enter a valid number for the raise amount.")

        # --- FOLD ---
        elif usrInput == "f":
            return "fold"

        # --- EXIT ---
        elif usrInput == "x":
            return "exit"

        # --- INVALID ---
        else:
            print("Invalid choice. Please enter C, R, F, or X.")


