import random
import matplotlib.pyplot as plt

list = []
list2 = []
dict2 = {}


def rand():
    rand = 0
    index = 44
    content = 1
    for x in range(45):
        list.append(content)
        content = content+1
    for x in range(6):
        rand = random.randint(0,index)
        list[rand], list[index] = list[index], list[rand]
        index-=1


if __name__ == "__main__":
    for x in range(3):
        rand()
        print(list)
        for x in list[(len(list) - 6):len(list)]:
            list2.append(x)
        list.clear()

    print(list2)
    for x in list2:
        dict = {x: list2.count(x)}
        dict2 = {**dict2, **dict}
    print(dict2)
    plt.bar(dict2.keys(), dict2.values())
    plt.xlabel("X-Werte")
    plt.ylabel("Y-Werte")
    plt.show()