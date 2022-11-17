file = 'guest_book.txt'

with open(file, 'w') as file_object:
    prompt = 'Please enter your name.'
    prompt += '\nEnter "q" to quit. '
    while True:
        name = input(prompt)
        if name == 'q':
            break
        else:
            message = f"Hello, {name.title()}!\n"
            print(message)
            file_object.write(message)
