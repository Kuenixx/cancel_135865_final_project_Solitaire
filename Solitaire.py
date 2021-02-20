# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from graphics import *
import os
import random
from random import shuffle
from button import Button
from Card import Card

# Screen title and size
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Solitaire"


class SolitaireGame:
    def __init__(self):
        self.interface()
        self.win = GraphWin(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.win.setBackground("lightgreen")
        Mposition = Rectangle(Point(65, 125), Point(130, 20))
        MX = Mposition.getP1()
        MY = Mposition.getP2()
        Mposition.setFill(color_rgb(0, 120, 0))
        Mposition.draw(self.win)
        pile, pile_1, pile_2, pile_3, pile_4, pile_5, pile_6, pile_7, deck = self.createPiles()

        stack_1 = []
        stack_2 = []
        stack_3 = []
        stack_4 = []
        cont = 0
        quitButton = Button(self.win, Point(960, 730), 60, 30, "Quit")
        quitButton.activate()
        replayButton = Button(self.win, Point(840, 730), 110, 30, "New Game")
        replayButton.activate()

        # pile[0].undrawCard()   eval("pile_"+str(i))
        i = 7

        aMin = 0
        aMax = 0
        cont_a = 0
        activeCards = []
        for i in range(52):
            if deck[i].is_face_up:
                activeCards.append(deck[i])
                cont_a += 1

        pack_choose = []
        cont_choose1 = -1
        cont_choose2 = -1
        cont_from_where = 0
        uni_count = 24
        p = self.win.getMouse()

        while not quitButton.clicked(p):
            # if p in
            # Reset variables for loop
            cont_choose1 = -1
            deck = []
            deck += pile + pile_1 + pile_2 + pile_3 + pile_4 + pile_5 + pile_6 + pile_7 + stack_1 + stack_2 + stack_3 + stack_4
            activeCards = []
            cont_a = 0
            Tposition = Rectangle(Point(0, 0), Point(1024, 10))
            Tposition.setFill(color_rgb(0, 120, 0))
            Tposition.draw(self.win)
            for i in range(52):

                if deck[i].is_face_up:
                    activeCards.append(deck[i])

                    cont_a += 1
            for i in range(cont_a):  # search first click
                CHECKX1 = p.getX() >= MX.getX()
                CHECKX2 = p.getX() <= MY.getX()
                CHECKY1 = p.getY() >= MX.getY()
                CHECKY2 = p.getY() <= MY.getY()
                CHECKX = CHECKX1 == CHECKX2
                CHECKY = CHECKY1 == CHECKY2
                if (CHECKX == True and CHECKY == True):
                    cont_false = -1
                    cont_true = 0

                    for u in range(uni_count):

                        if pile[u].is_face_up == True:
                            cont_true = u
                        elif pile[u].is_face_up == False:
                            cont_false += 1

                    try:
                        pile[cont_true].faceDown()
                        pile[cont_true + 1].drawCard(100, 200).draw(self.win)
                        activeCards[0] = pile[cont_true + 1]

                    except:
                        pile[0].drawCard(100, 200).draw(self.win)
                        activeCards[0] = pile[0]
                    uni_count = cont_false + 1
                    break

                if activeCards[i].clicked(p):
                    p2 = self.win.getMouse()
                    Tposition.undraw()
                    for x in range(cont_a):  # loop search second click

                        if activeCards[x].clicked(p2):
                            print(activeCards[x])
                            # activeCards[i].undrawCard()

                            if str(activeCards[i].checkPile()) == 'pile' and activeCards[x].canAttach(activeCards[i]):
                                pack_choose = eval(activeCards[i].checkPile())  # pack to undraw
                                # check face up
                                cont_false = -1
                                cont_true = 0
                                for u in range(uni_count):
                                    if pile[u].is_face_up == True:
                                        cont_true = u
                                    elif pile[u].is_face_up == False:
                                        cont_false += 1
                                pack_choose = eval(activeCards[x].checkPile())  # count pack to draw
                                cont_choose2 = -1
                                for t in pack_choose:
                                    cont_choose2 += 1
                                x2, y2 = eval(activeCards[x].checkPile())[cont_choose2].getXY()
                                eval(activeCards[i].checkPile())[cont_true].undrawCard()

                                eval(activeCards[x].checkPile()).append(pile[cont_true])
                                del pile[cont_true]

                                print(x2, y2)
                                print(cont_choose2)

                                # Draw new cards
                                y2 += 25

                                eval(str(activeCards[x].checkPile()))[cont_choose2 + 1].drawCard(x2, y2).draw(self.win)
                                print(pack_choose)  # pack to draw
                                try:
                                    pile[cont_true + 1].drawCard(100, 200).draw(self.win)
                                    activeCards[0] = pile[cont_true + 1]

                                except:
                                    pile[0].drawCard(100, 200).draw(self.win)
                                    activeCards[0] = pile[0]
                                uni_count = cont_false + 1

                                break

                            if str(activeCards[x].checkPile()) != 'pile' and activeCards[x].canAttach(
                                    activeCards[i]):  # check if it can attach
                                pack_choose = eval(activeCards[i].checkPile())  # pack to undraw
                                # check face up
                                cont_face = 0
                                for t in pack_choose:
                                    cont_choose1 += 1

                                    if eval(activeCards[i].checkPile())[cont_choose1].is_face_up:
                                        cont_face += 1
                                        if cont_face == 1:
                                            cont_choose2 = cont_choose1 - 1

                                    if eval(activeCards[i].checkPile())[cont_choose1] == activeCards[i]:
                                        cont_from_where = cont_choose1

                                # delete cards from pile
                                try:
                                    if eval(activeCards[i].checkPile())[cont_choose2].is_face_up:
                                        print("")
                                    else:

                                        x1, y = eval(activeCards[i].checkPile())[cont_choose2].getXY()
                                        eval(activeCards[i].checkPile())[cont_choose2].undrawCard()

                                        eval(activeCards[i].checkPile())[cont_choose2].drawCard(x1, y).draw(self.win)
                                except:
                                    print('tt')
                                cont_end = 0
                                for t in range(cont_from_where, cont_choose1 + 1, 1):
                                    eval(activeCards[i].checkPile())[t].undrawCard()

                                pack_choose = eval(activeCards[x].checkPile())  # pack to draw on
                                cont_choose3 = -1
                                for t in pack_choose:
                                    cont_choose3 += 1

                                contador = cont_from_where - 1  # append cards
                                for t in range(cont_from_where, cont_choose1 + 1, 1):
                                    contador += 1
                                    eval(activeCards[x].checkPile()).append(eval(activeCards[i].checkPile())[contador])
                                    del eval(activeCards[i].checkPile())[contador]

                                pack_choose = eval(activeCards[x].checkPile())  # count pack to draw
                                cont_choose2 = -1
                                for t in pack_choose:
                                    cont_choose2 += 1

                                print(cont_choose3, cont_choose2)
                                x2, y2 = eval(str(activeCards[x].checkPile()))[cont_choose3].getXY()

                                pic = cont_choose3
                                for t in range(cont_choose3, cont_choose2, 1):  # Draw new cards
                                    y2 += 25
                                    pic += 1
                                    eval(str(activeCards[x].checkPile()))[pic].drawCard(x2, y2).draw(self.win)
                                    print(pack_choose)  # pack to draw

                                break
                            break
                    break
            Tposition.undraw()
            if replayButton.clicked(p):
                self.win.close()
                SolitaireGame()
            p = self.win.getMouse()

    def interface(self):
        self.win1 = GraphWin("solitaire", SCREEN_WIDTH, SCREEN_HEIGHT)

        self.win1.setBackground("lightgreen")
        """
        self.text = Text(Point(SCREEN_WIDTH / 1.96, 250), "Solitaire")
        self.text.setTextColor("black")
        self.text.setSize(30)
        self.text.setFace("helvetica")
        self.text.draw(self.win1)
        """
        imagen = Image(Point(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), str("fotos/" + "red" + '.gif'))
        imagen.draw(self.win1)

        imagen = Image(Point(100, 800), str("fotos/" + "png" + '.gif'))
        imagen.draw(self.win1)

        imagen = Image(Point(509, 140), str("fotos/" + "soli" + '.gif'))
        imagen.draw(self.win1)

        Quit = Button(self.win1, Point(650, SCREEN_HEIGHT / 2), 150, 70, "Quit")

        Quit.activate()

        Start = Button(self.win1, Point(400, SCREEN_HEIGHT / 2), 150, 70, "Start Game")

        Start.activate()

        q = self.win1.getMouse()

        if Quit.clicked(q):
            self.win1.close()
            self.win.close()

        elif Start.clicked(q):
            self.win1.close()

    def createPiles(self):
        deck = Card.shuffle(52)

        pile = []
        pile_1 = []
        pile_2 = []
        pile_3 = []
        pile_4 = []
        pile_5 = []
        pile_6 = []
        pile_7 = []

        pile = deck[0:24]
        pile_1 = deck[24:25]
        pile_2 = deck[25:27]
        pile_3 = deck[27:30]
        pile_4 = deck[30:34]
        pile_5 = deck[34:39]
        pile_6 = deck[39:45]
        pile_7 = deck[45:52]

        stack_1, stack_2, stack_3, stack_4 = self.createStacks()

        c = 0
        d = 1
        posx = 100
        posy = 50

        for i in range(52):
            r = i
            if i < 24:

                if i < 23:
                    posy = 75
                    pile[i].is_face_up = False
                    pile[i].draw_init_Card(posx, posy, r).draw(self.win)
                else:
                    posy += 125
                    pile[i].is_face_up = True
                    pile[i].draw_init_Card(posx, posy, r).draw(self.win)
                    posy = 50

            if i == 24:
                i = 0
                posx = 200
                posy += 25
                pile_1[i].draw_init_Card(posx, posy, r).draw(self.win)
                posy = 50

            if 25 <= i <= 26:
                i -= 25
                posx = 300
                posy += 25
                if i < 1:
                    pile_2[i].is_face_up = False
                    pile_2[i].draw_init_Card(posx, posy, r).draw(self.win)
                else:
                    pile_2[i].is_face_up = True
                    pile_2[i].draw_init_Card(posx, posy, r).draw(self.win)
                    posy = 50

            if 27 <= i <= 29:
                i -= 27
                posx = 400
                posy += 25
                if i < 2:
                    pile_3[i].is_face_up = False
                    pile_3[i].draw_init_Card(posx, posy, r).draw(self.win)
                else:
                    pile_3[i].is_face_up = True
                    pile_3[i].draw_init_Card(posx, posy, r).draw(self.win)
                    posy = 50

            if 30 <= i <= 33:
                i -= 30
                posx = 500
                posy += 25
                if i < 3:
                    pile_4[i].is_face_up = False
                    pile_4[i].draw_init_Card(posx, posy, r).draw(self.win)
                else:
                    pile_4[i].is_face_up = True
                    pile_4[i].draw_init_Card(posx, posy, r).draw(self.win)
                    posy = 50

            if 34 <= i <= 38:
                i -= 34
                posx = 600
                posy += 25
                if i < 4:
                    pile_5[i].is_face_up = False
                    pile_5[i].draw_init_Card(posx, posy, r).draw(self.win)
                else:
                    pile_5[i].is_face_up = True
                    pile_5[i].draw_init_Card(posx, posy, r).draw(self.win)
                    posy = 50

            if 39 <= i <= 44:
                i -= 39
                posx = 700
                posy += 25
                if i < 5:
                    pile_6[i].is_face_up = False
                    pile_6[i].draw_init_Card(posx, posy, r).draw(self.win)
                else:
                    pile_6[i].is_face_up = True
                    pile_6[i].draw_init_Card(posx, posy, r).draw(self.win)
                    posy = 50

            if 45 <= i <= 51:
                i -= 45
                posx = 800
                posy += 25
                if i < 6:
                    pile_7[i].is_face_up = False
                    pile_7[i].draw_init_Card(posx, posy, r).draw(self.win)
                else:
                    pile_7[i].is_face_up = True
                    pile_7[i].draw_init_Card(posx, posy, r).draw(self.win)
                    posy = 50

        deck = []
        deck += pile + pile_1 + pile_2 + pile_3 + pile_4 + pile_5 + pile_6 + pile_7 + stack_1 + stack_2 + stack_3 + stack_4
        return pile, pile_1, pile_2, pile_3, pile_4, pile_5, pile_6, pile_7, deck

    def createStacks(self):

        hStack = []
        dStack = []
        tStack = []
        sStack = []

        img = Image(Point(950, 75), str("card_image/" + "GreyB" + '.gif'))
        img.draw(self.win)

        img = Image(Point(950, 200), str("card_image/" + "GreyB" + '.gif'))
        img.draw(self.win)

        img = Image(Point(950, 325), str("card_image/" + "GreyB" + '.gif'))
        img.draw(self.win)

        img = Image(Point(950, 450), str("card_image/" + "GreyB" + '.gif'))
        img.draw(self.win)

        return hStack, dStack, tStack, sStack


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

