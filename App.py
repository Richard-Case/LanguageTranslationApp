#Indicates that this file is to be run within the terminal.
#!/usr/bin/env python3

##############

#Importing my external function files
import FileHandler
import Translator
import Utilities

while (true)
	language = FileHandler.ChooseLanguage()
	
	while (True):
		translationFile = FileHandler.OpenFile(language)
		translatedMessage = Translator.TranslateMessage(translationFile)
		print(translatedMessage)
		userInput = str(input("\nWould you like to translate another word? (Y/N) -- "))
	
		if (userInput[0].upper() == 'N'):
			break
	
	userInput = str(input("\nWould you like to translate a different language? (Y/N) -- "))
	
	if (userInput[0].upper() == 'N'):
		break
	
input("\nPress ENTER to exit.")
translationFile.close()

Utilities.ClearTerminal()
