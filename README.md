
# Gclassroom-WA-bot
A simple python code which connects with google classroom api and  returns data on the list of courses and the assignments in it.


## Steps
-   Go to google cloud console
-   IAMADMIN -> Create new project
-   After Creating Enable google workspace api by going to API & SERVICES -> Library
-   Search Classroom and enable that api
-   Enable Credentials for a desktop app (For detailed explanations, VISIT [here](https://developers.google.com/classroom/guides/auth?hl=en))
- Run the app locally for authenticating and for the token.json file
-  Since the app is running on flask, run it on a cloud server and copy the public URL(I used Heroku).
-   Open [Twilio](https://twilio.com) and create an account.
-  Find the whatsapp sandbox inside it and follow the required instructions for configuring the sandbox.
-  Inside Messaging -> Settings -> Whatsapp Sandbox settings, paste the url you copied earlier.
- WOAH your bot is finished and ready to run. Type help inside the bot for the supported commands


### Things mainly used:
- FLASK - PYTHON
- Google API's
- Regex



### MISC Informations
- For running locally, type `python3 main.py`
- Also you may need to authenticate the required google account while running the app and to get the token.json file.
