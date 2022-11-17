file = 'learning_python.txt'

with open(file) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print('\n')
with open(file) as file_object:
    for line in file_object:
        print(line.rstrip())

print('\n')
with open(file) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print('\n10.2')
with open(file) as file_object:
    lines = file_object.readlines()

lp_string = ''
for line in lines:
    lp_string = line.rstrip()
    lp_string = lp_string.replace('Python', 'Ruby')
    print(lp_string)