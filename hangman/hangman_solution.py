'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random
# from turtle import position
# able to implement graphics but had to import more of turtle
import turtle

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(list(self.word)))
        self.num_lives = num_lives
        self.list_letters = list()
        print(f'The mystery word has {len(self.word)} characters')
        print(f'{self.word_guessed}')


    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        positions = list()
        if letter in self.word:
            for i, v in enumerate(self.word):
                if letter == v:
                    positions.append(i)
            for pos in positions:
                self.word_guessed = self.word_guessed[:pos]+[f'{letter}']+self.word_guessed[pos+1:]
            print(f'Nice! {letter} is in the word')
            print(f'{self.word_guessed}')
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {letter} is not in the word')
            print(f'You have {self.num_lives} lives remaining')


    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        valid_letter = False
        while valid_letter == False:
            letter = input('Guess a letter: ').lower()
            if len(letter) != 1:
                print('Please, enter just one character')
                continue
            if letter in self.list_letters:
                print(f"{letter} was already tried")
                continue
            self.list_letters.append(letter)
            self.check_letter(letter)
            valid_letter = True

        
def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    screen = turtle.getscreen()
    pen = turtle.Turtle()
    while game.num_lives > 0:
        init_lives = game.num_lives
        game.ask_letter()
        if game.num_letters == 0:
            print('Congratulations, you won!')
            break
        if game.num_lives != init_lives:
            turtle_drawing(s = screen, t = pen, lives = game.num_lives)
    if game.num_lives == 0:
        print(f'You ran out of lives. The word was {game.word}')

def turtle_drawing(s, t, lives: int) -> None:
    turtle.delay(50)
    if lives == 4:
        t.forward(100)
        t.backward(50)
    elif lives == 3:
        t.left(90)
        t.forward(200)
    elif lives == 2:
        t.left(90)
        t.forward(50)
    elif lives == 1:
        t.left(90)
        t.forward(10)
    elif lives == 0:
        t.right(90)
        t.circle(25, 540)
        t.right(90)
        t.forward(70)
        t.backward(60)
        t.left(45)
        t.forward(40)
        t.backward(40)
        t.right(90)
        t.forward(40)
        t.backward(40)
        t.left(45)
        t.forward(60)
        t.left(45)
        t.forward(40)
        t.backward(40)
        t.right(90)
        t.forward(40)


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
