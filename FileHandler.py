#GETTING THE TEXT MESSAGE
def textMessageInput():
    message = str(input("Please enter your text message:\n")).upper()
    messageList = message.split()
    return messageList

#OPENING THE TRANSLATION FILE
def openFile():
	userInput = ""
	#runLoop = True

	while (True):
		fileName = str(input("Please enter the name of the file you wish to use: "))
		print("The file name you've entered is: ", fileName)
		userInput = str(input("Is this correct? (Y/N) -- "))

		if (userInput[0].upper() == Y):
			break

	if (fileName[-4:] != ".txt"):
		fileName += ".txt"
		print("Filename corrected to: ", fileName)

    return open(fileName, "r")
