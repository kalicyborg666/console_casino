# NAME GAME: CASINO 777
# Development time: 12 hours 40 minuts
# Data: 22/04/2021

# Modules
import random
import sys
import os
from colorama import init
from colorama import Fore, Back, Style

# VARIABLE BLOCK
game = True
game_m = True
game_r = True
game_d = True
game_ob = True
money = 0

# DEFINITION BLOCK:

# MAIN CYCLE
def main(money): # MAIN LOOP
	while game_m and money > 0 and money != 0:
		money = moneyRead(money)
		os.system("cls")
		print_main(money)
		try:
			inp_main = int(input(colourFore(7) + colourBack(0) + colourStyle(2) + "                                         ")) # INPUT MAIN FOR TRANSITION
			if inp_main == 1: # Transition to roulette()
				roulette(money, game_r)
			elif inp_main == 2: # Transition to dice()
				dice(money, game_d)
			elif inp_main == 3: # Transition to oneBandit()
				oneBandit(money, game_ob)
			elif inp_main== 0: # EXIT MAIN LOOP
				game = False
				os.system("cls")
				return game
		except ValueError:
			moneyWrite(money)
			print(colourFore(3) + colourBack(0) + colourStyle(2) + "Incorrect value")

# SUBDEFINITION MAIN CYCLE
def roulette(money, game_r): # MAIN CYCLE ROULETTE
	while game_r and money > 0:
		os.system("cls")
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Select the type of bet:" + "\n" +
			"Your balance = " + str(money) + "$" + "\n" +
			colourFore(5) + colourBack(0) + colourStyle(2) + "1 - Direct bet | 35 to 1" + "\n" +
			colourFore(4) + colourBack(0) + colourStyle(2) + "2 - Row | 2 to 1" + "\n" +
			colourFore(3) + colourBack(0) + colourStyle(1) + "3 - Red / Black | 1 to 1" + "\n" +
			colourFore(2) + colourBack(0) + colourStyle(2) + "4 - Even / Odd | 1 to 1" + "\n" +
			colourFore(1) + colourBack(0) + colourStyle(0) + "0 - Back to the menu" + "\n")
		if_roulette = int(input(colourFore(7) + colourBack(0) + colourStyle(2))) # INPUT SWITCH ROULETTE
		if if_roulette == 1: # 1 GAME ROULETTE
			money = subroulette1(money)
			moneyWrite(money) # RECORD MONEY 1 GAME ROULETTE
		elif if_roulette == 2: # 2 GAME ROULETTE
			money = subroulette2(money)
			moneyWrite(money) # RECORD MONEY 2 GAME ROULETTE
		elif if_roulette == 3: # 3 GAME ROULETTE
			money = subroulette3(money)
			moneyWrite(money) # RECORD MONEY 3 GAME ROULETTE
		elif if_roulette == 4: # 4 GAME ROULETTE
			money = subroulette4(money)
			moneyWrite(money) # RECORD MONEY 4 GAME ROULETTE
		elif if_roulette == 0: # EXIT GAME ROULETTE
			game_r = False
			return money
def dice(money, game_d):# MAIN CYCLE DICE
	while game_d and money > 0:
		os.system("cls")
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Select the type of bet:" + "\n" +
			colourFore(3) + colourBack(0) + colourStyle(2) + "Your balance = " + str(money) + "$" + "\n" +
			colourFore(4) + colourBack(0) + colourStyle(0) + "1 - Against the dealer (</>/=) | 2 to 1 <> | 5 to 1 = " + "\n" +
			colourFore(2) + colourBack(0) + colourStyle(0) + "2 - Even / Odd | 1 to 1" + "\n" +
			colourFore(3) + colourBack(0) + colourStyle(0) + "3 - Direct bet | 6 to 1" + "\n" +
			colourFore(1) + colourBack(0) + colourStyle(0) + "0 - Back to the menu" + "\n")
		if_dice = int(input(colourFore(7) + colourBack(0) + colourStyle(2))) # INPUT SWITCH DICE
		if if_dice == 1: # 1 GAME DICE
			money = subdice1(money)
			moneyWrite(money) # RECORD MONEY 1 GAME DICE
		elif if_dice == 2: # 2 GAME DICE
			money = subdice2(money)
			moneyWrite(money) # RECORD MONEY 2 GAME DICE
		elif if_dice == 3: # 3 GAME DICE
			money = subdice3(money)
			moneyWrite(money) # RECORD MONEY 3 GAME DICE
		elif if_dice == 0: # EXIT GAME DICE
			game_d = False
			return money
