def add(a, b) -> int:
	return a + b

def multiply(a, b) -> int:
	return a * b

def reset_intcode():
	with open("input.txt", encoding="utf-8") as f:
		return [int(x) for x in f.readline().split(",")]



def execute_intcode(intcode, noun, verb):
	intcode[1] = noun
	intcode[2] = verb
	i = 0
	while True:
		if intcode[i] == 99:
			return intcode[0], intcode
		else:
			func = add if intcode[i] == 1 else multiply
			target_i = intcode[i+3]
			i_of_a = intcode[i+1]
			a = intcode[i_of_a]
			i_of_b = intcode[i+2]
			b = intcode[i_of_b]
			# print(f"func: {func}, a: {a}, b: {b}, target: {target_i}")
			intcode[target_i] = func(intcode[i_of_a],intcode[i_of_b])
			i += 4

# result, intcode = execute_intcode(RAW_INTCODE, 12, 2)

for noun in range(100):
	for verb in range(100):
		# print(f"Testing with noun = {noun} and verb = {verb}..")
		result, intcode = execute_intcode(reset_intcode(), noun, verb)
		# print(result)
		if result == 19690720:
			print(f"Result: {result}, noun: {noun}, verb: {verb} (Magic number 100 * noun + verb = {100*noun+verb})")

