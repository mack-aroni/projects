import random as rand

class pokerGameSim:
    
    def __init__(self, players):
        self.val = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
        self.deck = ["D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","DA",
                "C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","CA",
                "S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","SA",
                "H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","HA"]
        self.players = players
        self.hand = []
        self.house = []

    """
    draw():
    private method that draws a random card
    from the deck
    """
    def __draw(self):
        #pops random card off the deck to be "drawn"
        c = rand.randint(0,len(self.deck)-1)
        return self.deck.pop(c)

    """
    preFlop():
    private method that deals out the preflop 
    cards to the players hand
    """
    def preFlop(self):
        #draws two cards to be the players hand
        first = self.__draw()
        second = self.__draw()

        self.hand.append(first)
        self.hand.append(second)

        print("hand:", self.hand)
        self.evaluate()

    def evaluate(self):
        high = 0
        low = 0
        onTable = self.hand + self.house
        print("onTable:", onTable)
        if len(onTable) == 2:
            high, low = self.__doubles(onTable, high, low)
            high, low = self.__highCard(onTable, high, low)
        print(high, low)
        return

    def __doubles(self, onTable, high, low):
        if self.hand[0][1::] != self.hand[1][1::]:
             return high + 0, low + (13*6)
        v = self.val[self.hand[0][1::]]
        return high + ((v - 2) * 6) + 1, low + ((14 - v) * 6)

    def __highCard(self, onTable, high, low):
        if high > 0:
             return high, low + (52*51/2 - (high + low))
        list = sorted([x[1::] for x in onTable], key=lambda x: self.val[x])[::-1]
        print("list:", list)
        h = self.val[list[0]]
        l = self.val[list[1]]
        high = high + (l - 2) * 4 + 3
        low = low + (h - l - 1) * 4
        high = high + (h - 1) * 4 * (h - 2) * 4
        low = low + (14 - h) * 4 * (14 - h - 1) * 4
        return high, low

if __name__ == "__main__":
    #for i in range(10):
        game = pokerGameSim(4)
        game.preFlop()