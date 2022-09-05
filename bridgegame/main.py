from random_word import RandomWords

r = RandomWords()

atempts = 0
atemptsLeft = 10

wordToGuess = r.get_random_word()
guessAtempts = []
leftToGuess = list(wordToGuess)
wordToDisplay = list("_" * len(wordToGuess))

print(wordToGuess)

while True:
	print("word to guess: " + "".join(wordToDisplay))
	print("previous guesses: {}".format(guessAtempts))
	print(leftToGuess)
	userInput = input("guess a letter: ")

	if userInput in wordToGuess:
		print("letter '{}' is the correct letter".format(userInput))
		leftToGuess = list(filter((userInput).__ne__, leftToGuess))
		# wordToDisplay.insert(wordToGuess.index(userInput), userInput)
		wordToDisplay[wordToGuess.index(userInput)] = userInput
	else:
		print("letter '{}' is not the correct letter".format(userInput))
	
	if atemptsLeft <= 0:
		print("no more atempts left")
		break

	if len(leftToGuess) == 0:
		print("you guessed the word!")
		break

	guessAtempts.append(userInput)
	atempts+=1


print("it took '{}' atempts".format(atempts))