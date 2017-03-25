class Event(object):
	NONE    = None
	ROCK    = 0
	SCISSOR = 1
	SPOCK   = 2
	PAPER   = 4
	
	def __init__(self, type_ = None):
		self.type = type_

	def setType(self, type_):
		self.type = type_