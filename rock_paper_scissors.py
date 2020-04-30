import random 
import os
import sys

def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]

def clear():
	if platform is 'Windows':
		os.system('cls')
	else :
		os.system('clear')

def choose():
	global choice
	global choices
	choices = ["1","2","3"]
	choice = random.choice(choices)

def check(inpt):
	check_x = {1:0,2:1,3:2}
	check_y = {1:1,2:2,3:0}
	
	if inpt == choice:
		print("\nIt's a Draw.\n")
	elif inpt == choices[check_x[int(inpt)]] and choice == choices[check_y[int(inpt)]]:
		print("\nPrfft, You Lose.")
	else:
		print("\nYou Won!")

def interface():
	print("\n\n [1] Rock \n [2] Paper \n [3] Scissor \n\n [99] Exit ")
	inpt = input("\nEnter an your move: ")
	choose()
	if inpt in choices:
		check(inpt)
		result = {1:"Rock",2:"Paper",3:"Scissor"}
		input("\nYour move:\t"+result[int(inpt)]+"\nMy move:  \t"+result[int(choice)])
		clear()
	elif inpt == "99":
		exit()
	else:
		input("Give me a valid input, you crackhead. \n")
		clear()
		interface()

def main():
	global platform
	platform = get_platform()
	clear()
	input("Alright, think you could beat me? ^_-\n")
	input("Let's see\n")
	while True:
		interface()
		clear()

main()