# def oneBandit(money):
	#print("Select the type of bet:" + "\n"
		#"1 - " + "\n"
		#"2 - " + "\n"
		#"3 - " + "\n"
		#"4 - " + "\n")  # MAIN CYCLE ONE-ARMED BANDIT in development(лень)

# DEFINITION MONEY
def assignMoney():
	try:
		file = open(r"C:\Users" + """\\""" + nameuser + "\Documents\money.txt", "r")
		read = file.read()
		file.close()
		if read.isdigit():
			read = int(read)
			if read > 0:
				money = int(read)
			elif read <= 0:
				file = open(r"C:\Users" + """\\""" + nameuser + "\Documents\money.txt", "w")
				money = str(1000)
				file.write(money)
				file.close()
				money = int(money)
		else:
			file = open(r"C:\Users" + """\\""" + nameuser + "\Documents\money.txt", "w")
			money = str(1000)
			file.write(money)
			file.close()
			money = int(money)
	except FileNotFoundError:
		file = open(r"C:\Users" + """\\""" + nameuser + "\Documents\money.txt", "w")
		money = str(1000)
		file.write(money)
		file.close()
		money = int(money)
	return money
def moneyWrite(money):
	file = open(r"C:\Users" + """\\""" + nameuser + "\Documents\money.txt", "w")
	money = str(money)
	file.write(money)
	file.close() # WRITE MONEY # WRITE MONEY
def moneyRead(money):
	file = open(r"C:\Users" + """\\""" + nameuser + "\Documents\money.txt", "r")
	read = file.read()
	money = int(read)
	file.close()
	return money # READ MONEY

# SUBDEFINITION ROULETTE
def subrouletteanimation(num):
	colourStyle(0)
	i2 = 35
	for i in range(37):
		c1 = random.randint(1,6)
		c2 = random.randint(1,6)
		print(colourFore(0) + colourBack(7) + colourStyle(0) + str(i) + colourFore(c1) + colourBack(c2) + colourStyle(0) + " | " + "__" * i + colourBack(0))
	r = 36 - num
	for i in range(r):
		c1 = random.randint(1,6)
		c2 = random.randint(1,6)
		print(colourFore(0) + colourBack(7) + colourStyle(0) + str(i2) + colourFore(c1) + colourBack(c2) + colourStyle(0) + " | " + "__" * i2 + colourBack(0))
		i2 -= 1
def subroulette1(money):
	os.system("cls")
	print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
	num1_0 = int(input(colourFore(7) + colourBack(0) + colourStyle(2) + "Enter a number from 0 to 36: "))
	num1_1 = int(input(colourFore(7) + colourBack(0) + colourStyle(2) + "Enter bet amount: "))
	money -= num1_1
	num_random1 = random.randint(0, 36)
	print(colourFore(3) + colourBack(0) + colourStyle(2) + "Bets are placed, spin the wheel! ...")
	subrouletteanimation(num_random1)
	if num1_0 == num_random1:
		num1_1 *= 36
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Winning a bet: ", str(num1_1))
		money += num1_1
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money
	else:
		num1_1 *= 0
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "You lose.." + "\n" +
		colourFore(3) + colourBack(0) + colourStyle(2) + "Correct number: " + str(num_random1) + "\n" +
		colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money # Subcycle 1 roulette(money)
