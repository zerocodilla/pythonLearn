# 8.1.
def display_message():
    """Print one sentence telling everyone what I am learning about in this chapter."""
    print("I am learning functions in this chapters.")


display_message()


# 8.2.
def favorite_book(title):
    """Print a message about favorite book."""
    print(f"\nOne of my favorite books is {title.title()}.")


favorite_book('anna karenina')


# 8.3.
def make_shirt(size, text):
    """Function accepts a size and the text of a message that should be printed on the shirt."""
    print(f"\nYour size is {size}")
    print(f"The text you want to print on t-shirt is '{text}'")


make_shirt('M', 'More Woman in Tech!')


# 8.4.
def make_shirt(text='I love Python', size='L'):
    """Function accepts a size and the text of a message that should be printed on the shirt."""
    print(f"\nYour size is {size}")
    print(f"The text you want to print on t-shirt is '{text}'")


make_shirt()
make_shirt(size='M')
make_shirt(text='Love is everywhere')


# 8.5
def describe_city(city, country='bulgaria'):
    """Print country of the city."""
    print(f"{city.title()} is in {country.title()}.")


describe_city('sofia')
describe_city('berlin', 'germany')
describe_city('paris', 'france')


# 8.6
def city_country(city, country):
    """Print city and its country."""
    message = f"{city.title()}, {country.title()}"
    return message


pair = city_country('belgrade', 'serbia')
print(pair)
pair = city_country('sofia', 'bulgaria')
print(pair)
pair = city_country('moscow', 'russia')
print(pair)


# 8.7
def make_album(artist, name, tracks=''):
    """Builds a dictionary describing a music album."""
    album = {'artist_name': artist, 'album_name': name}
    if tracks:
        album['tracks'] = tracks
    return album


album_0 = make_album('jack d', 'inspiration')
album_1 = make_album('rammstein', 'young')
album_2 = make_album('sting', 'infinity')
print(album_1, album_0, album_2)
album_3 = make_album('alexa', 'hello', '9')
print(album_3)


# 8.8
def make_album(artist, name, tracks=''):
    """Builds a dictionary describing a music album."""
    album = {'artist_name': artist, 'album_name': name}
    if tracks:
        album['tracks'] = tracks
    return album


while True:
    print("\nEnter album information."
          "\nEnter 'q' to quit.")
    artist = input("Artist name: ")
    if artist == 'q':
        break

    name = input("Album title: ")
    if name == 'q':
        break

    album = make_album({artist}, {name})
    print(album)


# 8.9
def show_magicians(magicians):
    """Print magicians list."""
    for magician in magicians:
        print(magician.title())


magicians = ['copperfield', 'wagner', 'carlson']
show_magicians(magicians)


# 8.10
def make_great(magicians, great_magicians):
    """Move each magician to another list to make great."""
    while magicians:
        great_magician = magicians.pop()
        print(f"Making {great_magician.title()} great.")
        great_magicians.append(great_magician)


def show_magicians(great_magicians):
    """Print magicians list."""
    for great_magician in great_magicians:
        print(f"{great_magician.title()} the Great")


magicians = ['copperfield', 'wagner', 'carlson']
great_magicians = []
make_great(magicians, great_magicians)
show_magicians(great_magicians)


# 8.11
def make_great(magicians, great_magicians):
    """Move each magician to another list to make great."""
    while magicians:
        great_magician = magicians.pop()
        print(f"Making {great_magician.title()} great.")
        great_magicians.append(great_magician)


def show_magicians(great_magicians):
    """Print magicians list."""
    for great_magician in great_magicians:
        print(f"{great_magician.title()} the Great")


magicians = ['copperfield', 'wagner', 'carlson']
great_magicians = []
make_great(magicians[:], great_magicians)
show_magicians(great_magicians)
print(magicians)
print(great_magicians)


# 8.12
def make_sandwich(*items):
    """Print a summary of the sandwich that is being ordered."""
    print("Your ordered sandwich with the following items:")
    for item in items:
        print(item)


make_sandwich('cheese', 'tomatoes', 'mushrooms')
make_sandwich('ham')
make_sandwich('cheese', 'salmon')


# 8.13
def build_profile(first, last, **user_info):
    """Build dictionary with user info."""
    user_info['first_name'] = first
    user_info['last_mame'] = last
    return user_info


user_profile = build_profile('john', 'Ivanov', location='Bulgaria', profession='Unit Manager', language=['ru', 'eng'])
print(user_profile)


# 8.14
def car_info(manufacturer, model, **car_info):
    """Build dictionary with car info."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)
