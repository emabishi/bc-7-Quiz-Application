import time
import os
import json
import random
import requests
from firebase import firebase as firebase_lib
import urllib
from tqdm import tqdm
import Tkinter as tk

class Quiz(cmd.Cmd):

#Function to List Quizzler commands
	def do_inst(self,line):
		print("=================Welcome to Quizzler!====================")
		print("\n=============Give me a moment to load!=================\n")
		for x in tqdm(range(20)):
			sleep(0.1)
		print("Player, Use these commands to explore quizzler's functionality.\n")
		time.sleep(0.5)
		print("====================Commands==================== \n")
		time.sleep(0.2)
		print("help ===================== `Displays all available commands`\n")
		time.sleep(0.2)
		print("help<command> ============ 'Describes the command\n")
		time.sleep(0.2)
		print("listquizzes ============== 'Displays available local quizzes \n")
		time.sleep(0.2)
		print("takequiz<quiz_name> ====== 'Launches the local quiz quiz_name'\n")
		time.sleep(0.2)
		print("listonline   ============= 'Display available online quizzes'\n")
		time.sleep(0.2)
		print("takeonline <quiz_name> ====`Launch the online quiz quiz_name`\n")
		time.sleep(0.2)
		print("importquiz <path_to_json> = `Add a quiz to the local collection`\n")
		time.sleep(0.2)
		print("publishquiz  ==============='Add quiz to online collection")


	#listquizzes command-  List of all the available quizzes in your library
	#quizzes stored in C:Quizzler\\Quizzes
	def d0_list_quizzes(self,line):
		path_to_local_quizzes = 'C:\\Quizzler\\Quizzes'

		#Check whether the folder structure exists, if it does not, create it
		if os.path.exists(path_to_local_quizzes) == False:
			os.makedirs(path_to_local_quizzes)

		print("These are your local quizzes")

		for file in os.listdir(path_to_local_quizzes):

			#Check whether file is .json files
			if file.endswith(".json"):

				#if it is, print it out without the .json extension
				#Prettify it
				#print((file)[:len(file) - 5])
				print "=============="+((file)[:len(file) - 5])+"==============="

				#Display them a little slowly
				time.sleep(1)

		#User tip
		print("\nTip: Use command 'takequiz<quizname>' to begin taking a quiz\n")

		#Add some styling
		print("$" *20 + "=" * 20 + "%" * 20)


	#takequiz <quiz_name> - Start taking a new quiz
	def do_take_quiz(quiz_name):
		quiz_name = input("Use command 'takequiz<quizname>' to begin taking a quiz\n")    

		#name of local json file. get base name as quiz name
		path_to_quiz_LOTR = 'C:\\Quizzler\\Quizzes\\LOTR.json'
		if quiz_name in os.path.basename(path_to_quiz_LOTR):

			#use json load function to convert to list
			with open(path_to_quiz_LOTR) as LOTR_quiz:
				LOTR = json.load(LOTR_quiz)
			
			#run LOTR quiz----- #1. Shuffle questions in quiz
			questions = LOTR.keys()
			random.shuffle(questions)

			#Start quiz
			#Set initial score to Zero 
			score = 0

			#Monitor number of questions asked
			position = 0
			while position < len(questions):

				
				#Start timing
				start_time = time.time()
				duration = 10
				
				#return a question in the quiz
				print questions[position]

				#Still time left
				out_of_time = False

				#For each question
				for question in questions:
					if time.time() - start_time > duration:
						out_of_time == True
						print("Sorry! Your time's up!")
						break

				#Prompt user for an answer
				user_answer = input("Please enter your answer.\n")
				if user_answer == LOTR[(questions[position])]:   #Answer to question
					print("Your answer is correct! \n")
					score += 1
					print("Your score is {}").format(score)
				else:
					print("Your answer is incorrect \n")
					print("Your score is {}").format(score)

				#A question has been attempted, increment position variable
				position +=1

				#Get elapsed time
				elapsed = (time.time() - start_time)

				# Get remaining time
	            remaining = int(duration - elapsed)

	            # Display remaing time in user friendly formatting
	            print "\tTime remaining: " + str(remaining) + " seconds\n"

				if position == len(questions):
					print("Your total socre is {} \n").format(score)
					print("Questions in module over. Please take another quiz")


					#Call list quizzes function
					list_quizzes()
		else:
			print "Invalid response.Quiz does not exist."


		path_to_quiz_GOT = 'C:\\Quizzler\\Quizzes\\GOT'
		if quiz_name in os.path.basename(path_to_quiz_GOT):
			#use json load function to convert to list
			with open(path_to_quiz_GOT) as GOT_quiz:
				GOT = json.load(GOT_quiz)

			#run quiz
			questions  = GOT.keys()
			random.shuffle(questions)

			#Start quiz
			#Set initial score to Zero 
			score = 0

			#Monitor number of questions asked
			position = 0
			while position < len(questions):

				#return a question in the quiz
				print questions[position]

				#Call start timing function
				#start_timing()

				#Prompt user for an answer
				user_answer = input("Please enter your answer.\n")
				if user_answer == GOT[(questions[position])]:
					print("Your answer is correct! \n")
					score += 1
					print("Your score is {}").format(score)
				else:
					print("Your answer is incorrect \n")
					print("Your score is {}").format(score)
				#A question has been attempted, increment position variable
				position +=1
				if position == len(questions):
					print("Your total socre is {} \n").format(score)
					print("Questions in module over. Please take another quiz")


					#Call list quizzes function
					list_quizzes()
		else:
			print "Invalid response.Quiz does not exist."

		path_to_quiz_MATH = 'C:\\Quizzler\\Quizzes\\MATH'
		if quiz_name in os.path.basename(path_to_quiz_MATH):

			#use json load function to convert to list
			with open(path_to_quiz_MATH) as MATH_quiz:
				MATH = json.load(MATH_quiz)

			#run quiz
			questions  = MATH.keys()
			random.shuffle(questions)

			#Start quiz
			#Set initial score to Zero 
			score = 0

			#Monitor number of questions asked
			position = 0
			while position < len(questions):

				#return a question in the quiz
				print questions[position]


				#Prompt user for an answer
				user_answer = input("Please enter your answer.\n")
				if user_answer == MATH[(questions[position])]:
					print("Your answer is correct! \n")
					score += 1
					print("Your score is {}").format(score)
				else:
					print("Your answer is incorrect \n")
					print("Your score is {}").format(score)
				#A question has been attempted, increment position variable
				position +=1
				if position == len(questions):
					print("Your total socre is {} \n").format(score)
					print("Questions in module over.")

					#Call play_again function
					play_again()

		else:
			print "Invalid response.Quiz does not exist."


	def do_play_again():
		#ask play_again
		play_again_response  = input("Would you like to play again?")

		#if input is yes, return quiz list
		if play_again_response == "YES" or "Y" or "y":
			list_quizzes()
	    
		#else exit game
		else:
			raise SystemExit

	def do_EOF(self,line):
		return True

if __name__ == '__main__':
    Quiz().cmdloop()

