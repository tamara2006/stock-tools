import highLowData 
import notifyemails 
import json

with open('userInput.json', 'r') as openfile: #read userInput JSON
    userDictionary = json.load(openfile)

apikeyVar = userDictionary["Apikey"] #retreive apikey

listOfSymbols = userDictionary["stock symbols"] #retrieve desired stocks 

sendToEmail = userDictionary["email"]

notificationState = userDictionary["Email Alert"]

alertPercentage = userDictionary["Percentage to alert"]

bigResult = ""
for symbolVar in listOfSymbols:
    p1 = highLowData.HighLow(symbolVar, apikeyVar, alertPercentage)
    msg = p1.data()
    if msg != "None": 
        bigResult += str(msg)

if notificationState == True and bigResult != "":
    finalMessage =  """Subject: Stock Alert


""" + bigResult
    p2 = notifyemails.EmailNotification(sendToEmail)
    p2.sendEmail(finalMessage)
    print("Favourable conditions, email is sent!") 