def subroulette2(money):
	os.system("cls")
	print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
	print(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter a number from 1 to 3" + "\n" +
	colourFore(3) + colourBack(0) + colourStyle(2) + "(1| 1-12, 2| 12-24, 3| 24-36):" + "\n")
	num2_0 = int(input(colourFore(7) + colourBack(0) + colourStyle(2)))
	num2_1 = int(input(colourFore(7) + colourBack(0) + colourStyle(2) + "Enter bet amount: "))
	money -= num2_1
	num_random2 = random.randint(1, 3)
	print(colourFore(3) + colourBack(0) + colourStyle(2) + "Bets are placed, spin the wheel! ...")
	subrouletteanimation(36)
	if num2_0 == num_random2:
		num2_1 *= 3
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Winning a bet: ", str(num2_1))
		money += num2_1
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money
	if num2_0 == num_random2:
		num2_1 *= 3
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Winning a bet: ", str(num2_1))
		money += num2_1
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money
	if num2_0 == num_random2:
		num2_1 *= 3
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Winning a bet: ", str(num2_1))
		money += num2_1
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money	
	else:
		num2_1 *= 0
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "You lose.." + "\n" +
		colourFore(3) + colourBack(0) + colourStyle(2) + "Correct number: " + str(num_random2) + "  (1| 1-12, 2| 12-24, 3| 24-36)" + "\n" +
		colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money # Subcycle 2 roulette(money)
def subroulette3(money):
	os.system("cls")
	print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
	num3_0 = input(colourFore(7) + colourBack(0) + colourStyle(2) + "Enter 'Red' or 'Black': ")
	num3_1 = int(input(colourFore(7) + colourBack(0) + colourStyle(2) + "Enter bet amount: "))
	money -= num3_1
	num_random3 = random.randint(0, 1)
	print(colourFore(3) + colourBack(0) + colourStyle(2) + "Bets are placed, spin the wheel! ...")
	subrouletteanimation(36)
	if num3_0 == "Red" and 0 == num_random3:
		num3_1 *= 2
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Winning a bet: ", str(num3_1))
		money += num3_1
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money
	elif num3_0 == "Black" and 1 == num_random3:
		num3_1 *= 2
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Winning a bet: ", str(num3_1))
		money += num3_1
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money
	else:
		num3_1 *= 0
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "You lose.." + "\n" +
		colourFore(3) + colourBack(0) + colourStyle(2) + "Correct color: " + str(num_random3) + colourFore(3) + colourBack(0) + colourStyle(0) + "  0-Red, 1-Black" + "\n" +
		colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money
def subroulette4(money):
	os.system("cls")
	print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
	num4_0 = input(colourFore(7) + colourBack(0) + colourStyle(2) + "Enter 'Even' or 'Odd': ")
	num4_1 = int(input(colourFore(7) + colourBack(0) + colourStyle(2) + "Enter bet amount: "))
	money -= num4_1
	num_random4 = random.randint(0, 36)
	print(colourFore(3) + colourBack(0) + colourStyle(2) + "Bets are placed, spin the wheel! ...")
	subrouletteanimation(36)
	if num4_0 == "Even" and num_random4 % 2 == 0:
		num4_1 *= 2
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Winning a bet: ", str(num4_1))
		money += num4_1
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money
	elif num4_0 == "Odd" and num_random4 % 2 != 0:
		num4_1 *= 2
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Winning a bet: ", str(num4_1))
		money += num4_1
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money
	else:
		num4_1 *= 0
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "You lose.." + "\n" +
		colourFore(3) + colourBack(0) + colourStyle(2) + "Correct number: " + str(num_random4) + "\n" +
		colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money

