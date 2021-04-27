import re
from Wire import Wire

def get_data(path):

	with open(path) as file:
		data = file.read().split("\n")

	return data

def parse_data(raw_data):

	data = list()
	for line in raw_data:
		data.append(parse_line(line))

	return data

def parse_line(line):

	connection = dict()
	[sender, connection["receiver"]] = line.split(" -> ")

	operator = re.findall(r"[A-Z]+", sender)
	connection["operator"] = operator[0] if len(operator) > 0 else "CONST"

	connection["args"] = re.findall(r"[0-9a-z]+", sender)
	
	return connection

def part_one():

	raw_data = get_data("smallInput.txt")
	connections = parse_data(raw_data)
	
	wires = dict()
	for conn in connections:
		name = conn["receiver"]
		wires[name] = Wire(name)

	print(wires["x"])

def part_two():
	pass

if __name__ == '__main__':
	part_one()