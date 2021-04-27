class Wire:

	def CONST(self):
		return self.args[0]

	def NOT(self):
		pass

	def AND(self):
		pass

	def OR(self):
		pass

	def LSHIFT(self):
		pass

	def RSHIFT(self):
		pass

	def __init__(self, name):
		self.name = name
		self.operator = None
		self.args = None

	def __get__(self):
		return self.operator()

	def __str__(self):
		return self.name

	def set_getter(self, func_name, args):
		self.args = args
		self.operator = func_name
