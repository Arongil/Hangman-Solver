# Hangman-Solver
Solves hangman.

Working version: https://trinket.io/library/trinkets/d64e49300f.

This is the basic psuedo-code for finding the next hangman letter, given a word list, and a word length:

Guess vowels until one is found (in the order: e, a, o, i, u, y);
Once we've found a letter(wordLength, knownLetters) {
    Create a subset of the total words with the letter(s) we've found so far, in their respective positions;
    Set our guess to the most commonly occuring letter in our subset of words, not including letters we've already found;
    Override the guess only if there is a clear English pattern, such as "q" imples "u",
    return Guess;
};

Call the same function again, updating the inputs;
Repeat until finished;
