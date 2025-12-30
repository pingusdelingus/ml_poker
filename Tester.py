from Deck import Deck


#need this import for Card to work
from Card import Card

d = Deck()
#print(d)

print(f"the deck has {len(d)} cards")


#a_spades = Card("Spades", 14)
#print(a_spades)




#print(d.deal_one())
#print(d.deal_one())
#print(d.deal_one())
#print(d.deal_one())

#print(d.d_len)


from Player import Player

p1 = Player([d.deal_one(), d.deal_one()], [])

vil = Player([d.deal_one(), d.deal_one()], [] )

print(p1)


from Game import TexasHoldEm

g = TexasHoldEm([p1, vil ], d)

g.start_new_hand()



from VillainPlayer import VillainPlayer


vp = VillainPlayer([d.deal_one()], [])

print(f"vp is : {vp}")

