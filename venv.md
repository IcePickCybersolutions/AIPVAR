# Setting up Rasputin's Home 
### Creating a Virtual Environment in Python

Welcome, this is all about how to set up the virtual environment that will have all the right packages to run my code.
If you are looking for a good tutorial on setting up virtual environments for your own code [check out this tutorial.](https://realpython.com/python-virtual-environments-a-primer/)

Anyway, here it is:

##### Ingredients:
* Python 3
* A fair bit of storage
* A somewhat-well named folder
* An internet connection

### On Mac/Linux/Windows:
(anything that I type in quotes is somehting to type, don't include the quotes tho)

(if it's italicized it's a placeholder that you should replace with your own values)
1. In terminal/cmd "pip install virtualenv" (installs the virtualenv tool systemwide)
3. Create or navigate to the folder where Rasputin will live
4. Terminal: "python3 -m venv *name of your virtual environment*" (creates the virtual environment)
5. Terminal: "source env/bin/activate" (activates the virtualenv and allows you to affect only it with your commands)
6. Terminal: "pip install *the following packages*" [SpeechRecognition](https://pypi.org/project/SpeechRecognition/), [pyttsx3](https://pypi.org/project/pyttsx3/), [wikipedia](https://pypi.org/project/wikipedia/), [wolframalpha](https://pypi.org/project/wolframalpha/), [requests](https://pypi.org/project/requests/)
7. Terminal: "deactivate" (you're no longer in the virtual environment, type source env/bin/activate to reopen it and add more stuff)
8. Thats that, if everything worked right, you should now have a working voice assistant!
