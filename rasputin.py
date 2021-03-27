'''
I'd like to thank you for reading my code, pls be nice tho ;)
If you're a little newer to this whole coding thingy,
don't stress, theres a metric ton of comments that I think explain it all rather nicely.
And if you are more experienced, feel free to shoot me a message or comment on anything that I could've done better
'''

'''
Just importing a bunch of dependencies so the damn thing works
Check out the venv folder on my github page for how to set up a virtual environment for this script to work.
'''
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import smtplib
import ssl
import pyautogui

# starting up the speech recognition engine (sapi5) which only works on windows
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


# function for how the engine should speak
def speak(text):
    engine.say(text)
    engine.runAndWait()


# function for basic pleasantries
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello World")
        print("Hello World")
    elif hour>=12 and hour <=18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")


# this takes input from speech and responds to it with actions defined later
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Awaiting commands...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

		# if it can't understand you it asks you to say it again
        except Exception as e:
            speak("Repeat instructions")
        return "None"
    return statement
# and thats the end of our functions

# when the machine starts up it should introduce itself and greet you
print("Loading in Artificially Intelligent Personal Assistant Rasputin")
speak("Loading in AIPAR")
wishMe()

# makes sure that it's still active, and if so offers its services
if __name__=='__main__':
    while True:
        speak("Issue further commands.")
        statement = takeCommand().lower()
        if statement==0:
            continue

		# will shut down the program if you ask it to
        if "good bye" or "see you later" or "have a good one" or "stop" in statement:
            speak("Good Night")
            print("Exiting AIPA Rasputin")
            break

