from easygui import *
file =  open(".env", "w")

msg = "Type in your discord bot and server credentials"
title = ".env configuration"
fieldNames = ["Your Discord bot's private token", "Server ID", "Channel ID to where the bot interactions take place"]
fieldValues = []
fieldValues = multenterbox(msg, title, fieldNames)

stuudiumMsg = "Your Stuudium credentials"
stuudiumTitle = "Stuudium logon credentials"
stuudiumFieldNames = ["Stuudium base URL", "Stuudium username", "Stuudium password", "Stuudium student id"]
stuudiumFieldValues = []
stuudiumFieldValues = multenterbox(stuudiumMsg, stuudiumTitle, stuudiumFieldNames)

while True:
    if fieldValues == None: break
    errmsg = ""
    for i in range(len(fieldNames)):
      if fieldValues[i].strip() == "":
        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "": break # no problems found
    fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
    if stuudiumFieldValues == None: break
    errmsg2 = ""
    for j in range(len(stuudiumFieldNames)):
      if stuudiumFieldValues[j].strip() == "":
        errmsg2 = errmsg2 + ('"%s" is a required field.\n\n' % stuudiumFieldValues[i])
    if errmsg2 == "": break # no problems found
    stuudiumFieldValues = multenterbox(errmsg2, stuudiumTitle, stuudiumFieldNames, stuudiumFieldValues)

file.write("#.env\n")
file.write("DISCORD_ TOKEN = " + fieldValues[0] + "\n")
file.write("GUILD_ID = " + fieldValues[1] + "\n")
file.write("CHANNEL_ID = " + fieldValues[2] + "\n")
file.write("STUUDIUM_BASE_URL= " + stuudiumFieldValues[0] + "\n")
file.write("STUUDIUM_USERNAME= " + stuudiumFieldValues[1] + "\n")
file.write("STUUDIUM_PASSWORD= " + stuudiumFieldValues[2] + "\n")
file.write("STUUDIUM_STUDENT_ID= " + stuudiumFieldValues[3] + "\n")
file.close()