# Library to provide way of using operating system dependent functionality i.e.make directories
import os

# Library to manipulate JavaScript Object Notation files with python
import json

# Library to help randomise data
import random

#Library to enable printing and manipulation of time
import time

#Library to enable Command Line Interface Functionality
import cmd

#Enables progress bar functionality
from tqdm import tqdm

#Library to enable high level file functionality
import shutil

#Library to integrate with Firebase
from firebase import firebase

# Firebase database url to upload to and download quizzes from 
firebase_url = 'https://scorching-inferno-6139.firebaseio.com/'


# Firebase|Python API to update(PATCH, PUT), create(POST), or remove(DELETE) stored data
firebase = firebase.FirebaseApplication(firebase_url, None)



class Quiz(cmd.Cmd):
        """
        Class that includes all Quizzler functions

        """

        #Introduction script, runs when Quizzler begins

        prompt = '|Quizzler|'


        a = '*'
        b = '**'
        c = '***'
        d = '=' 
        e = '-'

        player_name = raw_input("What is your name Player?\n")
        print c + " Greetings! {} ".format(player_name).center(74, d) + c
        print " " 
        print c + " Welcome to Quizzler! ".center(74, d) + c
        print " " 
        print c + " Give me a moment to load! ".center(74, d) + c
        time.sleep(0.5)
        for x in tqdm(range(20)):
            time.sleep(0.1)
        print " "
        print " "
        print "       ".center(80,e) 
        print " Use these commands to explore quizzler's functionality.".center(74) 
        print " "
        time.sleep(0.5)
        print " COMMANDS ".center(78)
        print "  ".center(80,e)
        time.sleep(0.2)
        print c + " help ====| Displays all available commands and their descriptions ".center(74) + c
        time.sleep(0.2)
        print c + " help <command> ====| Describes the command ".center(74) + c
        time.sleep(0.2)
        print c + " listquizzes ====| Displays available local quizzes ".center(74) + c
        time.sleep(0.2)
        print c + " takequiz <quiz name> ====| Launches the local quiz quiz name ".center(74) + c
        time.sleep(0.2)
        print c + " listonline ====| Display available online quizzes ".center(74) + c
        time.sleep(0.2)
        print c + " downloadquiz <quiz source path> ====| Add a quiz to the local collection from online source ".center(74) + c
        time.sleep(0.2)
        print c + " uploadquiz ====| Add quiz to online collection ".center(74) + c
        time.sleep(0.2)
        print c + " importquiz <quiz source path> ====| Add quiz to local collection from external source ".center(74) + c
        time.sleep(0.5)
        print " "


        def do_listquizzes(self,line):

            """ 
            DESCRIPTION: List all local quizzes in Quizzler library
            USAGE: Command : listquizzes

            """

            path_to_local_quizzes = 'C:\\Quizzler\\Quizzes'

            #Check whether the folder structure exists, if it does not, create it
            if os.path.exists(path_to_local_quizzes) == False:
                os.makedirs(path_to_local_quizzes)

            print "***" + "These are your local quizzes".center(74,"*") + "***"

            for file in os.listdir(path_to_local_quizzes):

                #Check whether file is .json files
                if file.endswith(".json"):

                    #if it is, print it out without the .json extension
                    print ("="*37) + " " + ((file)[:len(file) - 5]) + " " + ("="*37)
                    time.sleep(1)

            #User tip
            print "\nTip: Use command 'takequiz <quizname> to begin taking a quiz\n".center(74," ")

            #Add some styling
            print " ".center(80,"*")




        def do_takequiz(self,quiz_name):

            """ 
            DESCRIPTION: List all local quizzes in Quizzler library
            USAGE: Command : takequiz <quiz name> Start taking a new quiz of quiz name
            """

            #name of local json file. get base name as quiz name
            path_to_quiz_LOTR = 'C:\\Quizzler\\Quizzes\\LOTR.json'

            #If quiz_name given by user is in the basename of the quiz: Allows for user errors
            if quiz_name in os.path.basename(path_to_quiz_LOTR):

                #use json load function to convert to list
                with open(path_to_quiz_LOTR) as LOTR_quiz:
                    LOTR = json.load(LOTR_quiz)
                
                #Pick questions in .json file
                questions = LOTR.keys()

                #Shuffle questions in quiz
                random.shuffle(questions)

                #Start quiz
                #Set initial score to Zero 
                score = 0

                #Monitor number of questions asked
                position = 0

                #Start timing now
                start_time = time.time()

                #default duration set : 10seconds * number of questions
                duration = 10 * len(questions)

                #While the position variable is less than the number of questions,
                while position < len(questions):

                    
                    #return a question in the quiz
                    print questions[position]

                    #There's still time left
                    out_of_time = False


                    #Prompt user for an answer
                    user_answer = raw_input("Please enter your answer.\n")

                    elapsed = time.time() - start_time


                    #Stop quiz if time is spent
                    if elapsed > duration:
                        out_of_time == True
                        print "Sorry! Your time's up!"
                        break

                    #Every time a question is answered print out the time left for the quiz
                    print "time remaining: %.f seconds" % (duration - elapsed)

                    #Check if answer is correct and return appropriate response 
                    if user_answer == LOTR[(questions[position])]:   
                        print "Your answer is correct! \n"
                        score += 1
                        print "Your score is {}".format(score)
                    else:
                        print "Your answer is incorrect \n"
                        print "Your score is {}".format(score)

                    #A question has been attempted, increment the position variable
                    position +=1

                    #Questions are over
                    if position == len(questions):
                        print "Your total score is {}".format(score)
                        print "\nQuestions in module over. Please take another quiz".center(78,"-")
                        print " \n"
                        print "Use <listquizzes> to see your list of local quizzes or <help> to view options.\n".center(74, "-")

            #If quiz does not exist,
            else:
                print "Invalid response.Quiz does not exist. Please try again. Use takequiz <quiz name>."
                print " "

            path_to_quiz_GOT = 'C:\\Quizzler\\Quizzes\\GOT.json'
            if quiz_name in os.path.basename(path_to_quiz_GOT):

                
                with open(path_to_quiz_GOT) as GOT_quiz:
                    GOT = json.load(GOT_quiz)

                
                questions  = GOT.keys()

                random.shuffle(questions)
  
                score = 0

                position = 0

                start_time = time.time()
                duration = 10 * len(questions)


                while position < len(questions):

                    print questions[position]

                    out_of_time = False


                    user_answer = raw_input("Please enter your answer.\n")

                    elapsed = time.time() - start_time

                    if elapsed > duration:
                        out_of_time == True
                        print "Sorry! Your time's up!"
                        break

                    print "time remaining: %.f seconds" % (duration - elapsed)
                    
                    if user_answer == GOT[(questions[position])]:
                        print "Your answer is correct! \n"

                        score += 1

                        print "Your score is {}").format(score)
                    else:
                        print "Your answer is incorrect \n"
                        print "Your score is {}".format(score)

                    #A question has been attempted, increment position variable
                    position +=1

                    if position == len(questions):
                        print "Your total socre is {} \n").format(score)
                        print "Questions in module over. Please take another quiz"
                        print "\nUse command <listquizzes> to see your list of local quizzes or help to view options.\n"

            else:
                print "Invalid response.Quiz does not exist."

        
        def do_importquiz(self,src):

             """ 
            DESCRIPTION: Import quiz from external location i.e.external drive or folder
            USAGE: Command : importquiz <quiz source path> 
            """

            #Local destination to store imported quizzes
            local_destination = 'C:\\Quizzler\\Imported Quizzes'

            #If folder does not exist, create it
            if os.path.exists(local_destination) == False:
                os.makedirs(local_destination)

            try:
                #Copy json file from source to destination
                shutil.copy(src,local_destination)
                print "Quiz successfully imported to local quiz folder"

            #Print Error message showing user that source and local path are the same
            except shutil.Error: 
                print "Error! Source path and local_destination are the same\n".center(74, "-")
                print "Please attempt import again.".center(74, "-")


            #Print Error message showing user that source destination does not exist
            except IOError:
                print "Source destination does not exist"


        
        def do_listonline(self,online_quizzes):

            """
                DESCRIPTION: List quizzes stored online
                USAGE: Command: listonline

            """

            # Perform a get request and read the online quizzes folder in Firebase
            #Quizzes stored under folder Quiz in Firebase

            online_quizzes = firebase.get('/Quiz', None) #Quiz holds quizzes


            # Loop over the onlinequizzes to list them 
            for quiz in online_quizzes:

                # Print quiz from firebase db
                print quiz


        def do_downloadquiz(self,quiz_name):

            """
                DESCRIPTION: List quizzes stored online
                USAGE: Command: downloadquiz <quiz name>

            """

            # Url for the selected json file in the Firebase database
            download_url = firebase_url + '/Quiz/' + quiz_name

            # Folder to store downloaded quiz
            destination_folder = "C:\\Quizzler\\Downloaded Quizzes"


            file_path = "C:\\Quizzler\\Downloaded Quizzes\\" + quiz_name + '.json'

            # Check if destination folder exists and create it if it does not exist
            if os.path.exists(destination_folder) == False:
                os.makedirs(destination_folder)


            #Check if file already exists

            if os.path.isfile(file_path) == True:
                print "Quiz already exists in local quiz folder"

            else:
                #use get request to Firebase to get the quiz
                result = firebase.get('/Quiz/' + quiz_name, None)

                #Copy the quiz
                try:
                    with open(file_path, 'w') as fp:
                        json.dump(result, fp)


                    print "-" + "Downloading file".center(74,"*") + "-"

                    #Show progress bar
                    for i in tqdm(range(10)):
                        sleep(0.5)
       

                except:

                    print "\nError! Quiz failed to download! Please try again\n".center(74, "*")
                    print "To download quiz please type: downloadquiz <quiz_name>",center(74, "*")             

        def do_uploadquiz(self,quiz_source_path):

            """
                DESCRIPTION: Upload quiz to online Firebase database
                USAGE: Command: uploadquiz <quiz name>

            """

            quiz_full_path = quiz_source_path + ".json"
            quiz_name = os.path.basename(quiz_source_path)

            quiz_name_to_post = str(quiz_name)


            #If file exists, upload
            if os.path.isfile(quiz_full_path) == True:
                print "File existence confirmed".center(74, "-")

                # Write the contents to json file
                with open(quiz_full_path, 'r') as json_file:
                    try:

                        # Use json.load to move contents
                        quiz = json.load(json_file)

                        print "Uploading Quiz {}".format(quiz_name).center(74,"-")

                        for n in tqdm(range(10)):
                            time.sleep(0.5)

                        # Call a put request and save to the firebase database 
                        firebase.put("/Quiz/",quiz_name, quiz)

                        print "\nQuiz successfully uploaded!\n".center(74,"-")

                    except:

                        print "Upload failed! Please type upload<quiz_name> to try again.\n".center(74,"-")
                        print "Type help<uploadquiz> for help."

            else:
                print "Quiz does not exist at source.".center(74,"-")


            def do_EOF(self,line):
                return True

if __name__ == '__main__':
    Quiz().cmdloop()