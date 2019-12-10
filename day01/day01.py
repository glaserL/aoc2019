from math import floor
weights = []
with open("input.txt", encoding="utf-8") as f:
	for line in f:
		weights.append(int(line.strip()))


def calculate_required_fuel(mass: int) -> int:
	return floor(mass/3)-2

total_fuel_required = sum([calculate_required_fuel(weight) for weight in weights])

print(f"Total fuel required: {total_fuel_required}")



def calculate_required_fuel_recursively(mass) -> int:
	required_fuel = calculate_required_fuel(mass)
	if required_fuel < 0:
		return 0
	else:
		return required_fuel + calculate_required_fuel_recursively(required_fuel)
		
total_fuel_required_including_fuel_mass = sum([calculate_required_fuel_recursively(weight) for weight in weights])

print(f"Total fuel required including fuel mass: {total_fuel_required_including_fuel_mass}")