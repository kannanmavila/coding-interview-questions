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
		raise InstanceExists(InstanceExists(cls.__instances[cls]))


class Employee(object):
	"""An employee of the call-centre.

	Attributes:
		available: availability to perform a task

	"""

	def __init__(self, name, available=True):
		self.name = name
		self.available = available

	def is_available(self):
		return self.available

	def __repr__(self):
		return "Mr/s. %s (%s)" % (self.name, type(self).__name__)


class Fresher(Employee):
	"""A Team-lead in the call-centre."""

	def __init__(self, name, available=True):
		Employee.__init__(self, name, available)


class TL(Employee):
	"""A fresher in the call-center."""

	__metaclass__ = Singleton

	def __init__(self, name, available=True):
		Employee.__init__(self, name, available)


class PM(Employee):
	"""A Product Manager in the call-center."""

	__metaclass__ = Singleton

	def __init__(self, name, available=True):
		Employee.__init__(self, name, available)


if __name__ == "__main__":
	f1 = Fresher("Tom")
	f2 = Fresher("Hardy")
	tl = TL("Leo")
	pm = PM("DiCaprio")
