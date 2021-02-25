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

        quitButton = Button(self.win, Point(960, 730), 60, 30, "Quit")
        quitButton.activate()
       






        p = self.win.getMouse()

        while not quitButton.clicked(p):

            # Reset variables for loop
            deck = pile + pile_1 + pile_2 + pile_3 + pile_4 + pile_5 + pile_6 + pile_7 + stack_1 + stack_2 + stack_3 + stack_4
            activeCards = []
            cont_a = 0
            Tposition = Rectangle(Point(0, 0), Point(1024, 10))
            Tposition.setFill(color_rgb(0, 120, 0))
            Tposition.draw(self.win)
            for i in range(1,53):

                if deck[-i].is_face_up:
                    activeCards.append(deck[-i])

                    cont_a += 1
            for i in range(cont_a):  # search first click
                cont_from_where = 0
                CHECKX1 = p.getX() >= MX.getX()
                CHECKX2 = p.getX() <= MY.getX()
                CHECKY1 = p.getY() >= MX.getY()
                CHECKY2 = p.getY() <= MY.getY()
                CHECKX = CHECKX1 == CHECKX2
                CHECKY = CHECKY1 == CHECKY2
                if (CHECKX == True and CHECKY == True):
                    cont_false = 0
                    cont_true = 0
                    pile_loop = len(eval(pile[0].checkPile()))

                    for u in range(pile_loop):

                        if pile[u].is_face_up == True:
                            cont_true = u

                        elif pile[u].is_face_up == False:
                            cont_false += 1

                    pile[cont_true].faceDown()
                    try:
                        pile[cont_true + 1].drawCard(100, 200).draw(self.win)
                        activeCards[-1] = pile[cont_true + 1]

                    except:
                        pile[0].drawCard(100, 200).draw(self.win)
                        activeCards[-1] = pile[0]

                    break

                if activeCards[i].clicked(p):
                    p2 = self.win.getMouse()
                    Tposition.undraw()




                    for x in range(cont_a):  # loop search second click

                        if p2.getX() > 850:

                            rng = len(eval(activeCards[i].checkPile()))
                            yp = p2.getY()

                            o,xp,y2 = self.getStack(yp)

                            if str(activeCards[i]) == "1H" or str(activeCards[i]) == "1D" or str(activeCards[i]) == "1S" or str(activeCards[i]) == "1C":

                                if eval("stack_"+str(o))== []:

                                    for y in range(rng):
                                        if eval(activeCards[i].checkPile())[y] == activeCards[i]:
                                            cont_from_where = y
                                    if str(activeCards[i].checkPile()) != "pile":
                                        self.checkFaceup(eval(activeCards[i].checkPile()), cont_from_where)
                                    eval("stack_" + str(o)).extend(eval(activeCards[i].checkPile())[cont_from_where:cont_from_where + 1])
                                    eval(activeCards[i].checkPile())[cont_from_where].undrawCard()
                                    del eval(activeCards[i].checkPile())[cont_from_where]
                                    eval("stack_" + str(o))[0].drawCard(xp, y2).draw(self.win)

                            elif activeCards[x].clicked(p2) and activeCards[x].isInOrder(activeCards[i]):
                                for y in range(rng):
                                    if eval(activeCards[i].checkPile())[y] == activeCards[i]:
                                        cont_from_where = y
                                if str(activeCards[i].checkPile()) != "pile":
                                    self.checkFaceup(eval(activeCards[i].checkPile()), cont_from_where)
                                eval("stack_" + str(o)).extend(
                                    eval(activeCards[i].checkPile())[cont_from_where:cont_from_where + 1])
                                eval(activeCards[i].checkPile())[cont_from_where].undrawCard()
                                del eval(activeCards[i].checkPile())[cont_from_where]
                                rng = len(eval("stack_" + str(o)))

                                eval("stack_" + str(o))[rng-1].drawCard(xp, y2).draw(self.win)


                            else:
                                print('')
                            break

                        if str(activeCards[i]) == "KH" or str(activeCards[i]) == "KD" or str(activeCards[i]) == "KS" or str(activeCards[i]) == "KC":
                            xp = p2.getX()#check x of click

                            o = self.getEmptyPile(xp)#choose x of empty space clicked
                            if o == 0:
                                break
                            if eval("pile_"+str(o))  == []:
                                x2 = self.getPileX(o)
                                y2=50

                                if xp-50 <= x2 <= xp+50:


                                    rng = len(eval(activeCards[i].checkPile()))


                                    if str(activeCards[i].checkPile()) == "pile":
                                        for y in range(rng):
                                            if eval(activeCards[i].checkPile())[y] == activeCards[i]:
                                                cont_from_where = y

                                        eval("pile_"+str(o)).extend(eval(activeCards[i].checkPile())[cont_from_where:cont_from_where+1])
                                        eval(activeCards[i].checkPile())[cont_from_where].undrawCard()
                                        del eval(activeCards[i].checkPile())[cont_from_where]
                                        y2+=25
                                        eval("pile_" + str(o))[0].drawCard(x2, y2).draw(self.win)


                                        break
                                    if str(activeCards[i].checkPile()) != "pile":
                                        for y in range(rng):
                                            if eval(activeCards[i].checkPile())[y] == activeCards[i]:
                                                cont_from_where = y


                                        eval("pile_" + str(o)).extend(eval(activeCards[i].checkPile())[cont_from_where:rng])


                                        for t2 in range(cont_from_where, rng , 1):
                                            eval(activeCards[i].checkPile())[t2].undrawCard()
                                        del eval(activeCards[i].checkPile())[cont_from_where:rng]

                                        rng = len(eval("pile_" + str(o)))


                                        self.checkFaceup(eval(activeCards[i].checkPile()), cont_from_where)


                                        for y in range(rng):
                                            y2+=25
                                            eval("pile_" + str(o))[y].drawCard(x2,y2).draw(self.win)

                                        break
                                    break
                                break

                            break

                        if activeCards[x].clicked(p2):
                            print(activeCards[x])

                            #Check if chosen card is from pile
                            if str(activeCards[i].checkPile()) == 'pile' and activeCards[x].canAttach(activeCards[i]):
                                #pack_choose = eval(activeCards[i].checkPile())  # pack to undraw
                                # check face up
                                cont_false = -1
                                cont_true = 0
                                pile_loop = len(eval(pile[0].checkPile()))
                                for u in range(pile_loop):
                                    if pile[u].is_face_up == True:
                                        cont_true = u
                                    elif pile[u].is_face_up == False:
                                        cont_false += 1
                                pack_choose = eval(activeCards[x].checkPile())  # count pack to draw
                                cont_choose2 = -1
                                for t in pack_choose:
                                    cont_choose2 += 1
                                x2, y2 = eval(activeCards[x].checkPile())[cont_choose2].getXY()
                                eval(activeCards[x].checkPile()).append(pile[cont_true])
                                eval(activeCards[i].checkPile())[cont_true].faceDown()

                                #pile[cont_true].faceDown()
                                del pile[cont_true]


                                # Draw new cards
                                y2 += 25

                                eval(str(activeCards[x].checkPile()))[cont_choose2 + 1].drawCard(x2, y2).draw(self.win)
                                # pack to draw
                                try:
                                    pile[cont_true + 1].drawCard(100, 200).draw(self.win)
                                    activeCards[-1] = pile[cont_true + 1]

                                except:
                                    pile[0].drawCard(100, 200).draw(self.win)
                                    activeCards[-1] = pile[0]


                                break

                            #Check if chosen card is from s pile_# and requires move of many cards
                            if str(activeCards[x].checkPile()) != 'pile' and activeCards[x].canAttach(
                                    activeCards[i]):  # check if it can attach
                                pack_choose = eval(activeCards[i].checkPile())  # pack to undraw
                                # check face up
                                cont_face = 0
                                cont_choose1 = -1
                                for t in pack_choose:
                                    cont_choose1 += 1

                                    if eval(activeCards[i].checkPile())[cont_choose1].is_face_up:
                                        cont_face += 1
                                        if cont_face == 1:
                                            cont_choose2 = cont_choose1 - 1 #cont_choose_faceup

                                    if eval(activeCards[i].checkPile())[cont_choose1] == activeCards[i]:
                                        cont_from_where = cont_choose1

                                # delete cards from pile\
                                #check if card left is face up
                                self.checkFaceup(eval(activeCards[i].checkPile()),cont_from_where)

                                cont_end = 0
                                for t in range(cont_from_where, cont_choose1 + 1, 1):
                                    eval(activeCards[i].checkPile())[t].undrawCard()

                                pack_choose = eval(activeCards[x].checkPile())  # pack to draw on

                                cont_choose3 = 0
                                for t in pack_choose:
                                    cont_choose3 += 1

                                eval(activeCards[x].checkPile()).extend(eval(activeCards[i].checkPile())[cont_from_where:cont_choose1+1])

                                del eval(activeCards[i].checkPile())[cont_from_where:cont_choose1 + 1]

                                pack_choose = eval(activeCards[x].checkPile())  # count pack to draw

                                cont_choose2 = 0
                                for t in pack_choose:
                                    cont_choose2 += 1


                                x2, y2 = eval(str(activeCards[x].checkPile()))[cont_choose3-1].getXY()

                                pic = cont_choose3-1
                                for t in range(cont_choose3, cont_choose2, 1):  # Draw new cards
                                    y2 += 25
                                    pic += 1
                                    eval(str(activeCards[x].checkPile()))[pic].drawCard(x2, y2).draw(self.win)
                                    #print(pack_choose)  # pack to draw

                                break
                            break

                    break
            deck = pile + pile_1 + pile_2 + pile_3 + pile_4 + pile_5 + pile_6 + pile_7 + stack_1 + stack_2 + stack_3 + stack_4
            activeCards = []
            cont_a = 0
            for i in range(1, 53):

                if deck[-i].is_face_up:
                    activeCards.append(deck[-i])

                    cont_a += 1
            Tposition.undraw()
            p = self.win.getMouse()


    def getStack(self,y):
        i=''
        x=0
        y2=0
        if 25 <= y <= 125:
            i = '1'
            y2 = 75
            x = 950
        elif 150 <= y <= 250:
            i = '2'
            y2 = 200
            x = 950
        elif 275 <= y <= 375:
            i = '3'
            y2 = 325
            x = 950
        elif 400 <= y <= 500:
            i = '4'
            y2 = 450
            x = 950
        return i,x,y2

    def getEmptyPile(self,x):
        i=0
        if 150< x < 250:
            i = 1
        elif 250< x <350:
            i = 2
        elif 350 < x < 450:
            i = 3
        elif 450 < x < 550:
            i = 4
        elif 550< x <650:
            i = 5
        elif 650 < x < 750:
            i = 6
        elif 750 < x < 850:
            i = 7
        return i

    def getPileX(self, i):
        x=0
        if i == 1:
            x = 200
        elif i == 2:
            x = 300
        elif i == 3:
            x = 400
        elif i == 4:
            x = 500
        elif i == 5:
            x = 600
        elif i == 6:
            x = 700
        elif i == 7:
            x = 800
        return x

    def checkFaceup(self,pile,count):
        try:
            if pile[count - 1].is_face_up:
                print("")
            else:

                x1, y = pile[count - 1].getXY()
                pile[count - 1].undrawCard()

                pile[count - 1].drawCard(x1, y).draw(self.win)
        except:
            print('')

    def undrawFromPile(self, piles, cont_from_where, cont_choose1):
        for t in range(cont_from_where, cont_choose1 + 1, 1):
            piles[t].undrawCard()

    def interface(self):
        self.win1 = GraphWin("solitaire", SCREEN_WIDTH, SCREEN_HEIGHT)

        self.win1.setBackground("lightgreen")

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


        click = Point(0, 0)
        while not Start.clicked(click):
            click = self.win1.getMouse()
            if Quit.clicked(click):
                self.win1.close()
                self.win.close()

            elif Start.clicked(click):
                self.win1.close()



    # while
    def checkActive(self):
        activeCards = []

        for i in range(7):
            for x in eval("pile_" + str(i + 1))[i]:
                if eval("pile_" + str(i))[x].is_face_up:
                    activeCards.append(Card(eval("pile_" + str(i))[x]))
        return activeCards


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

        # self.checkPile(pile, pile_1, pile_2, pile_3, pile_4, pile_5, pile_6, pile_7)
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



