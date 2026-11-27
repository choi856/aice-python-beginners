# splitting african countries
african_countries = "Nigeria,Zimbabawe,Egypt,SouthAfrica,Ethopia"
countries_list = african_countries.split(",")
print(countries_list)

#splitting both on slash
date = "15/08/2003"
date_parts = date.split("/")
day = date_parts[0]
month = date_parts[1]
year = date_parts[2]
print(f"Day: {day}, Month: {month}, Year: {year}")
