import numpy as np
from tqdm import tqdm
import sys
from collections import defaultdict


def print_grid(grid):
	for i in range(grid.shape[0]):
		strbuffer = []
		for j in range(grid.shape[1]):
			value = grid[i,j]
			if value == 2:
				strbuffer.append("X")
			if value == 1:
				strbuffer.append(" -")
			else:
				strbuffer.append(" . ")
		print("".join(strbuffer))
		strbuffer.clear()



def parse_rawstring_to_tuple(rawstring: str):
	return (rawstring[0], int(rawstring[1:]))

def get_max_dimensions_x_y(wires):
	max_x_global = 0
	max_y_global = 0 
	for wire in wires:
		max_x = 0
		max_y = 0
		for direction, distance in wire:
			if direction == "L":
				max_x += distance
			elif direction == "R":
				max_x += distance
			if direction == "U":
				max_y += distance
			elif direction == "D":
				max_y += distance
		max_x_global = max(max_x_global, max_x)
		max_y_global = max(max_y_global, max_y)
	return max_x_global, max_y_global

def expand_instructions_to_indextuples(origin, direction, distance):
	indextuples = []
	if direction == "R":
		indextuples = [(x, origin[1]) for x in range(origin[0], origin[0]+distance+1, 1)]
	elif direction == "L":
		indextuples = [(x, origin[1]) for x in range(origin[0], origin[0]-distance-1, -1)]
	elif direction == "U":
		indextuples = [(origin[0], x) for x in range(origin[1], origin[1]+distance+1, 1)]
	elif direction == "D":
		indextuples = [(origin[0], x) for x in range(origin[1], origin[1]-distance-1, -1)]
	else: 
		print("Invalid direction.")
	print(f"Moving {len(indextuples)} to direction {direction} from start {origin}")
	return indextuples


with open(sys.argv[1], encoding="utf8") as f:
	wire_one = [parse_rawstring_to_tuple(direction) for direction in f.readline().strip().split(",")]
	wire_two = [parse_rawstring_to_tuple(direction) for direction in f.readline().strip().split(",")]

wires = [wire_one, wire_two]

grid_shape = get_max_dimensions_x_y(wires)
print(f"Initializing grid with shape {grid_shape}")
grid = np.zeros(grid_shape, dtype=int)


distance_to_nearest_crossing = np.inf
cross_mark = len(wires)
print(f"Crosses have value {cross_mark}")

for wire in wires:
	cur = (0, 0)
	for direction, distance in wire:
		for i, j in expand_instructions_to_indextuples(cur, direction, distance):
			cur = (i, j)
			grid[i,j] += 1
			if grid[i,j] == cross_mark and (i+j) != 0:
				distance_to_nearest_crossing = min(distance_to_nearest_crossing, abs(i)+abs(j))

# print_grid(grid)
print(f"Manhattan distance to nearest crossing: {distance_to_nearest_crossing}")



