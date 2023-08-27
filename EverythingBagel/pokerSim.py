import random as rand

class pokerGameSim:
    
    def __init__(self, players):
        self.val = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
        self.deck = ["D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","DA",
                "C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","CA",
                "S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","SA",
                "H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","HA"]
        self.players = players
        self.hand = []
        self.house = []

    """
    preFlop():
    private method that deals out the preflop 
    cards to the players hand
    """
    def preFlop(self):
        first = rand.randint(0,len(self.deck)-1)
        self.hand.append(self.deck.pop(first))

        second = rand.randint(0,len(self.deck)-1)
        self.hand.append(self.deck.pop(second))

        self.onTable = 2
        print("hand:", self.hand)
        self.evaluate()

    def evaluate(self):
        high = 0
        low = 0
        onTable = self.hand + self.house
        print("onTable:", onTable)
        if len(onTable) == 2:
            h, l = self.__highCard(onTable, high, low)
        return

    def __highCard(self, onTable, high, low):
        if high > 0:
             return
        list = sorted([x[1] for x in onTable], key=lambda x: self.val[x])[::-1]
        print("list:", list)
        high = list[0]
        low = list[1]
        return 0, 0

if __name__ == "__main__":
    #for i in range(10):
        game = pokerGameSim(4)
        game.preFlop()