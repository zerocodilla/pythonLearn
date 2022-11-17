file = 'guest.txt'

with open(file, 'w') as file_object:
    name = input("Please enter your name: ")
    file_object.write(name)