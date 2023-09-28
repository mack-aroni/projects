import random as rand

class pokerGameSim:
    
    def __init__(self, players):
        self.rank = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
        self.deck = ["D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","DA",
                    "C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","CA",
                    "S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","SA",
                    "H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","HA"]
        self.players = players - 1
        self.hand = []
        self.pHands = []
        self.house = []

    """
    draw():
    private method that draws a random card
    from the deck
    """
    def __draw(self):
        c = rand.randint(0,len(self.deck)-1)
        return self.deck.pop(c)

    """
    evaluate(table):
    private method that finds the highest value
    card combination from the table
    """
    def __evaluate(self, table):
        #flush
        flush = []
        suits = {"H":[], "D":[], "C":[], "S":[]}
        #group cards by suit
        for card in table:
            suits[card[0]].append(card[1::])
        #find suit with >= 5 cards
        for suit, cards in suits.items():
            if len(cards) >= 5:
                flush = [5,[c for c in cards[:5]]]

        #straight
        straight = []
        #check indices 0-5 and 1-6
        for i in range(len(table) - 4):
            if self.rank[table[i][1::]] - 4 == self.rank[table[i + 4][1::]]:
                straight = [6,[c[1::] for c in table[i:i+5]]]
                break

        #royal flush, straight flush
        if len(flush) > 0 and len(straight) > 0 and flush[1] == straight[1]:
            if straight[1][0] == "A":
                return [1]
            else:
                return [2,straight[1][0]]

        #pair/s, trips, quad, fullhouse
        trips = []
        twop = []
        pair = []
        card_count = {}
        card_comb = {"Q":[],"T":[],"D":[]}
        #group cards by occurence of rank
        for c in table:
            if c[1::] in card_count:
                card_count[c[1::]] += 1
            else:
                card_count[c[1::]] = 1
        #group cards by occurences
        for card, count in card_count.items():
            if count == 4:
                card_comb["Q"].append(card)
            elif count == 3:
                card_comb["T"].append(card)
            elif count == 2:
                card_comb["D"].append(card)

        #check quad
        if card_comb["Q"]:
            return [3,card_comb["Q"][0]]
        
        #check full houses
        elif len(card_comb["T"]) > 1:
            return [4, [card_comb["T"][0],card_comb["T"][1]]]
        elif card_comb["T"] and card_comb["D"]:
            return [4,[card_comb["T"][0], card_comb["D"][0]]]
        
        elif card_comb["T"]:
            trips = [7, card_comb["T"][0]]

        elif len(card_comb["D"]) > 1:
            twop = [8, [card_comb["D"][0], card_comb["D"][1]]]

        elif card_comb["D"]:
            pair = [9, [card_comb["D"][0]]]
        #return highest combo
        if flush: return flush
        elif straight: return straight
        elif trips: return trips
        elif twop: return twop
        elif pair: return pair
        #highcard
        else: return [10,[table[0][1::]]]

    """
    findWinner(hands):
    determines a winner or a tie using a list of hands including
    their original indices and the card combination rank
    """
    def __findWinner(self, rank, hands):
        print(hands)
        #find highest straight/straight flush by comparing the sum of the ranks
        if rank == 2 or rank == 6:
            for i in range(len(hands)):
                hands[i][1] = (sum(self.rank[c] for c in hands[i][1]))
            highest = max(hands, key=lambda c: c[1])
            return highest[0]
        
        #find highest quad/trips/pairs/highcard
        elif rank in [3,7,9,10]:
            highest = max(hands, key=lambda c: self.rank[c[1][0]])
            return highest[0]
        
        #compare fullhouses/two pairs/flush by comparing each card by card
        else:
            high = []
            for i in range(len(hands[0][1])):
                val = max(self.rank[h[1][i]] for h in hands)
                high = [h for h in hands if self.rank[h[1][i]] == val]
                if len(high) == 1:
                    return high[0][0]
            return [h[0] for h in hands]

    """
    preFlop():
    private method that deals out the preflop 
    cards to the players hand
    """
    def __preFlop(self):
        print("PRE-FLOP")
        #draws two cards to be the players hand
        self.hand = [self.__draw(), self.__draw()]
        #draws two cards to each other players hand
        self.pHands = [[self.__draw(), self.__draw()] for i in range(self.players)]

        print("Hand:", self.__printHand(self.hand))
        l = [self.__printHand(i) for i in self.pHands]
        print("pHands:", "".join(l))
        print("House:",self.__printHand(self.house))

    """
    flop():
    private method that deals out the flop 
    cards to the house
    """
    def __flop(self):
        print("FLOP")
        #draws three cards to the house
        self.house = [self.__draw(), self.__draw(), self.__draw()]

        print("Hand:", self.__printHand(self.hand))
        l = [self.__printHand(i) for i in self.pHands]
        print("pHands:", "".join(l))
        print("House:", self.__printHand(self.house))

    """
    turn():
    private method that deals out the turn 
    card to the house
    """
    def __turn(self):
        print("TURN")
        #draws an additional card to the house
        self.house.append(self.__draw())
        print("Hand:", self.__printHand(self.hand))
        l = [self.__printHand(i) for i in self.pHands]
        print("pHands:", "".join(l))
        print("House:", self.__printHand(self.house))

    """
    showdown():
    final round where the cards are evaluated
    and a winner is declared
    """
    def __showdown(self):
        print("SHOWDOWN")
        #copy pHands and insert player hand at the beginning
        hands = [c for c in self.pHands]
        hands.insert(0, self.hand)
        val = []

        #foreach hand add the cards to the house cards and evaluate
        for h in hands:
            table = h + self.house
            #sort cards by decreasing rank
            table = sorted([x for x in table], key=lambda x: self.rank[x[1::]])[::-1]    
            print(self.__printHand(table))
            val.append(self.__evaluate(table))

        #find player/s with the highest ranking combinations
        print("val",val)
        mVal = min(c[0] for c in val)
        indices = [i for i, v in enumerate(val) if v[0] == mVal]
        print("indices",indices)

        #evaluate hands returning one winner
        if len(indices) > 1:
            winner = self.__findWinner(val[indices[0]][0], [[i,val[i][1]] for i in indices])
            if isinstance(winner, int):
                if winner == 0: print("You Win")
                else: print("Player "+str(indices[winner])+" wins")
            else:
                print("Player",winner,"wins")
        #else if only one player, return winner
        else:
            if indices[0] == 0: print("You Win")
            else: print("Player "+str(indices[0])+" wins")

    """
    printHand(hand):
    private method that formats and prints out a hand
    """
    def __printHand(self, hand):
        s = "["
        for i in range(len(hand)):
            s = s + hand[i]
            if i != len(hand)-1:
                s = s + ", "
        s = s + "]"
        return s
    
    """
    run()
    main runloop for pokerSim game
    """
    def run(self):
        self.__preFlop()
        print()
        self.__flop()
        print()
        self.__turn()
        print()
        self.__showdown()
        """
        print("\nTESTING")
        val = []
        h1 = ["SK","SQ","SJ","S9","S8","H2"]
        h2 = ["DK","DQ","DJ","D10","D3","S2"]
        h3 = ["SK","HK","H10","D8","S2","S3"]
        hands = [h1,h2,h3]
        print("hands",hands)
        for h in hands:
            val.append(self.__evaluate(h))
        print("val",val)
        mVal = min(c[0] for c in val)
        indices = [i for i, v in enumerate(val) if v[0] == mVal]
        winner = self.__findWinner(val[indices[0]][0], [[i,val[i][1]] for i in indices])
        print(winner)
        """

if __name__ == "__main__":
    #for i in range(10):
        game = pokerGameSim(4)
        game.run()