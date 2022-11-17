
name = 'eric'
print(f'Hello {name.title()}, would you like to learn some Python today?')


name = 'eric'
print(f"{name.lower()}\nOh, excuse me\n{name.title()}\nAre you deaf??\n{name.upper()}!!!")


author_firstname = "albert"
author_lastname = "einstein"
famous_person = f"{author_firstname.title()} {author_lastname.title()}"
message = "\"A person who never made a mistake never tried anything new.\""
concat_message = f"{famous_person} once said, {message}"
print(f"{author_firstname.title()} {author_lastname.title()} once said, {message}")
print(concat_message)


name = "   firstname \n\tlastname   "
print(name)
print(name.strip())
print(name.rstrip())
print(name.lstrip())
