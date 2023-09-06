import random as rand

class pokerGameSim:
    
    def __init__(self, players):
        self.val = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
        self.deck = ["D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","DA",
                "C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","CA",
                "S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","SA",
                "H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","HA"]
        self.players = players - 1
        self.hand = []
        self.opHand = []
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
    preFlop():
    private method that deals out the preflop 
    cards to the players hand
    """
    def __preFlop(self):
        print("PRE-FLOP")
        #draws two cards to be the players hand
        self.hand = [self.__draw(), self.__draw()]
        #draws two cards to each other players hand
        self.opHand = [[self.__draw(), self.__draw()] for i in range(self.players)]

        print("Hand:", self.__printHand(self.hand))
        l = [self.__printHand(i) for i in self.opHand]
        print("opHand:", "".join(l))
        print("House:",self.__printHand(self.house))

    """
    flop():
    private method that deals out the flop 
    cards to the house
    """
    def __flop(self):
        print("FLOP")
        self.house = [self.__draw(), self.__draw(), self.__draw()]

        print("Hand:", self.__printHand(self.hand))
        l = [self.__printHand(i) for i in self.opHand]
        print("opHand:", "".join(l))
        print("House:", self.__printHand(self.house))

    """
    turn():
    private method that deals out the turn 
    card to the house
    """
    def __turn(self):
        print("TURN")
        self.house.append(self.__draw())

        print("Hand:", self.__printHand(self.hand))
        l = [self.__printHand(i) for i in self.opHand]
        print("opHand:", "".join(l))
        print("House:", self.__printHand(self.house))

    """
    showdown():
    final round where the cards are evaluated
    and a winner is declared
    """
    def __showdown(self):

        return

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
    
    def run(self):
        self.__preFlop()
        print()
        self.__flop()
        print()
        self.__turn()
        self.__showdown()

if __name__ == "__main__":
    #for i in range(10):
        game = pokerGameSim(4)
        game.run()