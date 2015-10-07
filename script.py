
M1 = 25
M2 = 22
M3 = 23
M4 = 24
CD = 4
CG = 17
var = 1


GPIO.setup(M1,GPIO.OUT)
GPIO.setup(M2,GPIO.OUT)
GPIO.setup(M3,GPIO.OUT)
GPIO.setup(M4,GPIO.OUT)
GPIO.setup(CD,GPIO.IN)
GPIO.setup(CG,GPIO.IN)

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

