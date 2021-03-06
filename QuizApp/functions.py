#Quizzler Command Line Application
#Author : Mabishi Elizabeth for Andela Kenya
#Date: 5th May 2016
#Version 1.0

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

#Library to enhance User Experience with colours
from colorama import Fore, Back, Style

from colorama import init


#Library to enhance User Experience with colours
from termcolor import cprint 

#Library to enhance User Experience with colours and different text fonts
from pyfiglet import figlet_format

#Library to hook system specific parameters
import sys

#Library to prettify tables
from prettytable import PrettyTable


#Library to integrate with Firebase
from firebase import firebase

# Firebase database url to upload to and download quizzes from 
firebase_url = 'https://scorching-inferno-6139.firebaseio.com/'


# Firebase|Python API to update(PATCH, PUT), create(POST), or remove(DELETE) stored data
firebase = firebase.FirebaseApplication(firebase_url, None)

this_path = os.path.dirname(os.path.abspath(__file__))
sounds_path = this_path + '/sounds/'
quizzes_path = this_path + '/quizzes/'

class Quiz(cmd.Cmd):
        """
        Class that includes all Quizzler functions

        """

        #Introduction script, runs when Quizzler begins

        prompt = '|Quizzler|'

        cprint(figlet_format('QUIZZLER!', font='cyberlarge'),
       'yellow', 'on_red', attrs=['bold'])
        cprint(figlet_format('Test Yourself!', font='cyberlarge'),
       'yellow', 'on_red', attrs=['bold'])


        init()

        # strip colors if stdout is redirected
        init(strip=not sys.stdout.isatty())

        #os.system("start C:\QuizzlerSounds\CrowdCheer.wav")


        a = '*'
        b = '**'
        c = '***'
        d = '=' 
        e = '-'

        print "-".center(78, e)
        print " "
        player_name = raw_input("What is your name Player?\n")
        print " "
        print "-".center(78, e)
        print c + " Greetings! {} ".format(player_name).center(74, d) + c
        print " " 
        print Fore.YELLOW + c + " Welcome to Quizzler! ".center(74, d) + c
        print " " 
        print c + " Give me a moment to load! ".center(74, d) + c
        time.sleep(0.5)
        for x in tqdm(range(20)):
            time.sleep(0.1)
        print " "
        print " "
        print Fore.YELLOW +   "       ".center(80, e) 
        print Fore.YELLOW + " Use these commands to explore quizzler's functionality.".center(74) 
        print " "
        time.sleep(0.5)
        print Fore.YELLOW + " COMMANDS ".center(78)
        print "  ".center(80, e)


        #Make table green
        print Fore.GREEN + " "
        

        #Make table with Commands list
        
        x  = PrettyTable(["Command", "Description"])
        x.add_row(["help", "Displays all available commands and their descriptions"])
        x.add_row(["help <command>", "Describes the command"])
        x.add_row(["listquizzes", "Displays available local quizzes"])
        x.add_row(["takequiz <quiz name>", "Launches the local quiz, quiz name"])
        x.add_row([" listonline", "Display available online quizzes "])
        x.add_row(["download <quiz source path>", "Add quiz to local collection from online source"])
        x.add_row(["import <quiz source path>", "Add quiz to local collection from external source "])
        x.add_row(["upload <quiz source path>", "Add quiz from local collection to online database  "])

        print x
        print " "

        #Rest colorama colours
        print(Style.RESET_ALL)

        def do_listquizzes(self, line):

            """ 
            DESCRIPTION: List all local quizzes in Quizzler library
            USAGE: Command : listquizzes

            """

            #path_to_quizzes = 'C:\\Quizzler\\Quizzes'

            #Check whether the folder structure exists, if it does not, create it
            if os.path.exists(quizzes_path) == False:
                os.makedirs(quizzes_path)

            #Filesize of new empty folder = 0
            if os.path.getsize(quizzes_path) == 0:
                print "You currently have no quizzes. Please import or download a quiz. See help for details."

            elif os.path.getsize(quizzes_path) != 0:
                print "***" + "These are your local quizzes".center(74, "*") + "***"

            for file in os.listdir(quizzes_path):

                #Check whether file is .json files
                if file.endswith(".json"):

                    #if it is, print it out without the .json extension
                    print ("="*37) + " " + ((file)[:len(file) - 5]) + " " + ("="*37)
                    time.sleep(1)

            #User tip
            print "\nTip: Use command 'takequiz <quizname> to begin taking a quiz\n".center(74," ")

            #Add some styling
            print " ".center(80,"*")




        def do_takequiz(self, quiz_name):

            """ 
            DESCRIPTION: Begin taking a quiz.
            USAGE: Command : takequiz <quiz name> Start taking a new quiz of quiz name
            """
            quiz_name = quiz_name.upper()
            path_to_quiz = quizzes_path + quiz_name +'.json'

            try:

                #If quiz_name given by user is in the basename of the quiz: Allows for user errors
                if quiz_name in os.path.basename(path_to_quiz):

                    #use json load function to convert to list
                    with open(path_to_quiz) as quiz:
                        quiz_data = json.load(quiz)
                    
                    #Pick questions in .json file
                    questions = quiz_data.keys()

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

                        # Add Space for readability
                        print " "

                        #There's still time left
                        out_of_time = False


                        #Prompt user for an answer
                        user_answer = raw_input("Please enter your answer.\n")

                        elapsed = time.time() - start_time


                        #Stop quiz if time is spent
                        if elapsed > duration:
                            out_of_time == True
                            print Fore.RED +"Sorry! Your time's up!"
                            print(Style.RESET_ALL)
                            break

                        #Add space for readability
                        print " "

                        #Every time a question is answered print out the time left for the quiz
                        print "time remaining: %.f seconds" % (duration - elapsed)

                        #Check if answer is correct and return appropriate response 
                        correct_answer  = str(quiz_data[(questions[position])])
                        if user_answer.upper() == correct_answer.upper():
                            print " "
                            print Fore.GREEN +"Your answer is correct! \n"

                            #Play this sound
                            #os.system("start C:\QuizzlerSounds\AudienceApplause.wav")

                            print(Style.RESET_ALL)

                            print " "

                            score += 1

                            print "Your score is {}".format(score)
                        else:
                            print " " 
                            print Fore.RED +"Your answer is incorrect \n"

                            
                            print(Style.RESET_ALL)

                            
                            print "Your score is {}".format(score)
                            print " "

                        #A question has been attempted, increment the position variable
                        position += 1

                        #Questions are over
                        if position == len(questions):
                            print "Your total score is {}".format(score)
                            print "\nQuestions in module over. Please take another quiz".center(78,"-")
                            print " \n"
                            print "Use <listquizzes> to see your list of local quizzes or <help> to view options.\n".center(74, "-")

                #If quiz does not exist,
            except IOError:
                print "Invalid response.Quiz does not exist. Please try again. Use takequiz <quiz name>."
                print " "


            
        
        def do_import(self, src):
            """
            DESCRIPTION: Import quiz from external location other than the internet. Use for external and internal storage locations
            USAGE: Command : import <quiz source path>
            """

            #local_destination = 'C:\\Quizzler\\Quizzes'

            #If folder does not exist, create it
            if os.path.exists(quizzes_path) == False:
                os.makedirs(quizzes_path)

            try:
                #Copy json file from source to destination
                shutil.copy((src + '.json'),quizzes_path)
                print "Quiz successfully imported to local quiz folder"

            #Print Error message showing user that source and local path are the same
            except shutil.Error: 
                print "Error! Source path and local_destination are the same\n".center(74, "-")
                print "Please attempt import again.".center(74, "-")


            #Print Error message showing user that source destination does not exist
            except IOError:
                print "Source destination does not exist"


        
        def do_listonline(self, online_quizzes):

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
                print " "


        def do_download(self, quiz_name):

            """
                DESCRIPTION: Download quizzes stored in the online database
                USAGE: Command: download <quiz name>

            """
            quiz_name = quiz_name.upper()

            # Url for the selected json file in the Firebase database
            download_url = firebase_url + '/Quiz/' + quiz_name

            # Folder to store downloaded quiz
            #destination_folder = "C:\\Quizzler\\Quizzes"


            file_path = quizzes_path + quiz_name + '.json'

            # Check if destination folder exists and create it if it does not exist
            if os.path.exists(quizzes_path) == False:
                os.makedirs(quizzes_path)


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
       

                except:

                    print "\nError! Quiz failed to download! Please try again\n".center(74, "*")
                    print "To download quiz please type: downloadquiz <quiz_name>".center(74, "*")             

        def do_upload(self, quiz_source_path):

            """
                DESCRIPTION: Upload quiz to online Firebase database
                USAGE: Command: upload <quiz source path>

            """

            quiz_full_path = quiz_source_path + ".json"
            quiz_name = os.path.basename(quiz_source_path)

            quiz_name_to_post = str(quiz_name)


            #If file exists, upload
            if os.path.isfile(quiz_full_path) == True:
                print "File existence confirmed".center(74, "-")

                #Space for readability
                print " "

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
                        
                        print " "

                    except:

                        print "Upload failed! Please type upload<quiz_name> to try again.\n".center(74,"-")
                        print "Type help<uploadquiz> for help."

            else:
                print "Quiz does not exist at source.".center(74,"-")

        #def do_applause(self,line):

            #Play wav file
            #os.system("start C:\QuizzlerSounds\AudienceApplause.wav")


        def do_EOF(self, line):
            return True

if __name__ == '__main__':
    Quiz().cmdloop()