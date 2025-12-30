from Deck import Deck
from Player import Player
from Card import Card

#create players
p1 = Player([],[])

p2 = Player([],[])

#create deck 
theDeck = Deck()


#deal to the players

p1.accept_card(theDeck.deal_one())
p1.accept_card(theDeck.deal_one())


p2.accept_card(theDeck.deal_one())
p2.accept_card(theDeck.deal_one())

print(f"Player 1 has : {p1}")


print(f"Player 2 has : {p2}")


def check_if_player_has_pocket_pair(Player):
    crds = Player.cards
    if len(crds) != 2:
        print("doesn't have 2 cards")
    elif len(crds) == 2:
        c1 = crds[0]
        c2 = crds[1]
        if c1.getValue() == c2.getValue():
            return True
        else:
            return False

#test check pocket pair method

tp = Player([Card("Hearts",10), Card("Diamonds",10)], [])

result_for_tp = check_if_player_has_pocket_pair(tp)
print(result_for_tp)
print('should be true ')


# runs simulation until pocket pair is found
def pocket_pair_check():
    havePocketPair = False
    count = 0
    while havePocketPair == False:
#        print(f"no pocket, p1 has {p1} and p2 has : {p2}")
        p1.kill_hand()
        p2.kill_hand()
        count += 1
        p1.accept_card(theDeck.deal_one_safe())
        p1.accept_card(theDeck.deal_one_safe())

        p2.accept_card(theDeck.deal_one_safe())
        p2.accept_card(theDeck.deal_one_safe())
        
        havePocketPair = check_if_player_has_pocket_pair(p1) or check_if_player_has_pocket_pair(p2)
        

    print(f"we found the pocket pair of {p1}, {p2} ")
    print(f"after {count} many hands")
    return count


num_hands_until_pp = []
max_attemps = 99999
for x in range(max_attemps):
    result = pocket_pair_check()
    num_hands_until_pp.append(result)


averageHands = sum(num_hands_until_pp) / len(num_hands_until_pp)
print(f"after {max_attemps} attempts, the average number of hands we had to wait for a pocket pair was")
print(f"{averageHands}")
print(f"we saw a min of {min(num_hands_until_pp)} and a max of {max(num_hands_until_pp)}")



s = 0 
for obs in num_hands_until_pp:
    s += (obs - averageHands) * (obs - averageHands)
stdDev = s / (len(num_hands_until_pp) - 1) 
import math
stdDev = math.sqrt(stdDev)
print(f"standard deviation is {stdDev}")
    
import statistics

otherstdDev = statistics.stdev(num_hands_until_pp)
print(f"other stddev is {otherstdDev}")


import matplotlib.pyplot as plt

plt.hist(num_hands_until_pp, bins=range(min(num_hands_until_pp), max(num_hands_until_pp) + 2), edgecolor="black", align="left")

# Add labels and title
plt.xlabel("Hands folded until got a Pocket Pair")
plt.ylabel("Frequency")
plt.title("Histogram of Integer Array")

# Show the plot
plt.show()
