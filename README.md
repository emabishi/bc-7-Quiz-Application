# Quizzler

*Quizzler* is a lightweight Command Line quiz application written in the Python language.

### Features
* Take quizzes directly from the terminal and immediately get scored based on your answers.
* Upload to and download quizzes from [Firebase] (http://firebase.com/ service).
* List quizzes in online Firebase storage.
* Import quizzes from any external location.
* Easy to develop quiz format. You can add your own quizzes and play them or test others.

### Dependencies | Requirements
* [Python 2.7.11] (https://www.python.org/downloads/) : Python Interpreter

* [requests 2.10.0] (http://docs.python-requests.org/en/master/) : Enables connection between Quizzler and Firebase
           ```pip install requests==1.1.0```

* [tqdm 4.5.0] (https://pypi.python.org/pypi/tqdm) : Enables implementation of progress bars
           ```pip install tqdm```

* [python-firebase 1.2] (https://pypi.python.org/pypi/python-firebase/1.2) : Enables easy connection between Firebase and Python
           ```pip install python-firebase```

* [Colorama==0.3.7 ]  (https://pypi.python.org/pypi/colorama) : Colour and font enhancing for python applications. ```pip install colorama```

* [pyfiglet==0.7.5] (https://pypi.python.org/pypi/pyfiglet): Takes ASCII text and renders it in ASCII art fonts.
```pip install https://pypi.python.org/packages/source/p/pyfiglet/pyfiglet-0.7.5.tar.gz```

* [termcolor==1.1.0] (https://pypi.python.org/pypi/termcolor): ANSII Color formatting for output in terminal. 
```pip install termcolor```

       
#### To install all requirements, download the [requirements.txt] (https://github.com/emabishi/bc-7-Quiz-Application/blob/master/requirements.txt) file then type this in your terminal application:
             pip install -r /path/to/requirements.txt

* To get you started, after installation, use the commands, listonline and download quiz <quiz name> or copy the quizzes in [this] (https://github.com/emabishi/bc-7-Quiz-Application/tree/master/QuizApp/quizzes) project's github repository and use the importquiz <quiz source path> command to import them into the Quizzler library. 


### Commands

|Command| Description|
|-----|---------------------------------------------------------|
|help | Displays all available commands and their descriptions |
| help (command) | Describes the command |
| listquizzes | Displays available local quizzes |
| takequiz (quiz name) | Launches the local quiz quiz name |
| listonline | Display available online quizzes |
| download (quiz) | Add a quiz to the local collection from online source |
| upload (quiz source path | Add quiz to online collection |
| importquiz (quiz source path) | Add quiz to local collection from external source |

### Copyright and Licensing
MIT license. For detailed licence information, see [license] (https://github.com/emabishi/bc-7-Quiz-Application/blob/master/LICENSE)

### Contact Information
Find the author at [@emabishi] (https://github.com/emabishi) on github.



