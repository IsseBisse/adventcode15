class Wire:

	def CONST(self):
		return self.args[0]

	def NOT(self):
		return ~self.args[0].get_value()

	def AND(self):
		return self.args[0].get_value() & self.args[1].get_value()

	def OR(self):
		return self.args[0].get_value() | self.args[1].get_value()

	def LSHIFT(self):
		return self.args[0].get_value() << self.args[1].get_value()

	def RSHIFT(self):
		return self.args[0].get_value() >> self.args[1].get_value()

	def __init__(self, name):
		self.name = name
		self.get_value = None
		self.args = None

	def __str__(self):
		return self.name

	def set_getter(self, func_name, args):
		self.args = args
		self.get_value = func_name
