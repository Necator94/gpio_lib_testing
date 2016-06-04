from bbio import *
import time
import Adafruit_BBIO.GPIO as GPIO
import threading
pinMode(GPIO0_26, INPUT)
GPIO.setup("P8_12", GPIO.OUT)
#export = open('/sys/class/gpio/export','w')
#export.write('46')
#export.close()
def bbiolib():
	a = []
	startTime = time.time()
	for i in range (10000):
		st = time.time()
		state = digitalRead(GPIO0_26)
		a.append(time.time() - st)
	meana = sum(a)/len(a)
	print time.time() - startTime, '  mean bbio', 1/meana

def adafruitlib():
	b = []
	startTime = time.time()
	for i in range (10000):
		st = time.time()
		state = GPIO.input("P8_12")
		b.append(time.time() - st)
	meanb = sum(b)/len(b)

	print time.time() - startTime, '  mean Adafruit_BBIO', 1/meanb
	GPIO.cleanup()

def sysfs():
	c = []
	f = open('/sys/class/gpio/gpio46/value', 'r')
	startTime = time.time()
	for i in range (10000):
		st = time.time()
		f.read()
		#time.sleep(0.0001)
		c.append(time.time() - st)
	f.close()
	meanc = sum(c)/len(c)

	print time.time() - startTime, '  mean sysfs', 1/meanc
	#unexport = open('/sys/class/gpio/unexport','w')
	#unexport.write('46')
	#unexport.close()

'''
aThread = threading.Thread(target = bbiolib)
bThread = threading.Thread(target = adafruitlib)
cThread = threading.Thread(target = sysfs)


aThread.start()
bThread.start()
cThread.start()
'''
bbiolib()
adafruitlib()
sysfs()