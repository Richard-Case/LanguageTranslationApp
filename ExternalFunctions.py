#GETTING THE TEXT MESSAGE
def textMessageInput():
    message = str(input("Please enter your text message:\n")).upper()
    messageList = message.split()
    return messageList

#OPENING THE TRANSLATION FILE
def openFile(fileName):
    myFile = open(fileName, "r")
    return myFile