# SUBDEFINITION DICE
def subdiceanimation(num):
	print(colourFore(0) + colourBack(1) + colourStyle(0)) 
	print( "-------------" + "\n" +
		  "|" + colourBack(7) + "           " + colourBack(1) + "|" + "\n" + colourBack(0) +
		  colourBack(1) +"|" + colourBack(7) + "           " + colourBack(1) + "|" + "\n" + colourBack(0) +
		  colourBack(1) + "|" + colourBack(7) + "     " + colourFore(0) + colourBack(3) + colourStyle(0) + str(num) + colourFore(0) + colourBack(7) + colourStyle(0) + "     " + colourBack(1) + "|" + "\n" + colourBack(0) +
		  colourBack(1) + "|" + colourBack(7) + "           " + colourBack(1) + "|" + "\n" + colourBack(0) +
		  colourBack(1) + "|" + colourBack(7) + "           " + colourBack(1) + "|" + "\n" + colourBack(0) +
		  colourBack(1) + "-------------" + "\n" + colourBack(0)) 
def subdice1(money):
	os.system("cls")
	print("Balance: ", str(money) + "$" + "\n")
	num1_0 = input(colourFore(7) + colourBack(0) + colourStyle(2) + "Please select: >, <, =: ")
	num1_1 = int(input(colourFore(7) + colourBack(0) + colourStyle(2) + "Enter bet amount: "))
	money -= num1_1
	num_random1 = random.randint(1, 6)
	num_random1_dealer = random.randint(1, 6)
	print(colourFore(3) + colourBack(0) + colourStyle(2) + "Bets are placed, spin the wheel! ...")
	print(colourFore(3) + colourBack(0) + colourStyle(2) + 'You dice: ' + '\n')
	subdiceanimation(num_random1)
	print(colourFore(3) + colourBack(0) + colourStyle(2) + 'Dealer dice: ' + '\n')
	subdiceanimation(num_random1_dealer)
	if num1_0 == ">" and num_random1 > num_random1_dealer:
		num1_1 *= 3
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Winning a bet: ", str(num1_1))
		money += num1_1
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money
	elif num1_0 == "<" and num_random1 < num_random1_dealer:
		num1_1 *= 3
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Winning a bet: ", str(num1_1))
		money += num1_1
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money
	elif num1_0 == "=" and num_random1 == num_random1_dealer:
		num1_1 *= 5
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Winning a bet: ", str(num1_1))
		money += num1_1
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money
	else:
		num1_1 *= 0
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "You lose.." + "\n" +
		colourFore(3) + colourBack(0) + colourStyle(2) + "Selected operation: " + colourFore(1) + colourBack(0) + colourStyle(0) + str(num1_0) + "\n" +
		colourFore(3) + colourBack(0) + colourStyle(2) + "Your number: " + str(num_random1) + "\n" +
		colourFore(3) + colourBack(0) + colourStyle(2) + "Dealer number: " + str(num_random1_dealer) + "\n" +
		colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money # Subcycle 1 dice(money)
def subdice2(money):
	os.system("cls")
	print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
	num2_0 = input(colourFore(7) + colourBack(0) + colourStyle(2) + "Enter 'Even' or 'Odd': ")
	num2_1 = int(input(colourFore(7) + colourBack(0) + colourStyle(2) + "Enter bet amount: "))
	money -= num2_1
	num_random2 = random.randint(1, 6)
	print(colourFore(3) + colourBack(0) + colourStyle(2) + "Bets are placed, spin the wheel! ...")
	print(colourFore(3) + colourBack(0) + colourStyle(2) + 'Number on dice: ' + '\n')
	subdiceanimation(num_random2)
	if num2_0 == "Even" and num_random2 % 2 == 0:
		num2_1 *= 2
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Winning a bet: ", str(num2_1))
		money += num2_1
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money
	elif num2_0 == "Odd" and num_random2 % 2 != 0:
		num2_1 *= 2
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Winning a bet: ", str(num2_1))
		money += num2_1
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money
	else:
		num2_1 *= 0
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "You lose.." + "\n" +
		colourFore(3) + colourBack(0) + colourStyle(2) + "Correct number: " + str(num_random2) + "\n" +
		colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money # Subcycle 2 dice(money)
