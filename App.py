#Write a program that will take a text meggage and translate it into words that your grandparents could understand.
#For example: "So funny LOL ROTFL" would be converted to "So funny LAUGHING OUT LOUD ROLLING ON THE FLOOR LAUGHING."

#For this scenario we will assume that we have a file that lists all the text message abbreviations and translations.

##############

#Importing my external function files
import FileHandler
import Translator

myFile = FileHandler.OpenFile()

while (True):
	translatedMessage = Translator.TranslateMessage(myFile)
	print(translatedMessage)
	userInput = str(input("Would you like to translate another word? (Y/N) -- "))

	if (userInput[0].upper() == 'N'):
		break

input("Press ENTER to exit.")
myFile.close()
