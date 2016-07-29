class InstanceExists(Exception):
	pass


class Singleton(type):
	"""A parent class for singleton entity classes."""

	__instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls.__instances:
			cls.__instances[cls] = super(Singleton, cls) \
					.__call__(*args, **kwargs)
			return cls.__instances[cls]
		raise InstanceExists(cls.__instances[cls])


class TL(object):
	"""A fresher in the call-center."""

	__metaclass__ = Singleton

	def __init__(self, name, available=True):
		self.name = name
		self.available = available

	def __repr__(self):
		return self.name


if __name__ == "__main__":
	tl = TL("Leo")
	t2 = TL("DiCaprio")
