from threading import Thread, Lock
from Queue import Queue
from random import randrange
from time import sleep

class Worker(Thread):
	def __init__(self, name, delay, queue,
		     lock, producer=True):
		Thread.__init__(self)
		self.name = name
		self.delay = delay
		self.queue = queue
		self.lock = lock
		self.producer = producer

	def run(self):
		print "Starting %s" % self.name
		while not job_done:
			while self.producer and self.queue.full():
				print "Producer avoiding busy wait"
				sleep(self.delay)
			while not self.producer and self.queue.empty():
				print "Consumer avoiding busy wait"
				sleep(self.delay)
			with self.lock:
				if self.producer:
					rand = randrange(100)
					print "Put %d" % rand
					self.queue.put(rand)
				else:
					print "Got %d" % self.queue.get()
			sleep(self.delay)
		print "Exiting %s" % self.name

#################### DRIVERS ####################

job_done = False
q = Queue(10)
lock = Lock()
cons = Worker("Consumer", 2, q, lock, False)
cons.start()
prod = Worker("Producer", 1, q, lock, True)
prod.start()

sleep(7)
job_done = True
cons.join()
prod.join()
print "All done"
