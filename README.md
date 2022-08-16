# Hangman

> This is the first project on the  AiCore portal. This is a simple hangman game, using only standard libraries.

## Milestone 1: Set up the Environment

This milestone is simply setting up the git repo. 

## Milestone 2: Ask the user for an input

First, the repo was cloned locally. The first task was to fill in the ask_letter method. A while loop was used with a 'valid_letter' flag to keep iterating over the
loop until a valid input was given. The input function was sufficient for this task, as the input was validated through the rest of the loop. Initially, the while loop
was set to:
```python
while letter == False
```
This was quickly moved away from as for every invalid input the handling would have to have an additional line of:
```python
letter = False
```
This wouldn't be an issue on a method this size, however, it would add unnecessary boilerplate if other validations were to be added.

## Milestone 3: Define the initialiser

This was more of an issue of making the code readable than of actual implementation. The docstring gave clear instructions on the typing of each parameter required in
initialiser. A list comprehension was used for self.word_guessed as it could handle variable word lengths and was easier to read than a for loop. f strings were used for
the print functions as opposed to .format as they are easier to read. f strings also have the incidental benefit of being faster, however, speed is unlikely to be an issue
as the script is not very complex.

## Milestone 4: complete the 'ask_letter' method

The bulk of this milestone was implementing the 'check_letter' method. This was checking whether the letter is present in the word, and substituting the underscores in
self.word_gussed for the guessed letter if correct. The below code checks whether the letter is in the string, extracts the indicies of the letter(s) and then substitutes
the underscores for letter in self.word_guessed.
```python
 positions = list()
        if letter.lower() in self.word:
            for i, v in enumerate(self.word):
                if letter == v:
                    positions.append(i)
            for pos in positions:
                self.word_guessed = self.word_guessed[:pos]+[f'{letter}']+self.word_guessed[pos+1:]
 ```
 This used list slicing to only substitute at the necessary indices. Implementation of this required the .lower method to be implemented on the letter to make sure capitals
 and lower case letters wouldn't be treated differently. The most obvious place to insert this was directly after the input, as it require the fewest changes to the code.
 
 
