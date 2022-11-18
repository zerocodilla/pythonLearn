def get_city_country(city, country, population=''):
    """Accept two parameters: a city name and a country name and return a single string."""
    if population:
        formatted_city = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_city = f"{city.title()}, {country.title()}"
    return formatted_city