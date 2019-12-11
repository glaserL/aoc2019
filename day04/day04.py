import sys
from tqdm import tqdm
BEGIN = None
END = None


def never_decrease(pw):
	current_max = 0
	for digit in pw:
		if current_max > digit:
			return False
		else:
			current_max = max(current_max, digit)
	return True

def has_double(pw):
	for i, digit in enumerate(pw):
		if i != 0 and pw[i-1] == digit:
			return True
	return False


def has_independent_double(pw):
	previous_digit = pw[0]
	number_of_same_until_now = 0
	for i, digit in enumerate(pw):
		if digit == previous_digit:
			number_of_same_until_now += 1
		else:
			if number_of_same_until_now == 2:
				return True
			else: 
				number_of_same_until_now = 1
		previous_digit = digit
	if number_of_same_until_now == 2:
		return True
	return False

# def has_independent_double(pw):
# 	seeing_double_rn = False
# 	for i, digit in enumerate(pw):

# 		if i < 2 and pw[i-1] == digit and pw[i-2] != digit:
# 			try:
# 				third = pw[i+1]
# 				if third != digit:
# 					return True
# 			except IndexError:
# 				print("Index Error")
# 				return True
# 		else:
# 			seeing_double_rn = False
# 	return False

checks = [
	lambda x: len(x) == 6,
	lambda x: BEGIN < int("".join([str(x_i) for x_i in x])) < END,
	has_double,
	has_independent_double,
	never_decrease

]

def check_password(pw):
	for check in checks:
		if not check(pw):
			return False
	return True

try:
	single_pw = int(sys.argv[1])
	pw_as_digits = [int(i) for i in str(single_pw)]
	print(f"Length: {len(pw_as_digits)==6}")
	print(f"has_double: {has_double(pw_as_digits)}")
	print(f"has_independent_double: {has_independent_double(pw_as_digits)}")
	print(f"never_decrease: {never_decrease(pw_as_digits)}")
except ValueError:
	with open(sys.argv[1], encoding = "utf-8") as f:
		BEGIN, END = f.readline().strip().split("-")
		BEGIN, END = int(BEGIN), int(END)
		print(f"Testing range {BEGIN}-{END}.")
		pw_count = 0 
		for pw in tqdm(range(BEGIN, END)):
			pw_as_digits = [int(i) for i in str(pw)]
			if check_password(pw_as_digits):
				pw_count += 1

	print(f"{pw_count} passwords match the criteria.")