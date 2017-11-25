#GETTING THE TEXT MESSAGE
def textMessageInput():
    message = str(input("Please enter your text message:\n")).upper()
    messageList = message.split()
    return messageList

#OPENING THE TRANSLATION FILE
def openFile():
    myFile = open("Text Speak.txt", "r")
    return myFile