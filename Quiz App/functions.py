import time
import os

# Function to run Introduction to Quizzler game
def intro():
	print("Welcome to Quizzler!")
	player_name = input("What is your name, player?")
	print(player_name, "Use these commands to explore quizzler's functionality.\n")
	time.sleep(0.5)
	print (help())

#Function to List Quizzler commands
def help():
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
def list_quizzes():
	path_to_local_quizzes = 'C:\\Quizzler\\Quizzes'

	#Check whether the folder structure exists, if it does not, create it
	if os.path.exists(path_to_local_quizzes) == False:
		os.makedirs(path_to_local_quizzes)
	for file in os.listdir(path_to_local_quizzes):

		#Check whether file is .json files
		if file.endswith(".json"):

			#if it is, print it out without the .json extension
			print(file)[:len(file) - 5]
	#User tip
	#print("\n Use command 'takequiz<quizname>' to begin taking a quiz")

	#Add some styling
	#print("\n" + "$" *20 + "=" * 20 + "%" * 20 + "\n")

def rank():
	level_response = input("Please choose your prefered player level.\n Type 'B' or 'b' for Beginner Mode\n Type 'I' or 'i' for intermediate Mode and\n Type 'G' or 'g' for Guru Mode")
	while True:
		try:
			if level_response == "Beginner" or "B" or "b":
			 	 #launch beginner module
			 	 #time_per_question = 10 seconds
			 	 #call take_quiz function
			 elif level_response == "Intermediate" or "I" or "i":
			 	 #launch intermediate module
			 	 #time_per_question = 7 seconds
			 	 #call take quiz function
			 elif level_response == "Guru" or "G" or "g":
			 	#launch guru module
			 	#time per question = 6 seconds
			 	#launch take quiz function
		except ValueError:
			 return "Invalid response: Please enter your preferred player level.\n Type 'B' or 'b' for Beginner Mode\n Type 'I' or 'i' for intermediate Mode and\n Type 'G' or 'g' for Guru Mode"

#takequiz <quiz_name> - Start taking a new quiz
def take_quiz(quiz_name):
	quiz_name = input("\n Use command 'takequiz<quizname>' to begin taking a quiz\n")    

	#name of local json file. get base name as quiz name
	path_to_quiz_LOTR = 'C:\\Quizzler\\Quizzes\\LOTR'
	if quiz_name == os.path.basename(path_to_quiz_LOTR):
		#use json load function to convert to list

		#run LOTR quiz-----get questions and answers
	path_to_quiz_GOT = 'C:\\Quizzler\\Quizzes\\GOT'
	elif quiz_name == os.path.basename(path_to_quiz_GOT):
		#use json load function to convert to list


		#run quiz
	path_to_quiz_MATH = 'C:\\Quizzler\\Quizzes\\MATH'
	elif quiz_name == os.path.basename(path_to_quiz_MATH):
		#use json load function


		#run quiz