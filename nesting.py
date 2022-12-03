travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille","Dijon"],
        "total_visits":12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg","Stuttgart"],
        "total_visits":5
    }
]
def add_new_country(country_name,cities,times_visited):
    new_entry = {
        "country":country_name,
        "cities_visited":cities,
        "total_visits":times_visited
    }
    travel_log.append(new_entry)
def add_new_country2(country_name,cities,times_visited):
    new_entry = {}
    new_entry["country"] = country_name
    new_entry["cities_visited"] = cities
    new_entry["total_visits"] = times_visited
    travel_log.append(new_entry)

add_new_country2(country_name="Russia",cities=["Moscow","St.Peter"],times_visited=2)
print(travel_log[1])