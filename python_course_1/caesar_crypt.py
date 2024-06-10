def encrypt(text, step, alphabet):
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                print(alphabet[(alphabet.index(text[i].lower()) + step) % len(alphabet)].upper(), end='')
            else:
                print(alphabet[(alphabet.index(text[i]) + step) % len(alphabet)], end='')
        else:
            print(text[i], end='')



def main():
    eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rus_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    print("Welcome to the Caesar encryption App!"
          "It can encrypt or decrypt Russian or English text.")
    text = input("Please enter text for de/encryption: ")
    # direction = input("Enter 'e' to encrypt or 'd' to decrypt: ")
    step = int(input("Enter step. Negative (<0) for decryption or Positive (>0) for encryption: "))
    if text[0].lower() in eng_alphabet:
        alphabet = eng_alphabet
    else:
        alphabet = rus_alphabet

    encrypt(text, step, alphabet)


if __name__ == '__main__':
    main()
