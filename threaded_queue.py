from time import time, ctime, sleep
from threading import Thread, Lock
from Queue import Queue

class MyQueue(object):
	def __init__(self):
		self.store = []

	def put(self, value):
		self.store.append(value)

	def get(self):
		return self.store.pop(0)

	def peek(self):
		return self.store[0]

	def empty(self):
		return not self.store


class SyncQueue(Thread):
	__lock = Lock()

	def __init__(self, name, delay, queue):
		Thread.__init__(self)
		self.name = name
		self.delay = delay
		self.queue = queue

	def run(self):
		print "Starting %s" % self.name
		while not self.queue.empty():
			with self.__lock:
				print "%s got %s" % (
						self.name,
						self.queue.get())
			sleep(self.delay)
		while not job_done:
			sleep(self.delay)
		print "Exiting %s" % self.name

if __name__ == "__main__":
	job_done = False
	#q = Queue(5) # Python's Queue
	q = MyQueue() # Custom Queue
	for i in xrange(5):
		q.put(i)
	q1 = SyncQueue("Q1", .5, q)
	q2 = SyncQueue("Q2", 1, q)
	q1.start()
	q2.start()

	# Wait for the job to be done
	while not q.empty():
		pass
	job_done = True
	q1.join()
	q2.join()
	print "All done!"
