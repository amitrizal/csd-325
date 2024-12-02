# city_functions.py

def city_country(city, country, population=None, language=None):
    """Returns a formatted string with city, country, optional population, and language."""
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result

# Test calls
print(city_country("santiago", "chile"))
print(city_country("kathmandu", "nepal", population=1000000))
print(city_country("tokyo", "japan", population=14000000, language="japanese"))
