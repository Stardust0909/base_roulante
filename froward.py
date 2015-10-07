# fonction pour avancer de x metres
import RPi.GPIO as GPIO
from time import sleep
import threading
import sys

GPIO.setmode(GPIO.BCM)
global M1
global M2
global M3
global M4
global CD
global CG
global RD
global RG

M1 = 25
M2 = 22
M3 = 23
M4 = 24
CD = 4
CG = 17
RD = 21
RG = 18


GPIO.setup(M1,GPIO.OUT)
GPIO.setup(M2,GPIO.OUT)
GPIO.setup(M3,GPIO.OUT)
GPIO.setup(M4,GPIO.OUT)
GPIO.setup(CD,GPIO.IN)
GPIO.setup(CG,GPIO.IN)
GPIO.setup(RD,GPIO.IN)
GPIO.setup(RG,GPIO.IN)


# metre = int(sys.argv[1]) nombre de metre qu'on veut faire en argument de commande

global countL
global countR
global limite 

limite=1
countL=0
countR=0
inputL=
inputR=


a = threading.Thread(None, count, None, (RD,RG), {}) 

def count(inputL, inputR):
	if (GPIO.input(inputL)):
		countL = countL+1
	if (GPIO.input(inputR)):
		countR = countR+1
	print countL
	print countR

a.start()

while (limite):
	if ((count) > 10000):
		limite=0
	else:
		avancer()
		
		
def avancer():
	var = 1

	print "motor on"
	GPIO.output(M1,GPIO.LOW)
	GPIO.output(M2,GPIO.HIGH)
	GPIO.output(M3,GPIO.LOW)
	GPIO.output(M4,GPIO.HIGH)


	while var:
			if GPIO.input(CD) == 0:
					GPIO.output(M1,GPIO.LOW)
					GPIO.output(M2,GPIO.LOW)
					GPIO.output(M3,GPIO.LOW)
					GPIO.output(M4,GPIO.LOW)
					var = 0
			elif GPIO.input(CG) == 0:
					GPIO.output(M1,GPIO.LOW)
					GPIO.output(M2,GPIO.LOW)
					GPIO.output(M3,GPIO.LOW)
					GPIO.output(M4,GPIO.LOW)
					var = 0
			else:
					sleep(10)
					var = 0

	print "stopping motor"
	GPIO.output(M1,GPIO.LOW)
	GPIO.output(M2,GPIO.LOW)
	GPIO.output(M3,GPIO.LOW)
	GPIO.output(M4,GPIO.LOW)

	GPIO.cleanup()
