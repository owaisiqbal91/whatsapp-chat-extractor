import os
import re
from datetime import datetime
import codecs

from src.db.message import Message
from src.db.message import addMessage

user = "Owais"

def parseFile(fileName):
    def isValidMsg(msgToCheck):
        return msgToCheck and not msgToCheck == "<Media omitted>" and len(msgToCheck) < 500

    messagesList = list()

    def addMessage(time, author, group, msg):
        message = Message(time, author, group, msg, len(msg), len(msg.split()))
        messagesList.append(message)

    isGroup = True
    with codecs.open(fileName, mode='r', encoding='utf-8') as f:
        group = re.search('WhatsApp Chat with (.+?)\\.txt', os.path.basename(fileName)).group(1)
        author = ""
        for line in f:
            # 9/21/15, 1:46 PM - Anindo: Suldeee
            result = re.search('(\d{1,2}/\d{1,2}/\d{2}), (\d{1,2}:\d{1,2} [AP]M) - (.+): (.*)', line)
            if (result):
                # if new msg and there is already a current author, save the msg before parsing for the new one
                if (author and isValidMsg(msg)):
                    addMessage(time, author, group, msg)
                time = datetime.strptime(str(result.group(1)) + "|" + str(result.group(2)), "%m/%d/%y|%I:%M %p")
                author = result.group(3)
                msg = result.group(4)
                if(not author == user):
                    isGroup = not author == group
            # if no match but there is a current author
            elif (author):
                addedMsgResult = re.search('(\d{1,2}/\d{1,2}/\d{2}), (\d{1,2}:\d{1,2} [AP]M) - (.+) added (.*)', line)
                if(addedMsgResult is None):
                    msg += line
        # append the last msg
        if (author and isValidMsg(msg)):
            addMessage(time, author, group, msg)

    #since default isGroup in message object is True, looping over and setting the flag only if it is False
    if(not isGroup):
        for message in messagesList:
            print(message.chatgroup)
            message.isGroup = isGroup

    return messagesList

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

chatFiles = [f for f in listdir_fullpath("../resources") if os.path.basename(f).startswith("WhatsApp Chat with ")]
messagesList = list()
for f in chatFiles:
    messagesList.extend(parseFile(f))
# fileName = '../resources/WhatsApp Chat with Anindo.txt'
addMessage(messagesList)
print(len(messagesList))