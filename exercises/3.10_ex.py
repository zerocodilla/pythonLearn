# visited counties in 2022
countries = ['russia', 'kazakhstan', 'uzbekistan', 'turkey', 'bulgaria', 'serbia']
# number of visited countries
visited = len(countries)
print(f'This year I\'ve been to {visited} countries.')
# transition country
print(f'In {countries[2].title()} I did not leave the airport.')
# remove transition country
popped_country = countries.pop(2)
print(f'So, {popped_country.title()} can be skipped.')
visited = len(countries)
print(f'It means I\'ve visited {visited} countries.')
# countries I've been the longest time
print(f'In {countries[0].title()} and in {countries[-2].title()} I\'ve spent the most time of the year.')
# change country
initial_val = countries[1]
countries[1] = 'greece'
print(f'I wish I would visit {countries[1].title()} instead of {initial_val.title()}')
# add country back
countries.insert(1, 'kazakhstan')
print(f'But this is not true. So, I add {countries[1].title()} back.')
# remove greece
visited = len(countries)
print(f'Let\'s check the list: {visited}. Something\'s wrong')
print(countries)
print(f'{countries[2].title()} is good dream, but unreal this year. Let\'s remove it')
del countries[2]
visited = len(countries)
print(f'Let\'s check the list: {visited}. Look\'s good')
# add at the end
countries.append('italy')
print(f'I wish we will go to {countries[-1].title()}')
countries.remove('italy')
print(countries)
# sort
countries.reverse()
print(countries)
countries.reverse()
print(countries)
