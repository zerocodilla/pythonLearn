from random import *

word_list = ['pineapple', 'car', 'tour']


def get_word():
    return choice(word_list).upper()


# current hangman state
def display_hangman(tries):
    stages = [  # final stage: head, body, both hands, both legs
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # head, body, both hands, one leg
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # head, body, both hands
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # head, body, one hand
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # head, body
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # head
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # initial state
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    word_completion = ['_' for _ in word]  # word pattern
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's guess the word!")
    print(display_hangman(tries))
    print(*word_completion, sep='')

    while not guessed:
        s = input("Enter a letter or a word to guess: ").upper()
        while not s.isalpha():
            s = input("Unexpected result. Please enter a letter or a word to guess: ").upper()
        while s in guessed_letters or s in guessed_words:
            s = input("You already tried this. Please enter a letter or a word you didn't try: ").upper()

        if len(s) == 1:
            guessed_letters.append(s)
            if s in word:
                for letter in guessed_letters:
                    for i in range(len(word)):
                        if letter == word[i]:
                            word_completion[i] = letter
                print(*word_completion, sep='')
            else:
                print(*word_completion, sep='')
                tries -= 1

        else:
            guessed_words.append(s)
            if s == word:
                word_completion = s
            else:
                print(*word_completion, sep='')
                tries -= 1

        if ''.join(word_completion) == word:
            print("Congratulations! You guessed the word.")
            break
        if tries == 0:
            print(display_hangman(tries))
            print(f"You have used all tries. The word was {word}.")
            break
        print(display_hangman(tries))


def main():
    while True:
        play(get_word())
        repeat = input("Enter 'y' if you want to play again, or 'q' to quit ")
        if repeat == 'q':
            break


if __name__ in '__main__':
    main()
