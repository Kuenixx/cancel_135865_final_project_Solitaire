
from graphics import *
import random
from random import shuffle

class Card:
    ranks = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'J', 'Q', 'K')
    suits = ('S', 'D', 'H', 'C')
    image = []

    image_name = ['RB']

    def __init__(self, ranksuit):

        self.rank = ranksuit[0]
        self.suit = ranksuit[1]
        self.face_up = f"card_image/{self.rank}{self.suit}.gif"
        self.is_face_up = True
        self.face_down = f"card_image/RB.gif"

    def clicked(self, p):
        r = self.searchCard()
        f = str(self.image[r])
        x, y = self.getXY()

        "Returns true if button active and p is inside"
        return (self.is_face_up and x - 50 <= p.getX() <= x + 50
                and y - 50 <= p.getY() <= y + 50)

    def getXY(self):
        r = self.searchCard()
        f = str(self.image[r])
        x = eval(f[12:15])
        y = eval(f[18:22])
        return x, y

    def checkPile(self):
        x, y = self.getXY()

        if x == 100:
            return 'pile'
        if x == 200:
            return 'pile_1'
        if x == 300:
            return 'pile_2'
        if x == 400:
            return 'pile_3'
        if x == 500:
            return 'pile_4'
        if x == 600:
            return 'pile_5'
        if x == 700:
            return 'pile_6'
        if x == 800:
            return 'pile_7'
        if x == 950:
            if y == '85':
                return 'Stack_1'
        if x == 200:
            if y == '210':
                return 'Stack_2'
        if x == 325:
            if y == '335':
                return 'Stack_3'
        if x == 450:
            if y == '460':
                return 'Stack_4'

    def draw_init_Card(self, posx, posy, i):

        name = str(self.rank + self.suit)
        self.image_name.append(name)
        if self.is_face_up == False:
            img = Image(Point(posx, posy), self.face_down)
        else:
            img = Image(Point(posx, posy), self.face_up)
        self.image.append(img)

        return self.image[i]

    def searchCard(self):
        r = 0
        while self.image_name[r] != str(self.rank + self.suit):
            r += 1
        return r - 1

    def drawCard(self, posx, posy):

        self.is_face_up = True
        r = self.searchCard()
        self.image[r] = Image(Point(posx, posy), self.face_up)
        return self.image[r]

    def faceDown(self):
        self.is_face_up = False
        r = self.searchCard()
        self.image[r].undraw()

    def undrawCard(self):
        r = self.searchCard()
        self.image[r].undraw()

    def getRank(self):

        return self.rank

    def getSuit(self):

        return self.suit

    # def faceUp(self):

    def shuffle(self):

        deck = [rank + suit for rank in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K'] for suit
                in "SCDH"]
        shuffle(deck)
        cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                 28,
                 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]
        for i in range(52):
            cards[i] = Card(deck[i])
            # name = str(Card(deck[i]))
            # self.image_name.append(Card(deck[i]))
        return cards

    def isBelow(self, card):

        if self.rank == 'J' and card.rank == "Q":
            return True
        elif self.rank == 'Q' and card.rank == 'K':
            return True
        elif self.rank == 'K':
            return False
        elif self.rank == '1' and card.rank == '2':
            return True
        elif self.rank == '2' and card.rank == '3':
            return True
        elif self.rank == '3' and card.rank == '4':
            return True
        elif self.rank == '4' and card.rank == '5':
            return True
        elif self.rank == '5' and card.rank == '6':
            return True
        elif self.rank == '6' and card.rank == '7':
            return True
        elif self.rank == '7' and card.rank == '8':
            return True
        elif self.rank == '8' and card.rank == '9':
            return True
        elif self.rank == '9' and card.rank == '0':
            return True
        elif self.rank == '0' and card.rank == 'J':
            return True
        else:
            return False

    def isNext(self, card):
        return self.rank == (eval(card.rank) + 1)

    def isOppositeSuit(self, card):

        if self.suit == "C" and card.suit == "H":
            return True
        if self.suit == "C" and card.suit == "D":

            return True
        elif self.suit == "S" and card.suit == "D":

            return True
        elif self.suit == "S" and card.suit == "H":

            return True
        elif self.suit == "H" and card.suit == "S":

            return True
        elif self.suit == "H" and card.suit == "C":

            return True
        elif self.suit == "D" and card.suit == "C":

            return True
        elif self.suit == "D" and card.suit == "S":

            return True
        else:

            return False

    def isSameSuit(self, card):

        if self.suit == "C" and card.suit == "C":
            return True
        if self.suit == "D" and card.suit == "D":

            return True
        elif self.suit == "S" and card.suit == "S":

            return True
        elif self.suit == "A" and card.suit == "H":

            return True
        else:
            return False

    def canAttach(self, card):

        if card.isBelow(self) and card.isOppositeSuit(self):
            print('true')
            return True
        elif self.isBelow(card) and self.isSameSuit(card):
            return True
        else:
            print("false")
            return False

    def isInOrder(self, card):
        if card.isNext(self) and not card.isOppositeSuit(self):
            return True
        else:
            return False

    def __str__(self):

        return str(self.rank) + str(self.suit)


