# 3.1 names of my friends
names = ['natasha', 'maria', 'marcia', 'darina', 'daria']
print(names[0].title())
print(names[-1].title())
print(names[1].title())
print(names[2].title())
print(names[-2].title())

# 3.2 message to friend
names = ['natasha', 'maria', 'marcia', 'darina', 'daria']
message = f'Hello, {names[0].title()}!'
print(message)
print(f'Hello, {names[1].title()}!')
print(f'Hello, {names[2].title()}!')
print(f'Hello, {names[-1].title()}!')
print(f'Hello, {names[-2].title()}!')


# 3.3 countries I want to visit
countries = ['germany', 'italy', 'usa', 'greece']
message = f'The next country I will visit is {countries[-1].title()}'
print(message)

# 3.4
guests = ['albert einstein', 'mozart', 'tchaikovsky']
print(f'Hello, {guests[0].title()}, please join us for dinner!')
print(f'\nHello, {guests[1].title()}, please join us for dinner!')
print(f'\nHello, {guests[-1].title()}, please join us for dinner!')

# 3.5
guests = ['albert einstein', 'mozart', 'tchaikovsky']
print(f'\n{guests[-1].title()} can\'t join us today')
guests[-1] = 'pushkin a.s.'
print(f'{guests[-1].title()} will come instead')
print(f'{guests[0].title()} please join us')
print(f'{guests[1].title()} please join us')
print(f'{guests[-1].title()} please join us')

# 3.6. invite more guests
print(f'Dear {guests[0].title()}, {guests[1].title()}, {guests[-1].title()}, we expect more guests!')
guests.insert(0, 'brezhnev')
guests.insert(2, 'bach')
guests.append('pushkin')
print(guests)
print(f'\nDear {guests[0].title()}, please join us for dinner!')
print(f'Dear {guests[1].title()}, please join us for dinner!')
print(f'Dear {guests[2].title()}, please join us for dinner!')
print(f'Dear {guests[3].title()}, please join us for dinner!')
print(f'Dear {guests[4].title()}, please join us for dinner!')
print(f'Dear {guests[5].title()}, please join us for dinner!')
print('\nAttention!')
length = len(guests)
print(length)

# 3.7
print('I\'m terrible sorry, but only two guests can be invited')
print(guests)
popped_guest = guests.pop()
print(f'Dear {popped_guest.title()}, I\'m sorry, your invitation is canceled')
popped_guest = guests.pop()
print(f'Dear {popped_guest.title()}, I\'m sorry, your invitation is canceled')
popped_guest = guests.pop()
print(f'Dear {popped_guest.title()}, I\'m sorry, your invitation is canceled')
popped_guest = guests.pop()
print(f'Dear {popped_guest.title()}, I\'m sorry, your invitation is canceled')
print(f'Dear {guests[0].title()} your invitation is active')
print(f'Dear {guests[1].title()} your invitation is active')
del guests[0]
del guests[0]
print(guests)

# 3.8
countries = ['greece', 'usa', 'maldives', 'czech', 'austria']
print(countries)
# alphabetic, temporary
print(sorted(countries))
print(countries)
# reverse alphabetic, temporary
print((sorted(countries, reverse=True)))
print(countries)
# reverse, chronology
countries.reverse()
print(countries)
# to change back
countries.reverse()
print(countries)
# permanent change
countries.sort()
print(countries)
# permanent change
countries.sort(reverse=True)
print(countries)
print(len(countries))
