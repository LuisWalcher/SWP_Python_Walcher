import json
import random
from pathlib import Path

import args as args
import matplotlib.pyplot as plt

import Stats

import requests

configpath = "C:\\Users\\luisw\\PycharmProjects\\SWP_Rubner\\SteinScherePapierWebserver\\config.json"


def schere(com):
    if com == "Spock" or com == "Stein":
        return False
    elif com == "Schere":
        return None
    else:
        return True

def spock(com):
    if com == "Papier" or com == "Echse":
        return False
    elif com == "Spock":
        return None
    else:
        return True

def stein(com):
    if com == "Spock" or com == "Papier":
        print("Hallo")
        return False
    elif com == "Stein":
        return None
    else:
        return True


def echse(com):
    if com == "Schere" or com == "Stein":
        return False
    elif com == "Echse":
        return None
    else:
        return True

def papier(com):
    if com == "Echse" or com == "Schere":
        return False
    elif com == "Papier":
        return None
    else:
        return True

def symbol_player(result):
    symbol_player = input("Wähle ein Symbol: ")

    if(symbol_player == "Schere"):
        return schere(symbol_com(result)),stats(symbol_player,result)
    elif(symbol_player == "Spock"):
        return spock(symbol_com(result)),stats(symbol_player,result)
    elif(symbol_player == "Stein"):
        return stein(symbol_com(result)),stats(symbol_player,result)
    elif(symbol_player == "Echse"):
        return echse(symbol_com(result)),stats(symbol_player,result)
    elif(symbol_player == "Papier"):
        return papier(symbol_com(result)),stats(symbol_player,result)
    else: print("Falsches Symbol!")


def symbol_com(result):
    list = ["Schere","Spock","Stein","Echse","Papier"]
    rand = random.randint(0,4)
    symbol_com = list[rand]
    stats(symbol_com,result)
    print(symbol_com)
    return symbol_com

def win(result,WinC,WinP):


    ergebnis = symbol_player(result)
    if ergebnis[0] == True:
        print("Gewonnen!")
        WinP += 1
    elif ergebnis[0] == False:
        print("Verloren!")
        WinC += 1
    else:
        print("Unentschieden!")


    revenche = input("Erneut Spielen?(Y/N): ")
    if(revenche == "Y"):
        win(result,WinC,WinP)
    elif(revenche == "N"):
        menu(ergebnis[1],WinC,WinP)
    else:
        print("Falsche Eingabe")
        menu(ergebnis[1],WinC,WinP)



def menu(result,WinC,WinP):
    menu_option = input("Wähle eine Option(Spiel/Statistik/Quit): ")
    if(menu_option == "Spiel"):
        win(result,WinC,WinP)
    elif(menu_option == "Statistik"):
        stats_show(result,WinC,WinP)
        menu(result,WinC,WinP)
    elif (menu_option == "Quit"):
        print("Ende!")
        write_json(result, WinC, WinP)
    else:
        print("Falsche Eingabe")
        menu(result, WinC, WinP)


def stats(symbol,result):
    result[symbol] += 1
    print(result)
    return result


def stats_show(result,WinC,WinP):
    plt.bar(result.keys(),result.values())
    plt.show()
    val = [WinC,WinP]
    key = ["Wins Computer","Wins Player"]
    plt.bar(key,val)
    plt.show()


def write_json(results, WinC, WinP):
    path = Path('game_data.json')
    print("--------------------")
    if path.exists():
        with open(path, 'r') as json_file:
            data = json.load(json_file)
            print("Results", data.get("Results"))
            print(results)
            results = {key: results.get(key,0)+data.get("Results").get(key,0) for key in set(results) | set(data.get("Results"))}
            print(results)
            data2 = {
                "WinC": WinC + data.get('WinC'),
                "WinP": WinP + data.get('WinP'),
                "Results": results
            }
    else:
        print("Test")
        data2 = {
            "WinC": WinC,
            "WinP": WinP,
            "Results": results
        }

    with open(path, 'w') as json_file:
        json.dump(data2, json_file, indent=4)

    with open(path, 'r') as json_file:
        data = json.load(json_file)
        send_data(data)



def send_data(data):
    with open(configpath, 'r') as json_file:
        config = json.load(json_file)
    res = requests.post(config.get("url"), json=data)

    print("-----------------",res.text)





if __name__ == '__main__':

    menu(Stats.get_struc()[0],Stats.get_struc()[1],Stats.get_struc()[2])

