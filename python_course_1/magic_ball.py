from random import *


def game_loop():
    answers = ['Undoubtedly', 'It seems to me - yes', 'It’s unclear, try again', 'Don’t even think',
               'Most likely', 'Ask later', 'My answer is no',
               'No doubts', 'Good prospects', 'Better not to tell', 'According to my data - no'
               'Definitely yes', 'Signs say yes', 'It’s impossible to predict now', 'Prospects are not very good',
               'You can be sure', 'Yes', 'Concentrate and ask again', 'Very doubtful']
    while True:
        input("What is your question? ")
        print(choice(answers))

        repeat = input("Enter 'y' if you want to ask more. ")
        if repeat != 'y':
            print("Come back if you have more questions. Bye!")
            break


def main():

    print("Hello, my friend! I am a magic destiny ball. I know all answers.")
    user = input("What is your name? ")
    print(f"Welcome, {user}!")

    game_loop()


if __name__ == '__main__':
    main()