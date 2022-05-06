#!/usr/bin/env python3

#Write a program that will take a text meggage and translate it into words that your grandparents could understand.
#For example: "So funny LOL ROTFL" would be converted to "So funny LAUGHING OUT LOUD ROLLING ON THE FLOOR LAUGHING."

#For this scenario we will assume that we have a file that lists all the text message abbreviations and translations.

##############

#Importing my external function files
import FileHandler
import Translator
import Utilities

language = FileHandler.ChooseLanguage()

while (True):
	translationFile = FileHandler.OpenFile(language)
	translatedMessage = Translator.TranslateMessage(translationFile)
	print(translatedMessage)
	userInput = str(input("\nWould you like to translate another word? (Y/N) -- "))

	if (userInput[0].upper() == 'N'):
		break

input("\nPress ENTER to exit.")
translationFile.close()

Utilities.ClearTerminal()