def subdice3(money):
	os.system("cls")
	print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
	num3_0 = int(input(colourFore(7) + colourBack(0) + colourStyle(2) + "Enter a number from 1 to 6: "))
	num3_1 = int(input(colourFore(7) + colourBack(0) + colourStyle(2) + "Enter bet amount: "))
	money -= num3_1
	num_random3 = random.randint(1, 6)
	print(colourFore(3) + colourBack(0) + colourStyle(2) + "Bets are placed, spin the wheel! ...")
	print(colourFore(3) + colourBack(0) + colourStyle(2) + 'Number on dice: ' + '\n')
	subdiceanimation(num_random3)
	if num3_0 == num_random3:
		num3_1 *= 6
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Winning a bet: ", str(num3_1))
		money += num3_1
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money
	else:
		num3_1 *= 0
		print(colourFore(3) + colourBack(0) + colourStyle(2) + "You lose.." + "\n" +
		colourFore(3) + colourBack(0) + colourStyle(2) + "Correct number: " + str(num_random3) + "\n" +
		colourFore(3) + colourBack(0) + colourStyle(2) + "Balance: ", str(money) + "$" + "\n")
		intup_0 = input(colourFore(3) + colourBack(0) + colourStyle(2) + "Enter to back: " + "\n")
		return money # Subcycle 3 dice(money)

# DEFINITION COLOUR 
def colourFore(num):
	fore = ( Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE)
	fore_num = fore[num]
	return fore_num
def colourBack(num):
	back = ( Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE )
	back_num = back[num]
	return back_num
def colourStyle(num):
	style = ( Style.DIM, Style.NORMAL, Style.BRIGHT )
	style_num = style[num]
	return style_num 

#PRINT MENU TEXT DEFINITION
def print_main(money):
	print("                                                                       " + "\n"
		"                                                                       " + "\n"
		"                                                                       " + "\n"
		"                                                                       " + "\n"
		"                                                                       " + "\n"
		"                                                                       " + "\n"
		"                                                                       " + "\n"
		"                                                                       " + "\n"
		"                                                                       " + "\n"
		"                                                                       " + "\n"
		"                                                                       " + "\n"
		"                                                                       " + "\n"
		"                                                                       " + "\n" +
		"                                         " + colourFore(0) + colourBack(1) + colourStyle(1) + "T"
		+ colourFore(0) + colourBack(2) + colourStyle(0) + "H" +
		colourFore(0) + colourBack(3) + colourStyle(0) + "I" +
		colourFore(0) + colourBack(4) + colourStyle(0) + "S" +
		colourFore(0) + colourBack(5) + colourStyle(0) + " C" +
		colourFore(0) + colourBack(6) + colourStyle(0) + "A" +
		colourFore(0) + colourBack(1) + colourStyle(0) + "S" +
		colourFore(0) + colourBack(2) + colourStyle(0) + "I" +
		colourFore(0) + colourBack(3) + colourStyle(0) + "N" +
		colourFore(0) + colourBack(4) + colourStyle(0) + "O" +
		colourFore(0) + colourBack(5) + colourStyle(0) + " 7" +
		colourFore(0) + colourBack(6) + colourStyle(0) + "7" +
		colourFore(0) + colourBack(1) + colourStyle(0) + "7" + colourBack(0) + "\n")
	print("                                         " + colourFore(3) + colourBack(0) + colourStyle(2) + "Your balance = " + str(money) + "$" + "       " +  "\n" +
		"                                         " + "What games do you want to play?" + "       " +   "\n" +
		"                                         " + colourFore(5) + colourBack(0) + colourStyle(0) + "1 - Enter for play Roulette" + "       " +   "\n" +
		"                                         " + colourFore(2) + colourBack(0) + colourStyle(0) + "2 - Enter for play Dice" + "       " +   "\n" +
		"                                         " + colourFore(3) + colourBack(0) + colourStyle(0) + "3 - Enter for play One-armed bandit" + "       " +  "\n" +
		"                                         " + colourFore(1) + colourBack(0) + colourStyle(0) + "0 - Leave the casino" + "       " + "\n")

while game:
	init()
	nameuser = str(input('Enter name User on your computer' + '\n'))
	money = assignMoney()
	game = main(money)