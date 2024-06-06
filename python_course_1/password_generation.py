from random import *


def define_rules(digit, lowercase, uppercase, punc_symbols, mislead_symbols):
    digits = '23456789'
    lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_.'
    misleading_symbols = 'i l1Lo0O'
    chars = ''
    if digit != 'n':
        chars += digits
    if lowercase != 'n':
        chars += lowercase_letters
    if uppercase != 'n':
        chars += uppercase_letters
    if punc_symbols != 'n':
        chars += punctuation
    if mislead_symbols == 'y':
        chars += misleading_symbols
    return chars


def generate_password(chars, quantity, length, ):

    for i in range(quantity):
        password = sample(chars, length)
        print(*password, sep='')


def main():
    quantity = int(input('How many passwords would you like to generate? '))
    length = int(input('How long should be password? '))
    digit = input('Enter "n" to exclude digits: ')
    lowercase = input('Enter "n" to exclude lowercase letter: ')
    uppercase = input('Enter "n" to exclude uppercase letter: ')
    punc_symbols = input('Enter "n" to exclude punctuation symbols: ')
    mislead_symbols = input('Enter "y" to use misleading symbols like "i l1Lo0O": ')

    generate_password(define_rules(digit, lowercase, uppercase, punc_symbols, mislead_symbols), quantity, length)


if __name__ == '__main__':
    main()
