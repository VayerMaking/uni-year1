from random_word import RandomWords

r = RandomWords()

atemptsLeft = 10

wordToGuess = r.get_random_word()
guessAtempts = []
leftToGuess = list(wordToGuess)
wordToDisplay = list("_" * len(wordToGuess))

while True:

	if atemptsLeft == 10:
		print("\033c", end="")

	print(
		f"""
		.______   .______       __   _______   _______  _______ 
		|   _  \  |   _  \     |  | |       \ /  _____||   ____|
		|  |_)  | |  |_)  |    |  | |  .--.  |  |  __  |  |__   
		|   _  <  |      /     |  | |  |  |  |  | |_ | |   __|  
		|  |_)  | |  |\  \----.|  | |  '--'  |  |__| | |  |____ 
		|______/  | _| `._____||__| |_______/ \______| |_______|
                                                        
		"""
	)

	print("word to guess: " + " ".join(wordToDisplay))
	print("---------------------------------------------------"+ "".join("-----" * len(guessAtempts)))
	print("|-- previous guesses : {} --|--  atempts left: {} --|".format(guessAtempts, atemptsLeft))
	print("---------------------------------------------------"+ "".join("-----" * len(guessAtempts)))

	userInput = input("guess a letter: ")

	if userInput in wordToGuess:
		print("letter '{}' is the correct letter".format(userInput))
		leftToGuess = list(filter((userInput).__ne__, leftToGuess))

		for i in range(len(wordToGuess)):
			if wordToGuess[i] == userInput:
				wordToDisplay[i] = userInput
	else:
		print("letter '{}' is not the correct letter".format(userInput))
		atemptsLeft -= 1
	
	if atemptsLeft <= 0:
		print("no more atempts left")
		print("game over")
		break

	if len(leftToGuess) == 0:
		print("you guessed the word [ {} ]".format(wordToGuess))
		break

	guessAtempts.append(userInput)

	print("\033c", end="")

