import random

import  numpy as np

#Liste mit 52 Karten
#5 Zufallszahlen ziehen
#52 werte durch 4 dann hat man die farbe, weil dann hat man jeweils 0,1,2,3,4
#farbe egal

def getCards(anzZiehungen):
    cards = np.arange(1,53)
    print(cards)
    drawnCards = random.sample(range(1,53), anzZiehungen)
    print(drawnCards)
    colors = cards[0:len(cards)//4] # herz: color; pik: color+13; karo: color+26; kreuz: color+39
    whichCard(drawnCards, colors)

def whichCard(drawn, color):
    #key1: Herz, key2: Pik; key3: Karo, key4: Kreuz
    index=0
    finalColors = {}
    orderedCards = []
    while index != 4:
        for x in drawn:
            if x in (color+(len(color)*index)):
                orderedCards.append(["key"+str(index+1),x])
        for x in orderedCards:
            finalColors.setdefault(x[0], []).append(x[1])
            orderedCards.remove(x)
        index += 1
    print(finalColors)


if __name__ == '__main__':
    getCards(5)


