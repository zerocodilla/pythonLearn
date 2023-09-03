# 6.1
men = {'first_name': 'john', 'last_name': 'ivanov', 'age': '39', 'fav_language': 'ruby', 'city': 'istanbul'}
print(men['first_name'].title())
print(men['last_name'].title())
print(men['age'])
print(men['city'].title())
print(men['fav_language'].upper())

# 6.2
favorite_numbers = {
    'yana': 13,
    'laura': 9,
    'natasha': 1,
    'vera': 8
}
print(f"Yana's favorite number is {favorite_numbers['yana']}")
print(f"laura's favorite number is {favorite_numbers['laura']}")
print(f"Natasha's favorite number is {favorite_numbers['natasha']}")
print(f"Vera's favorite number is {favorite_numbers['vera']}")

# 6.3
print(6.3)
terms = {
    'tuple': 'is an ordered, immutable collection of data in ().',
    'list': 'is an ordered, mutable collection of objects in [].',
    'dictionary': 'key-value, in {}.',
    'if_statement': 'is condition.',
    'loop': 'is used for iterating over a sequence.'
}
print(f"\nTuple {terms['tuple']}")
print(f"\nList {terms['list']}")
print(f"\nDictionary {terms['dictionary']}")
print(f"\nIf-statement {terms['if_statement']}")
print(f"\nLoop {terms['loop']}")

# 6.4
print('\n6.4')
for term, meaning in terms.items():
    print(f'{term.title()} {meaning}')

terms['variable'] = 'is a place in computer memory with an assigned name'
terms['print()'] = 'is a basic Python functions'
terms['for loop'] = 'loops allow us to iterate over sequences'
for term, meaning in terms.items():
    print(f'{term.title()} {meaning}')

# 6.5
print('\n6.5')
rivers = {'nile': 'egypt', 'danube': 'serbia', 'rhine': 'germany'}
for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}')
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())

# 6.6
print('\n6.6')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
candidates = ['john', 'lera', 'markus', 'jen', 'phil', 'sarah', 'edward']
for name in candidates:
    if name not in favorite_languages.keys():
        print(f'-{name.title()} please, take a pool')
    else:
        print(f'+{name.title()} thank you for taking the pool')

# 6.7.
men_0 = {'first_name': 'john', 'last_name': 'ivanov', 'age': '39', 'fav_language': 'ruby', 'city': 'istanbul'}
men_1 = {'first_name': 'john', 'last_name': 'ivanov', 'age': '39', 'fav_language': 'ruby', 'city': 'istanbul'}
men_2 = {'first_name': 'john', 'last_name': 'ivanov', 'age': '39', 'fav_language': 'ruby', 'city': 'istanbul'}
people = [men_0, men_1, men_2]
for men in people:
    print(men)

# 6.8
chappy = {
    'type': 'cat',
    'owner': 'john'
}
felix = {
    'type': 'cat',
    'owner': 'laura'
}
angel = {
    'type': 'cat',
    'owner': 'unknown'
}
pets = [chappy, felix, angel]
for pet in pets:
    print(pet)

# 6.9
favorite_restaurants = {
    'john': ['crystal', 'royal thai', 'mcdonald\'s'],
    'laura': ['spaghetti', 'royal thai'],
    'amely': ['altruist', 'walk']
}
for name, restaurants in favorite_restaurants.items():
    print(f"{name.title()}'s favorite restaurants are:")
    for restaurant in restaurants:
        print(f"\t{restaurant.title()}")

# 6.10
favorite_numbers = {
    'yana': [13, 19],
    'laura': [9, 0],
    'natasha': [1, 7],
    'vera': [8, 4]
}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")


# 6.11
cities = {
    'sofia': {
        'country': 'bulgaria',
        'population': 1200000,
        'fact': 'mountains around'
    },
    'novosibirsk': {
        'country': 'russia',
        'population': 1500000,
        'fact': '100 years old'
    },
    'solingen': {
        'country': 'germany',
        'population': 159360,
        'fact': 'famous for scissors and knifes production'
    }
}
