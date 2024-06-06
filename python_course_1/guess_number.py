from random import *


def generate_num(max_number=100):
    return randint(1, max_number)


def is_valid(num: str):
    if not num.isdigit():
        return False

    return 1 <= int(num) <= 100


def game_loop(nmb: int):
    cnt = 0

    while True:
        response = input("Please, enter a number to guess? ")
        if response == 'q':
            break

        if not is_valid(response):
            continue
        response = int(response)

        if response > nmb:
            print("Too big, try again.")
            cnt += 1
        elif response < nmb:
            print("Too small, try again.")
            cnt += 1
        else:
            cnt += 1
            print(f"You are right! The number is {nmb}. Congratulations!"
                  f"\nYou guessed the number in {cnt} attempts")
            break
    repeat = input("Enter 'y' to play again. ")
    if repeat == 'y':
        main()


def main():
    print("Hello! Let's guess the number?"
          "\nEnter 'q' if you want to quit the game.")

    max_number = input("Enter the maximum number for generation: ")
    if not max_number.isdigit():
        print("Invalid value. Default maximum number 100 is taken.")
        max_number = 100

    game_loop(generate_num(int(max_number)))


if __name__ == '__main__':
    main()
