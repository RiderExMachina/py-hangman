# py-hangman
My take on Hangman in Python.

It can import from a wordlist, so long as it's in the same directory and named "wordlist.txt". There are currently 4 words in the built-in wordlist.

This is a very simple game, sample output when running:

```
> python3 hangman.py 
10 _ _ _ _ _ _ _ _ _ _
Guess a letter, any letter >t
Yes, T is in the word.

Correct letters guessed:  _ _ _T _ _ _ _ _ _

Guess a letter, any letter >l
No, L is not in the word.

You have 5 guesses left.

Incorrect letters guessed: L
Correct letters guessed:  _ _ _T _ _ _ _ _ _

Guess a letter, any letter >m
No, M is not in the word.

You have 4 guesses left.

Incorrect letters guessed: L M
Correct letters guessed:  _ _ _T _ _ _ _ _ _

Guess a letter, any letter >n
Yes, N is in the word.

Incorrect letters guessed: L M
Correct letters guessed: N _ _TN _ _ _ _ _

Guess a letter, any letter >p
No, P is not in the word.
Incorrect letters guessed: L M
Correct letters guessed:  _ _ _T _ _ _ _ _ _

You have 3 guesses left.

Incorrect letters guessed: L M P
Correct letters guessed: N _ _TN _ _ _ _ _

Guess a letter, any letter >
```
