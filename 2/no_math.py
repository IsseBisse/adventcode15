def get_data(path):
	with open(path) as file:
		data = file.read().split("\n")

	for i, entry in enumerate(data[:-1]):
		parsed_entry = entry.split("x")
		data[i] = tuple([int(num) for num in parsed_entry])

	return data

def part_one():
	data = get_data("input.txt")
	print(data)
	
def part_two():
	pass

if __name__ == '__main__':
	part_one()