# from here we define commands and what they will do
'''To write your own command use this 'formula'

if "spoken-command" or "alternative spoken command" in statement:
	speak("What you want Rasputin to say")
	commandstotellrasputinwhatyouwantdonewhenusaythat
	time.slee(5)


Here are some general commands to do stuff:
 - to have rasputin open a file/start a specific program: subprocess.Popen("rwhere/that/file/is.exe")
 - to have rasputin open a certain webpage: webbrowser.open_new_tab("https://website.com")
 -

'''
        # will search wiki and both speak and pring out the results
        if 'wikipedia' or 'wiki' in statement:
            speak("Searching Wikipedia...")
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # activates one proxy server connection to better hide you on the internet
        elif 'activate proxies' in statement:
            pyautogui.keyDown('winright')
            pyautogui.press('r')
            pyautogui.keyUp('winright')
            pyautogui.write('cmd')
            pyautogui.press('enter')
            pyautogui.press('left')
            pyautogui.press('enter')
            pyautogui.write(r'cd C:"\\"Windows"\"SysWOW64')
            pyautogui.press('enter')
            # replace the variables with values like 131.72.69.14:8080, just google "free proxy list for options" spys.one is a good site for finding these
            pyautogui.write('netsh winhttp set proxy proxyServerIP:proxyServerPort')
            speak("Proxies active.")

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is now open")
            time.sleep(5)

        # this doesn't actually search anything, but simply opens the google webpage
        elif 'open google' or 'browse' or 'google' in statement:
            webbrowser.open_new_tab("https://google.com")
            speak("Search is ready")
            time.sleep(5)

        elif 'open gmail' or 'email' or 'get messages' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Emails prepared")
            time.sleep(5)

        elif 'drive' or 'docs' or 'my drive' in statement:
            webbrowser.open_new_tab("https://drive.google.com/drive/u/0/my-drive")
            speak("Google Docs is loaded")
            time.sleep(5)

        # if you're gonna comment on this i already know u have an android
        elif 'icloud' in statement:
            webbrowser.open_new_tab("https://www.icloud.com/")
            speak("Apple cloud services operational")
            time.sleep(5)

        # i love this site, use it for all sorts of stuff
        # it's basically a schedule app
        elif 'pipefy' or 'kapkan' or 'kanban' or 'pipes' in statement:
            webbrowser.open_new_tab("https://app-auth.pipefy.com/login")
            speak("Pipes are read to be clogged")
            time.sleep(5)

        elif 'translate' or 'reverso' in statement:
            webbrowser.open_new_tab("https://www.reverso.net/text_translation.aspx?lang=EN")
            speak("Translations ready to be made, and well")
            time.sleep(5)

        elif 'gimp' in statement:
            subprocess.Popen(r"C:\Program Files\GIMP 2\bin\gimp-2.10.exe")
            speak("Painbrushes at the ready")
            time.sleep(5)

        # if you're into design and haven't tried figma, please do, it's free and easy
        elif 'figma' in statement:
            subprocess.Popen(r"C:\Users\user\AppData\Local\Figma\Figma.exe")
            speak("Creative juices flowing?")
            time.sleep(5)

        # if you're wondering what ide i use, this is one, on each differnet vm and machine i use a different one tho
        elif "atom" in statement:
            subprocess.Popen(r"C:\Users\user\AppData\Local\atom\atom.exe")
            speak("Better not be replacing me")
            time.sleep(5)

        elif "geforce" or "geforce experience" in statement:
            subprocess.Popen(r"C:\Program Files\NVIDIA Corporation\NVIDIA GeForce Experience\NVIDIA GeForce Experience.exe")
            speak("Gaming time")
            time.sleep(5)

        elif "steam" in statement:
            subprocess.Popen(r"C:\Program Files (x86)\Steam\Steam.exe")
            speak("Booting steam")
            time.sleep(5)

        # somewhat useful website building tool, wouldn't recommend it unless you can get it free/really cheap
        elif "bootstrap studio" or "bss" in statement:
            subprocess.Popen(r"C:\Users\user\AppData\Local\Programs\bstudio\Bootstrap Studio.exe")
            speak("Ready to kill another site design")
            time.sleep(5)

        # not sponsored, but the limiter features are nice
        elif "opera" or "opera gx" in statement:
            subprocess.Popen(r"C:\Users\user\AppData\Local\Programs\Opera GX\launcher.exe")
            speak("Background browser up and running")
            time.sleep(5)

        elif "discord" or "comms" in statement:
            subprocess.Popen(r"C:\Users\user\AppData\Local\Discord\Update.exe --processStart Discord.exe")
            speak("Comms open")
            time.sleep(5)

        # my editor friend gets mad if i use anything of a lower caliber
        elif "obs" or "recording" or "clips" or "clipping" in statement:
            subprocess.Popen(r"D:\Clipping\obs-studio\bin\64bit\obs64.exe")
            speak("I've got my eye on you...")
            time.sleep(5)

		# just tells you what the time is
        elif "time" in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtime}")

        elif "who are you" or "what can you do" in statement:
            speak("I am Rasputin, your personal assistant. I am programmed to do whatever you ask me, and am able to open and give you information about many things you would usually do, but faster and without any error, yeah, I'm that good.")

        elif "who made you" or "who created you" or "who's your daddy" or "who discovered you" or "who's your maker" in statement:
            speak("Code is rarely owned, friend.")

		'''
        will search the news sites: national post, new york times, and the wall street journal.
		Of course, feel free to add more sites to open, or replace mine
		'''
        elif "news" or "whats going on in the world" or "whats new" in statement:
            news = webbrowser.open_new_tab("https://nationalpost.com"), webbrowser.open_new_tab("https://www.nytimes.com/"), webbrowser.open_new_tab("https://www.wsj.com/")
            speak("Here are some headlines from Naitonal Post, the Times, and WSJ")
            time.sleep(6)

		'''
        just puts in a search on the web if you ask it to
		for example say "search for orange-flavoured chocolate" and rasputin will search for that
		'''
        elif "search" in statement:
            statement = statement.replace("Search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

		# this uses the WolframAlpha API to answer questions that you have, check out the WolframAlpha file in my repo to learn about this
		# To use this best say something along the lines of "I want to ask something", and upon the prompt, ask away
        elif "ask" in statement:
            speak('What question do you have for me?')
            question = takeCommand()
            app_id = "WolframAlpha App ID"
            client = wolframalpha.Client("WolframAlpha App ID")
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        '''
        Here is the start of the email reminder function.
        Follow the instructions in the gmail.md file in my github for help.
        '''
        port = 465

        elif "send me a reminder" or "remind me" in statement:
            # i would advise against putting emails into code, an input is safer, trust me
            password = input("Input your email password, don't worry I won't tell anyone :)")
            # don't change this it's necessary
            smtp_server = "smtp.gmail.com"
            # do change this
            sender_email = "your email goes here"
            receiver_email = "whoever you want the reminders to go to"
            # this code block connects to the server, authenticates, and sends your reminder
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login("your email goes here", password)
                # this just pulls the variables above and uses them to send the email
                server.sendmail(sender_email, receiver_email, reminder)
                # the prompt that asks you what your reminder is
                speak('What do you want me to remind you about?')
                reminder = takeCommand()
                # here is what Rasputin's gonna email you, feel free to add him to ur contacts
                message = """ \
                Subject: {reminder}

                Someone told me to remind you:
                {reminder}

                Anyway, have a great day!

                Legitimately,
                Rasputin
                """

        '''
        ejects a thumdrive, but you have to specfy which one when given choices.
        uses the pyautogui to automate this task,
        not an absolutely perfect solution but it's windows so cmd is far from perfect.
        please note that this dismounts drives so you'll likely
        have to go into disk management when using the drive again,
        right-click it, hit change drive letter and path, then hit okay, it'll work just like normal tho.
        if you just need to get a disk tf outta there, this is pretty useful.
        '''
        elif "eject disk" in statement:
            pyautogui.keyDown('winright')
            pyautogui.press('r')
            pyautogui.keyUp('winright')
            pyautogui.write('diskpart')
            pyauotgui.press('enter')
            pyautogui.press('left')
            pyauotgui.press('enter')
            pyautogui.write('list volume')
            pyauotgui.press('enter')
            speak("What volume number do you wish to eject?")
            usbnumber = takeCommand()
            pyautogui.write('select volume {usbnumber}')
            pyautogui.press('enter')
            pyautogui.write('remove all dismount')
            pyautogui.press('enter')
            speak("Volume {usbnumber} has been ejected, all clear to remove device.")

		# what i try to ask siri to do at least once a day, don't worry i'll keep trying :)
        elif "log off" or "sign out" or "power off" or "shut down" in statement:
            speak("Ok, your pc will log of in 10 seconds, exit all applications.")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
