import os
import json
import random
import time
import cmd
from tqdm import tqdm
import shutil
from firebase import firebase

# Firebase db url to upload and download samplequiz
firebase_url = 'https://scorching-inferno-6139.firebaseio.com/'


# API to update(PATCH, PUT), create(POST), or remove(DELETE) stored data
firebase = firebase.FirebaseApplication('https://scorching-inferno-6139.firebaseio.com/', None)



class Quiz(cmd.Cmd):
        prompt = '(Quizzler)'


    #Change deafult prompt to 'Quizzler'
        #prompt = '(Quizzler)'
        player_name = raw_input("What is your name Player?\n")
        print("========================Greetings {}!=======================").format(player_name)
        print("=================Welcome to Quizzler!====================")
        print("\n=============Give me a moment to load!=================\n")
        for x in tqdm(range(20)):
            time.sleep(0.1)
        print("\nUse these commands to explore quizzler's functionality.\n")
        time.sleep(0.5)
        print ("\n  ====================Commands====================  \n")
        time.sleep(0.2)
        print ("\nhelp ===================== `Displays all available commands and their descriptions`\n")
        time.sleep(0.2)
        print ("\nhelp<command> ============ 'Describes the command\n")
        time.sleep(0.2)
        print ("\nlistquizzes ============== 'Displays available local quizzes \n")
        time.sleep(0.2)
        print ("\ntakequiz<quiz_name> ====== 'Launches the local quiz quiz_name'\n")
        time.sleep(0.2)
        print ("\nlistonline   ============= 'Display available online quizzes'\n")
        time.sleep(0.2)
        print ("\ntakeonline <quiz_name> ====`Launch the online quiz quiz_name`\n")
        time.sleep(0.2)
        print ("\nimportquiz <path_to_json> = `Add a quiz to the local collection`\n")
        time.sleep(0.2)
        print ("\npublishquiz  ==============='Add quiz to online collection\n")



        #listquizzes command-  List of all the available quizzes in your library
        #quizzes stored in C:Quizzler\\Quizzes
        def do_listquizzes(self,line):
            """ 
            DESCRIPTION: List all local quizzes in quiz app
            USAGE: Command : listquizzes

            """
            path_to_local_quizzes = 'C:\\Quizzler\\Quizzes'

            #Check whether the folder structure exists, if it does not, create it
            if os.path.exists(path_to_local_quizzes) == False:
                os.makedirs(path_to_local_quizzes)

            print("These are your local quizzes")

            for file in os.listdir(path_to_local_quizzes):

                #Check whether file is .json files
                if file.endswith(".json"):

                    #if it is, print it out without the .json extension
                    print "=============="+((file)[:len(file) - 5])+"================="
                    time.sleep(1)

            #User tip
            print("\nTip: Use command 'takequiz<quizname>' to begin taking a quiz\n")

            #Add some styling
            print("$" *20 + "=" * 20 + "%" * 20)



        #takequiz <quiz_name> - Start taking a new quiz  i.e. takequiz LOTR
        def do_takequiz(self,quiz_name):
            #quiz_name = raw_input("Use command 'takequiz<quizname>' to begin taking a quiz\n")    

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

                start_time = time.time()
                duration = 10 * len(questions)
                while position < len(questions):

                    
                    #return a question in the quiz
                    print questions[position]

                    #Still time left
                    out_of_time = False


                    #Prompt user for an answer
                    user_answer = raw_input("Please enter your answer.\n")
                    elapsed = time.time() - start_time
                    if elapsed > duration:
                        out_of_time == True
                        print("Sorry! Your time's up!")
                        break
                    print "time remaining: %.f seconds" % (duration - elapsed)
                    if user_answer == LOTR[(questions[position])]:   #Answer to question
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
                        print("\nUse command <listquizzes> to see your list of local quizzes or help to view options.\n")

            #else:
                #print "Invalid response.Quiz does not exist."

            path_to_quiz_GOT = 'C:\\Quizzler\\Quizzes\\GOT.json'
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
                    user_answer = raw_input("Please enter your answer.\n")
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
                        print("\nUse command <listquizzes> to see your list of local quizzes or help to view options.\n")

            #else:
                #print "Invalid response.Quiz does not exist."
        #Import quiz function
        def do_importquiz(self,src):

            #Source path
            #src = raw_input("Please enter the source path for the quiz you'd like to import\n")
            # src = str(src)
            # src = os.path.abspath(src)

            #Local destination to store imported quizzes
            local_destination = 'C:\\Quizzler\\Imported Quizzes'

            #If folder does not exist, create it
            if os.path.exists(local_destination) == False:
                os.makedirs(local_destination)

            try:
                #Copy json file from source to destination
                shutil.copy(src,local_destination)
                print ("Quiz successfully imported to local quiz folder")

            #Print Error message showing user that source and local path are the same
            except shutil.Error: 
                print("Error! Source path and local_destination are the same\n Please attempt import again.")


            #Print Error message showing user that source destination does not exist
            except IOError:
                print("Source destination does not exist")


        #List online quiz function function
        def do_list_online(self,online_quizzes):

            """
                DESCRIPTION
                    List quizzes stored online
                    EXAMPLE USAGE:
                        listonline
                """

            # Perform a get request and store the root file in the online quizzes folder in C

            online_quizzes = firebase.get('/Quiz', None) #Quiz holds quizzes


            # Loop over the samplequizzes to list them 
            # Call enumerate method to arrange the quizzes starting from 1
            for quiz in online_quizzes:

                # Print quiz from firebase db
                print quiz


        def do_EOF(self,line):
            return True

if __name__ == '__main__':
    Quiz().cmdloop()