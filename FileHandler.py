def ChooseLanguage():
	languageOptionsFile = open("LanguageOptions.txt")
	languageOptions = [""]

	#Import Language Options
	languageOptions = languageOptionsFile.readlines()
	languageOptionsFile.close()

	print("Which language would you like to translate?")
	print("OPTIONS:")

	for index in range(len(languageOptions)):
		languageOptions[index] = languageOptions[index][:-1]

	for option in languageOptions:
		print(option)

	while (True):
		language = str(input("\nINPUT: "))

		for option in languageOptions:
			if (language == option):
				return language

		print("INVALID INPUT -- Please try again!")

def OpenFile(language):
	return open(language + ".txt", "r")
