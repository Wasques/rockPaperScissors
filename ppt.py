#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 10:47:18 2018

@author: carlos
"""
from random import randint
from time import sleep

def tornMaquina():
    return randint(1,3) 
    
def winner(tp, tm, pp, pm):
#1 = pedra
#2 = paper
#3 = tisores
    if(tp == 1):
        if(tm == 1):
            print("-------------\nPedra vs Pedra\nEmpat!\n")
            return pp, pm
        elif(tm == 2):
            print("-------------\nPedra vs Paper\nGuanya Màquina!\n")
            return pp, pm+1
        elif(tm == 3):
            print("-------------\nPedra vs Tisores\nGuanya Jugador!\n")
            return pp+1,pm
    elif(tp == 2):
        if(tm == 1):
            print("-------------\nPaper vs Pedra\nGuanya Jugador!\n")
            return pp+1, pm
        elif(tm == 2):
            print("-------------\nPaper vs Paper\nEmpat!\n")
            return pp,pm
        elif(tm == 3):
            print("-------------\nPaper vs Tisores\nGuanya Màquina\n")
            return pp,pm+1
    elif (tp == 3):
        if(tm == 1):
            print("-------------\nTisores vs Pedra\nGuanya Màquina\n")
            return pp,pm+1
        elif(tm == 2):
            print("-------------\nTisores vs Paper\nGuanya Jugador\n")
            return pp+1, pm
        elif(tm == 3):
            print("-------------\nTisores vs Tisores\nEmpat!\n")
            return pp,pm
def saveGame(pp,pm):
    fileW = open("saves.txt", "w")
    fileW.write(str(pp) + "\n" + str(pm) + "\n")
    fileW.close()

def startGame(pPlayer, pMachine):
    opcioJoc = 0
    while(opcioJoc != 5):
        print("PUNTUACIO JUGADOR:",pPlayer, "\nPUNTUACIO MAQUINA:", pMachine, "\n-------------")
        opcioJoc = int(input("1. Jugar pedra\n2. Jugar paper\n3. Jugar tisores\n4. Guardar partida\n5. Sortir\nQue vols fer?"))
        print()
        if(opcioJoc > 0 and opcioJoc < 4):
            numMaquina = tornMaquina()
            pPlayer,pMachine = winner(opcioJoc,numMaquina, pPlayer, pMachine)
        elif(opcioJoc == 4):
            saveGame(pPlayer,pMachine)
        elif(opcioJoc == 5):
            print("Sortint...")
        elif(opcioJoc < 1 or opcioJoc > 5):
            print("Opció no vàlida")
    
def loadGame(file):    
    try:
        pP = 0
        pM = 0
        fileR= open(file, "r")
        pP = int(fileR.readline())
        pM = int(fileR.readline())
        fileR.close()
        startGame(pP, pM)
    except:
        print("No hi ha cap arxiu de guardat")
        menu()
    
def menu():
    print("Menu:\n1. Nou joc\n2. Carregar joc\n3. Sortir")
    menuOpcio = int(input("Escull que vols fer: "))
    print()
    while(menuOpcio > 3 or menuOpcio < 1):
        menuOpcio = int(input("Aixó no es possible, escull una opció vàlida: "))
    
    if(menuOpcio == 1):
        startGame(0,0)
    elif(menuOpcio == 2):
        file = "saves.txt"
        loadGame(file)
        
menu()