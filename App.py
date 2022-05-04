#Write a program that will take a text meggage and translate it into words that your grandparents could understand.
#For example: "So funny LOL ROTFL" would be converted to "So funny LAUGHING OUT LOUD ROLLING ON THE FLOOR LAUGHING."

#For this scenario we will assume that we have a file that lists all the text message abbreviations and translations.

##############

import FileHandler			#Importing my external function file
#import Translator
allTranslations = []		#Declaring a list to hold the translations.
spaceIndex = 0				#Declaring a variable to hold an index value to use in loops which concatenate strings together.

#Then I need to retrieve the first abbreviation and translation and put them in a list.
myFile = FileHandler.openFile()

#I need the user to enter a text message, and I need to turn that string into a list.
textList = FileHandler.textMessageInput()

for line in iter(myFile):
    translationIndex = 2
    textIndex = 0

    wordsInLine = line.split()
	print(wordsInLine)	#TEST
    lengthOfList = len(wordsInLine)

    #Then I need to check the text message against index 0 in the list.
    for word in textList:
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
            textList[textIndex] = override
        textIndex += 1

        #Then I need to retrieve the next abbreviation and translation and replace the current values of the list with those, and run the same check and replace again.

spaceIndex = 0      #Resetting spaceIndex to 0, in order to use it again.

#Now convert the current translated list into a string to print to the console.
for value in textList:
    if spaceIndex == 0:
        translatedMessage = value
    else:
        translatedMessage = translatedMessage + " " + value
    spaceIndex += 1

#Print the string to the console.
print(translatedMessage)
input("Press ENTER to exit.")

#Close the file.
myFile.close()
