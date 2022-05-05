def OpenFile():
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
		language = str(input("INPUT: "))

		for option in languageOptions:
			if (language == option):
				return open(option + ".txt", "r")

		print("INVALID INPUT -- Please try again!")
