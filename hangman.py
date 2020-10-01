import random

def playAgain():
	print("Do you want to play again? [Y/n]")
	again = input(">")
	
	yes = ["y", "yes", ""]
	no = ["n", "no"]
	again = again.lower()
	
	if again in yes:
		main()
	elif again in no:
		exit()
	else:
		print("That is not an option. Please try again.")
		playAgain()

def winExit(word2Guess, guesses):
	print(f"You guessed the word {word2Guess} in {guesses} guesses!")
	playAgain()

def failExit(word2Guess, maxBadGuesses):
	print(f"You failed to guess the word \"{word2Guess}\" within {maxBadGuesses} guesses!")
	print("You lose!")
	playAgain()

def getWords():
	with open("wordlist.txt", 'r') as wordlist:
		words = wordlist.readlines()
	return words

def main():
	try:
		words = getWords()
	except:
		words = ["jazz", "neatnesses", "overload", "nah"]
	word2Guess = random.choice(words).upper()
	print(str(len(word2Guess)) +  " _" * len(word2Guess))

	incorrectLetters = []
	correctLetters = []
	lettersGuessed = incorrectLetters + correctLetters
	guessed = False
	goodGuesses = 0
	maxBadGuesses = 6
	badGuesses = 0

	while guessed == False:
		if maxBadGuesses <= badGuesses:
			failExit(word2Guess, maxBadGuesses)

		if incorrectLetters != []:
			print("Incorrect letters guessed: {}".format(" ".join(incorrectLetters)))

		if correctLetters != []:
			tempW2G = word2Guess
			for letter in word2Guess:
				if letter not in correctLetters:
					tempW2G = tempW2G.replace(letter, " _")

			print("Correct letters guessed: {}\n".format(tempW2G))

		if len(correctLetters) == len("".join(set(word2Guess))):
			guessed = True
			winExit(word2Guess, guesses)

		letter = input("Guess a letter, any letter >")
		letter = letter.upper()

		if len(letter) == 1 and letter != " " and letter in word2Guess:
			correctLetters.extend(letter)
			print(f"Yes, {letter} is in the word.\n")
			goodGuesses += 1
		elif len(letter) == len(word2Guess) and letter == word2Guess:
			goodGuesses += 1
			winExit(goodGuesses)
		elif len(letter) > 1 and letter not in exit:
			print("Nice try, cheater!\nOne letter at a time, please.\n")
		else:
			if not letter.isalpha():
				print(f"So you think you're a funny guy, huh? We both know {letter} isn't a letter!\n")
			if letter in incorrectLetters:
				print(f"Hey, you already guessed {letter}!\n")
			if letter.isalpha() and letter not in incorrectLetters:
				incorrectLetters.extend(letter)
				print(f"No, {letter} is not in the word.\n")
				badGuesses += 1
				print(f'You have {maxBadGuesses - badGuesses} guesses left.\n')

main()