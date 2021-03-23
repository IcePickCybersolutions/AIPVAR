# Using WolframAlpha to Answer the Hard Questions
### Setting up a Third-party API for rasputin.py

To begin, what this does is uses an application programming interface to return answers to complex questions using the machine intelligent WolframAlpha platform. 
WolframAlpha itself is an AI system built to answer questions in various areas, almost exclusively sciencey stuff tho. 

In the creators' own words:
> Compute expert-level answers using Wolfram’s breakthrough 
> algorithms, knowledgebase and AI technology.

In order to use this program you have to aquire an app id, which you can get from [the WolframAlpha site.](https://www.wolframalpha.com/)

Here's how you'll want to go about that:
1. Create or Sign In
2. Use the dropdown on your login, and navigate to "My Apps (API)"
3. Sign in and copy down your App ID
4. Paste the code into where it says "WolframAlpha App ID" in the rasputin.py file
5. Ask Rasputin some sciency questions

### Getting Gmail Ready
1. Create or Sign into a gmail account (could be more secure to create a new one, with a different pass)
2. Visit [Google's API page](https://developers.google.com/gmail/api/quickstart/python) and hit the "Enable the Gmail API" button
3. Save the resulting credentials.json file to wherever you stored rasputin.py and the rest of the files
4. Activate Rasputin's virtual environment, then "pip install --upgrade google-api-python-client google-auth-httplib2 google-oauthlib" (this will download and update the necessary tools to send emails)
5. Terminal: "python quickstart.py" (will run a python script form google to open a webpage for authentication)
6. If the webpage looks legit, accept to authorize
7. Onto the next step!
