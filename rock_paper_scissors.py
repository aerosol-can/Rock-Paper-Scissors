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
	global win0
	global win1
	win0 = False
	win1 = False
	
	if inpt == choice: 
		input("\nIt's a Draw.\n")
		
	elif inpt == choices[check_x[int(inpt)]] and choice == choices[check_y[int(inpt)]]:
		input("\nPrfft, You Lose.")
		win0 = True
	else:
		input("\nYou Won!")
		win1 = True

def point(plyr,point):
	points[plyr] = points[plyr]+point

def interface():
	print("\n\n [1] Rock \n [2] Paper \n [3] Scissor \n\n [99] Exit ")
	inpt = input("\nEnter an your move: ")
	choose()
	if inpt in choices:
		check(inpt)
		result_dict = {1:"Rock",2:"Paper",3:"Scissor"}
		input("\nYour move:\t"+result_dict[int(inpt)]+"\nMy move:  \t"+result_dict[int(choice)])
		if win0 == True:
			point(0,1)
		elif win1 == True:
			point(1,1)
		clear()
	elif inpt == "99":
		exit()
	else:
		input("Give me a valid input, you crackhead. \n")
		clear()
		interface()

def main():
	global platform
	global points
	points = [0,0]
	platform = get_platform()
	clear()
	input("Alright, think you could beat me? ^_-\n")
	input("Let's see\n")
	while True:
		option = input("Do you want it to be a \n[1] Regular game\n\tor a \n[2] Point Match \n")
		if option == '1':
			interface()
			clear()
		elif option == '2':
			iteration = int(input("How many matches do you want in the Game?\n"))
			for i in range(iteration):
				interface()
				clear()
			input("\n\n\nScore is: \n\t" + "Me: " + str(points[0]) + "\n\tYou: " + str(points[1]))
			inpt = input("Wanna exit? [y/n]\n")
			if inpt is 'y':
				exit()
			else:
				main()

if __name__ == "__main__" :
	main()
