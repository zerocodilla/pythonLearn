file = 'programming_poll.txt'

with open(file, 'a') as file_object:
    prompt_name = "Enter your name"
    prompt_name += "\nEnter 'q' to quit anytime. "
    prompt_message = 'Tell why you love programming? '
    while True:
        name = input(prompt_name)
        if name == 'q':
            break
        else:
            file_object.write(f"{name.title()}:\n")
        message = input(prompt_message)
        if message == 'q':
            break
        else:
            file_object.write(f"\t'{message}'.\n")

