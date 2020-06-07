# -*- coding: utf-8 -*-
# By: N15vF 
#Version: 1.0


import time
from random import randrange

print("\n")

print("               ******************************")
print("               *     ADIVINAR  RESPUESTA    *")
print("               ******************************")

localtime = time.localtime()
result = time.strftime("%I:%M:%S %p", localtime)
print ("                  -----", result, "-----   ")
time.sleep(4.4)

num1 = int(randrange(2,50,2))
div = (num1) // 2

print("\n: Este juego consiste en adivinar la respuesta final que esta en tu mente...")
time.sleep (4.3)
print(": Procura recordar el numero que piensas...\n")
time.sleep (5.5)

print("\n--- ** OK COMENSAMOS ** ---\n")

print("     -----------Oooo---")
print("     -----------(----)---")
print("     ------------)--/----")
print("     ------------(_/-")
print("     ----oooO----")
print("     ----(---)----")
print("     -----\--(--")
print("     ------\_)-\n ")

time.sleep (4.5)

print("\n==> Piensa un * NUMERO * \n") 
time.sleep (5.5)

print("==> Ahora ese numero Multiplicalo por: 2 \n")
time.sleep (5.5)

print("==> Ahora Sumalo mas: ", num1 ) 
time.sleep (6.5)

print("\n==> Ahora Dividelo entre: 2 \n")
time.sleep (6.7)

print("==> Ahora Resta Todo menos el * NUMERO * que Pensaste...\n")
time.sleep (7.4)

print("   *** TU RESPUESTA ES... ***  \n")
time.sleep(3.8)

print("             ||")
print("             ||")
print("             ||")
print("             \/\n")
print("   =======>>",  div ,  "<<=======        ")
print("...........................\n")

print(".(....\............../....)") 
print(". \....\........... /...../ ")
print("...\....\........../...../ ")
print("....\..../´¯.I.¯`\..../ ")
print("..../... I....I..(¯¯¯`\ ")
print("...I.....I....I...¯¯.\...\ ")
print("...I.....I´¯.I´¯.I..\...) ")
print("...\.....` ¯..¯ ´.......' ")
print("....\_____________.?´ ")
print(".....lo o o o o o ol ")
print(".....lo o o o o o ol ")
print(".....lo o o o o o o|")

time.sleep (2.1)
print("\n ----- Good Bye -----")
time.sleep (1.1)
