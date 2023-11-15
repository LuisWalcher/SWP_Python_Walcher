import random
import matplotlib.pyplot as plt
import  numpy as np

def getCards(anzZiehungen,statistic, oldstatistic):

    drawnCards = random.sample(range(0,52), anzZiehungen)
    #print(numbers(drawnCards))


    royalFlush(numbers(drawnCards), colors(drawnCards), statistic)
    if(len(statistic) > len(oldstatistic)):
        return statistic
    else:
        straightFlush(colors(drawnCards),numbers(drawnCards), statistic)
    if (len(statistic) > len(oldstatistic)):
        return statistic
    else:
        quat(numbers(drawnCards), statistic)
    if (len(statistic) > len(oldstatistic)):
        return statistic
    else:
        fullHouse(numbers(drawnCards), statistic)
    if (len(statistic) > len(oldstatistic)):
        return statistic
    else:
        flush(colors(drawnCards), statistic)
    if (len(statistic) > len(oldstatistic)):
        return statistic
    else:
        straight(numbers(drawnCards), statistic)
    if (len(statistic) > len(oldstatistic)):
        return statistic
    else:
        triplet(numbers(drawnCards), statistic)
    if (len(statistic) > len(oldstatistic)):
        return statistic
    else:
        doublePair(numbers(drawnCards), statistic)
    if (len(statistic) > len(oldstatistic)):
        return statistic
    else:
        pair(numbers(drawnCards),statistic)
    if (len(statistic) > len(oldstatistic)):
        return statistic

    else:
        highestcard(numbers(drawnCards),statistic)
        return statistic

def colors(cards):
    colors=[]
    for x in cards:
        colors.append(x // 13)  # herz: color; pik: color+13; karo: color+26; kreuz: color+39
    return colors

def numbers(cards):
    numbers = []
    for x in cards:
        numbers.append(x % 13)
    return numbers

def highestcard(cards,statistic):
    for x in cards:
        cards.remove(x)
        if(x in cards):
            return statistic
    statistic.append(1)
    return statistic

def pair(cards,statistic):
    pair = 0
    for x in cards:
        if (cards.count(x) == 2):
            pair += 1
    if(pair==2):
        return statistic.append(2)
    else:
        return statistic

def doublePair(cards,statistic):
    doublepair = 0
    for x in cards:
        if (cards.count(x) == 2):
            doublepair += 1
    if(doublepair==4):
        return statistic.append(3)
    else:
        return statistic



def triplet(cards,statistic):
    triplet = 0
    for x in cards:
        if (cards.count(x) == 3):
            triplet += 1
    if (triplet == 3):
        return statistic.append(4)
    else:
        return statistic

def straight(cards,statistic):
    pos = 0
    cards.sort()
    for x in cards[1:len(cards)]:
        if(x-cards[pos] == 1 or x-cards[0] == 12):
            pos += 1
        else: return statistic
    return statistic.append(5)

def flush(colors,statistic):
    for x in colors:
        if (colors.count(x) == 5):
            return statistic.append(6)
        else:
            return statistic


def fullHouse(cards,statistic):
    fullHouse = 0
    for x in cards:
        if (cards.count(x) == 3 or cards.count(x) == 2):
            fullHouse += 1
    if(fullHouse == 5):
        return statistic.append(7)
    else: return statistic

def quat(cards,statistic):
    quat = 0
    for x in cards:
        if (cards.count(x) == 4):
            quat += 1
    if (quat == 4):
        return statistic.append(8)
    else: return statistic

def straightFlush(colors,cards,statistic):
    pos = 0
    cards.sort()
    for x in cards[1:len(cards)]:
        if ((x - cards[pos] == 1 or x - cards[0] == 12) and colors.count(colors[0]) == 5):
            pos += 1
        else:
            return statistic
    return statistic.append(9)

def royalFlush(numbers,colors,statistic):
    numbers.sort()
    for x in colors:
        if (colors.count(x) == 5 and numbers == [8,9,10,11,12]):
            return statistic.append(10)
        else:
            return statistic

def main():
    symbols = ["Highest Card", "Pair", "Double Pair", "Triblet", "Straight", "Flush", "Full House", "Quad",
               "Straight Flush", "Royal Flush"]
    statistic = []
    oldstatistic = []
    stat = []
    ziehungen = 100000
    for x in range(ziehungen):
        getCards(5, statistic, oldstatistic)
        stat = statistic + stat
        statistic.clear()
        oldstatistic.clear()
    dict2 = {}
    print(stat)
    stat.sort()
    for x in stat:
        dict = {symbols[x - 1]: stat.count(x) / ziehungen * 100}
        dict2 = {**dict2, **dict}
    print(dict2)
    plt.pie(dict2.values(), labels=dict2.keys())
    plt.show()

if __name__ == '__main__':
    main()


