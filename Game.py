
from Player import Player
class TexasHoldEm:
    def deal_flop(self ):
        if len(self.d.d) > 3:
            self.community_cards.append(self.d.deal_one() ) 
            self.community_cards.append(self.d.deal_one() ) 
            self.community_cards.append(self.d.deal_one() ) 
            print("flop dealt")
            return True
        else:
            print("deck doesn't have enough cards, check shuffle logic ")
            return False

    def show_cc(self):
        for c in self.community_cards:
            print(f"{str(c)} | ", end = "")

    def handle_action(self, street):
        if street == 'p':
            for index in range(len(self.pl)):
                player_action = self.pl[index]

        if street == "f":
            for index in range(len(self.player_list)):
                player = self.player_list[index]
                prevBet = self.current_action or None
                result = player.make_action(prevBet)


        if street == "t":
            pass
        if street == "r":
            pass

    def init(self):
        for player in self.pl:
            player.kill_hand()
        self.d.shuffle() 

    def game_loop(self):
        self.init()
        if len(self.d.d) != 52:
            print('deck not shuffled')
            return
        #all players in pl should have no cards and self.d should be shuffled with 52 cards
        for player in self.pl:
            player.accept_card(self.d.deal_one())
            player.accept_card(self.d.deal_one())
        self.handle_action('p')

        didFlopDealCorrectly = self.deal_flop()
        if not didFlopDealCorrectly:
            print('mega error in dealing flop')
            raise ValueError

        self.show_cc()
        self.handle_action('f')

        self.deal_turn()
        self.show_cc()
        self.handle_action('t')

        self.deal_river()
        self.show_cc()
        self.handle_action('r')

            
    def deal_river(self):
        if len(self.d.d) > 1:
            self.community_cards.append(self.d.deal_one() ) 
            return True
        else:
            return False


    def deal_turn(self):
        if len(self.d.d) > 1:
            self.community_cards.append(self.d.deal_one() ) 
            return True
        else:
            return False

    def start_new_hand(self):
        self.game_loop()





    def __init__(self, pl, d):
        self.pl = pl
        self.community_cards = []
        self.d = d
        self.init()

    def is_hand_trips(self,player_and_cc):
        for i in range(len(player_and_cc)):
            for j in range(len(player_and_cc)):
                for k in range(len(player_and_cc)):
                    if i != j and j!=k:
                        if player_and_cc[i].getValue() == player_and_cc[j].getValue() and player_and_cc[j].getValue() == player_and_cc[k].getValue():
                            return player_and_cc[i].getValue()
        return 0
   
    def find_highest_num_of_suit(self,suit, player_and_cc):
        highestVal = 0
        for c in player_and_cc:
            if c.getSuit() == suit:
                if c.getValue() > highestVal:
                    highestVal = c.getValue()
        return highestVal


    def is_quads(self,player_and_cc):
        nums = []
        for c in player_and_cc:
            nums.append(c.getValue())
        from collections import Counter

        freqs = Counter(nums)
        most_common_num, count = freqs.most_common(1)[0]

        if count == 4:
            return most_common_num
        else:
            return 0
            

    def is_hand_flush(self,player_and_cc):
        suits = []
        diamond_count = 0
        heart_count = 0
        spade_count = 0
        club_count = 0

        for c in player_and_cc:
            suits.append(c.getSuit())
            if c.getSuit() == "Hearts":
                heart_count +=1
            elif c.getSuit() == "Diamonds":
                diamond_count += 1
            elif c.getSuit() == "Spades":
                spade_count += 1
            elif c.getSuit() == "Clubs":
                club_count += 1
        if heart_count >=4:
            #return highest heart
            return ["Hearts" ,self.find_highest_num_of_suit("Hearts", player_and_cc)]

        elif diamond_count >=4 :
            return ["Diamonds", self.find_highest_num_of_suit("Diamonds", player_and_cc)]


        elif spade_count >=4:
            return ["Spades",self.find_highest_num_of_suit("Spades", player_and_cc)]
        elif club_count >=4:
            return ["Spades", self.find_highest_num_of_suit("Clubs", player_and_cc)] 
        else:
            return [None, None]


    def is_hand_straight(self,player_and_cc):
        onlyNumArray = []
        for c in player_and_cc:
            onlyNumArray.append(c.getValue())

        onlyNumArray.sort()
        onlyNumArray = set(onlyNumArray)

        if 14 in onlyNumArray:
            onlyNumArray.append(1)

        
        streak = 1
        high_card_in_straight = 0
        
        for index in range(1, len(onlyNumArray)):
            if streak >=5:
                return high_card_in_straight
            if onlyNumArray[index - 1] == onlyNumArray[index]:
                streak += 1
                high_card_in_straight = onlyNumArray[index]
            else:
                streak = 1
        return 0


    def is_hand_a_two_pair(self,player_and_cc,firstPairNum):
        for index in range(len(player_and_cc)):
            firstCard = player_and_cc[index]
            for jdex in range(len(player_and_cc)):
                secondCard = player_and_cc[jdex]
                if jdex != index and firstCard.getValue() == secondCard.getValue() and firstCard.getValue() != firstPairNum:
                    return firstCard.getValue()
        return 0

    def is_hand_a_pair(self,player_and_cc):
        for index in range(len(player_and_cc)):
            firstCard = player_and_cc[index]
            for jdex in range(len(player_and_cc)):
                secondCard = player_and_cc[jdex]
                if jdex != index and firstCard.getValue() == secondCard.getValue():
                    return firstCard.getValue()
        return 0

        return False
    def read_hands(self):
        pl = self.player_list
        cc = self.community_cards

        for player in pl:
            curr_player_hand = player.cards
            if len(curr_player_hand) != 2:
                print('player has more than 2 cards')
                return
#            curr_card1, curr_card2 = curr_player_hand[0], curr_player_hand[1]
            player_and_cc = cc + curr_player_hand # this should be alist of card objects

            # pair checking

            isHighCard = False
            isPair = False
            isTwoPair = False
            isTrips = False
            isStraight = False
            isFlush = False
            isFullHouse = False
            isQuads = False
            isStraightFlush = False
            isRoyalFlush = False

            #one pair check
            firstPairNum = self.is_hand_a_pair(player_and_cc)
            isPair = True if pairNum > 0 else False 

            #two pair check
            secondPairNum = self.is_hand_a_two_pair(player_and_cc,firstPairNum)
            isTwoPair = True if secondPairNum >0 and firstPairNum != secondPairNum else False

            #trips check
            tripsNum = self.is_hand_trips(player_and_cc)
            isTrips = False if tripsNum == 0 else True

            #straight check
            straight_card = is_hand_straight(player_and_cc)
            isStraight = True if straight_card >0 else False

            #flush check
            flush_card = is_hand_flush(player_and_cc) # [suit, highest_num]
            isFlush = False if flush_card[0] == None else True
            flush_highest_card = flush_card[1]

            if isTrips == True and isPair == True and firstPairNum != tripsNum:
                isTrips = False
                isPair = False
                isFullHouse = True

            quadsNum = self.is_quads(player_and_cc)
            isQuads = True if quadsNum >= 0 else False

            if isStraight and isFlush and (flush_highest_card == straight_card):
                isStraight = False
                isFlush = False
                isStraightFlush == True

            if isStraightFlush and (flush_highest_card == 14):
                isStraightFlush = False
                isRoyalFlush = True
 

