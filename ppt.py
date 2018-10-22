#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 10:47:18 2018

@author: carlos
"""
from random import randint

def printRock():
    print("""
                 *@@@#                    
               %,      &@@@@(             
               @        %     .@           
             &        /       *,          
             ,*       #        .,  .@      
         .*@       @         @     @*    
      *@      .%. &         .       @    
      @              /       .      .  @  
     @                #     /       &   @ 
    ./                     %       &    @ 
    &       %         *   %       &    #/ 
    @           ,&/.,@  ,.       #     @  
    /*                 @(      &      @   
     @                 (  #( &      ,#    
      @                         ,. @      
      ##                         #*      
       @%                      @,       
            @@*      .        ,@(         
                 @ @ @ @@ ./%#,          
        """)
def printPaper():
    print("""
                 // ,#                 
        ,@@(     /   /                 
       /    %   .,   /      #@,        
        /   (   *    (    .*   %       
        &    /  (    %    (   *        
/ **    ,    &  %    &   #    (        
    @    /   ,. &    /  %    &         
&    (   %    & &   *  %    @          
 %    *. &                 &           
  %    **#                &            
   #              ,%      /            
    /          /&    *&.  &      /@%#&*
     &   *%@*      &       @.*      .
     #            &                  &,
      *          %               ,@    
      &          #            ##       
       /         /          .*         
        #                  ,*          
         #.              .&   
        """)

def printScissors():
    print(""" 
                  .                    
               #.   .#         @,  *(  
               (     %        %      % 
               *     *       @      @  
               @      *     &      &   
               ./     @    /      ,    
                %     *   ..      &    
                 /     %  #      (     
           .#   .@ .*,,,@(       @     
      #.   &     @          (@   @     
      *    (     %              @&     
      #     &      @/            */    
      ,.     #     ,    **         ,   
       @#     #     ,  #,          &   
       # &.   #(@@#   *           ..   
        &                        ,(    
         #                      (.     
          %                   */       
            ,@             /%     
        """)
    
def tornMaquina():
    return randint(1,3) 
    
def winner(tp, tm, pp, pm):
    #1 = pedra
    #2 = paper
    #3 = tisores
    if(tp == 1):
        print("Jugador:")
        printRock()
        if(tm == 1):
            print("Maquinà:")
            printRock()
            print("Empat!\n")
            return pp, pm
        elif(tm == 2):
            print("Maquinà:")
            printPaper()
            print("Guanya Màquina!\n")
            return pp, pm+1
        elif(tm == 3):
            print("Maquinà:")
            printScissors()
            print("Guanya Jugador!\n")
            return pp+1,pm
    elif(tp == 2):
        print("Jugador:")
        printPaper()
        if(tm == 1):
            print("Maquinà:")
            printRock()
            print("Guanya Jugador!\n")
            return pp+1, pm
        elif(tm == 2):
            print("Maquinà:")
            printPaper()
            print("Empat!\n")
            return pp,pm
        elif(tm == 3):
            print("Maquinà:")
            printScissors()
            print("Guanya Màquina\n")
            return pp,pm+1
    elif (tp == 3):
        print("Jugador:")
        printScissors()
        if(tm == 1):
            print("Maquinà:")
            printRock()
            print("Guanya Màquina\n")
            return pp,pm+1
        elif(tm == 2):
            print("Maquinà:")
            printPaper()
            print("Guanya Jugador\n")
            return pp+1, pm
        elif(tm == 3):
            print("Maquinà:")
            printScissors()
            print("Empat!\n")
            return pp,pm
        
def saveGame(pp,pm):
    fileW = open("saves.txt", "w")
    fileW.write(str(pp) + "\n" + str(pm) + "\n")
    fileW.close()

def startGame(pPlayer, pMachine):
    opcioJoc = 0
    while(opcioJoc != 5):
        print("PUNTUACIO JUGADOR:",pPlayer, "\nPUNTUACIO MAQUINA:", pMachine, "\n-------------")
        opcioJoc = int(input("1. Jugar pedra - 2. Jugar paper - 3. Jugar tisores -4. Guardar partida - 5. Sortir\nQue vols fer?"))
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