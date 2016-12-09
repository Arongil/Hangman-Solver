# This will contain the function that will determine the, statistically, best next letter to pick, for the given word and known letters.

# Change to match the current word length
wordLength = 5
# This list will reflect everything we know about the word so far.
knownLetters = []
# This list will contain all letters not in the word.
knownNonLetters = []

vowels = ["e", "a", "o", "i", "u", "y"]
currentVowel = 0

def nextLetter():
  # If we know nothing about the word, we will guess vowels, until we find one.
  if len(knownLetters) == 0:
    global currentVowel
    currentVowel += 1
    return vowels[currentVowel - 1]
  return "temporary return"

# The nextLetter() function will slowly fill out this list.
word = ["" for i in xrange(wordLength)]

foundWord = False
while not foundWord:
  nextGuess = nextLetter()
  ######################
  # Temporary
  if nextGuess == "temporary return":
    foundWord = True
  # Temporary
  ######################
  print "'" + nextGuess + "' is the guess for the next letter."
  correct = raw_input("Was the letter correct? [y/n]")
  if correct == "y":
    position = int(raw_input("Where in the word was the letter ('r' in 'word' is at '3', for example)? [integer]"))
    # knownLetters is made up of arrays, with the 0th element as the letter, and the first as position.
    knownLetters.append([nextGuess, position])
  else:
    # knownNonLetters is just an array of letters that we have checked, that aren't in the word.
    knownNonLetters.append(nextGuess)

print "\nCode Complete."
