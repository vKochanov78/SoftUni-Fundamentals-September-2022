import re

places = input()

pattern = r"(=|\/)[A-Z][a-zA-Z]{2,}\1"
destinations = []
travel_points = 0

result = re.finditer(pattern, places)

for destination in result:
    current_destination = re.split("\/|=", destination.group())[1]
    travel_points += len(current_destination)
    destinations.append(current_destination)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")