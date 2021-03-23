# Using Gmail to Send Reminders
### Let Rasputin tell you to get your ~~$%&#~~ Together

I used [this tutorial](https://realpython.com/python-send-email/) to learn how to do this btw.

This can be a little touchy security-wise if you don't go about it safely. 
So, here is how you can use the gmail OAuth2 authrization framework to keep yourself safe and still get Rasputin's emails. 
Before we hop in, the things we'll need to do are first to get gmail authorization, then setup a secure SMTP connection, and lastly make sure the email gets to you.
But don't worry, the code is all handled, all you've gotta do is put together the codes and tell Rasputin what to send you!

### Getting Gmail Ready
1. Create or Sign into a gmail account (could be more secure to create a new one, with a different pass)
2. Visit [Google's API page](https://developers.google.com/gmail/api/quickstart/python) and hit the "Enable the Gmail API" button
3. Save the resulting credentials.json file to wherever you stored rasputin.py and the rest of the files
4. Activate Rasputin's virtual environment, then "pip install --upgrade google-api-python-client google-auth-httplib2 google-oauthlib" (this will download and update the necessary tools to send emails)
5. Terminal: "python quickstart.py" (will run a python script form google to open a webpage for authentication)
6. If the webpage looks legit, accept to authorize
7. Onto the next step!
