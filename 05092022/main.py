# import random
# import string

# hiddenLetter = random.choice(string.ascii_letters)

# atempts = 0

# while True:
# 	userInput = input("enter a letter: ")

# 	if userInput == hiddenLetter:
# 		print("letter '{}' is the correct letter".format(userInput))
# 		break
# 	else:
# 		print("letter '{}' is not the correct letter".format(userInput))
# 		atempts+=1

# print("it took '{}' atempts".format(atempts))

# wordList = list("qwerty")

# for i in range(len(wordList)):
# 	if wordList[i] != "e":
# 		wordList[i] = "*"

# print("".join(wordList))

import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()
print(WORDS)

