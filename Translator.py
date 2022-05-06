def MessageToTranslate():
	message = str(input("\nPlease enter your text message:\n")).upper()
	return message.split()

def TranslateMessage(translationFile):
	spaceIndex = 0
	messageList = MessageToTranslate()

	for line in iter(translationFile):
	    translationIndex = 2
	    textIndex = 0

	    wordsInLine = line.split()
	    lengthOfList = len(wordsInLine)

	    #Then I need to check the text message against index 0 in the list.
	    for word in messageList:
	        spaceIndex = 0
	        #If the text message contains that value...
	        if wordsInLine[0] == word:
	            while translationIndex < lengthOfList:
	                if spaceIndex == 0:
	                    override = wordsInLine[translationIndex]
	                else:
	                    override = override + " " + wordsInLine[translationIndex]

	                spaceIndex += 1
	                translationIndex += 1

	            #I need to replace it with the associated translation.
	            messageList[textIndex] = override
	        textIndex += 1

	        #Then I need to retrieve the next abbreviation and translation and replace the current values of the list with those, and run the same check and replace again.

	spaceIndex = 0

	#Now convert the current translated list into a string to print to the console.
	for value in messageList:
	    if spaceIndex == 0:
	        translatedMessage = value
	    else:
	        translatedMessage = translatedMessage + " " + value
	    spaceIndex += 1

	return translatedMessage
