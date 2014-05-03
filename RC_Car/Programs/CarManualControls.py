"""OSC Test Script
Written by Aaron Chamberlain Dec. 2013
The purpose of this script is to make a very simple communication structure to the popular 
application touchOSC. This is achieved through the pyOSC library. However, since the pyOSC 
documentation is scarce and only one large example is included, I am going to strip down 
the basic structures of that file to implement a very simple bi-directional communication.
"""

#!/usr/bin/env python

import socket, OSC, re, time, threading, math
from RPIO import PWM

servo = PWM.Servo()
motor = PWM.Servo()
servoPin = 23
motorPin = 18

receive_address = 'xxx,xxx.xxx.xxx', 7000 #Mac Adress, Outgoing Port
send_address = 'xxx.xxx.xxx.xxx', 9000 #iPhone Adress, Incoming Port

class PiException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)
		
##########################
#	OSC
##########################

# Initialize the OSC server and the client.
s = OSC.OSCServer(receive_address)
c = OSC.OSCClient()
c.connect(send_address)

s.addDefaultHandlers()

# define a message-handler function for the server to call.
def test_handler(addr, tags, stuff, source):
	print "---"
	print "received new osc msg from %s" % OSC.getUrlStr(source)
	print "with addr : %s" % addr
	print "typetags %s" % tags
	print "data %s" % stuff
	msg = OSC.OSCMessage()
	msg.setAddress(addr)
	msg.append(stuff)
	c.send(msg)
	print "return message %s" % msg
	print "---"
	
def moveStop_handler(add, tags, stuff, source): #function for stop button +
	servo.stop_servo(servoPin)
	motor.stop_servo(motorPin)

def moveMode_handler(add, tags, stuff, source): #function for mode button -implement
	addMove(0,0)


def moveServo_handler(add, tags, stuff, source): #function for direction fader +
	print "message received:"
	msg = OSC.OSCMessage()
	msg.setAddress(addr)
	msg.append(stuff)
	c.send(msg)
	servoVal = round(stuff[0], -1)
	int(servoVal)
	servo.set_servo(servoPin, servoVal) #sets servo to val from iPhone

def moveSlow_handler(add, tags, stuff, source): #function for stealth fader, slow movement +
	print "message received:"
	msg = OSC.OSCMessage()
	msg.setAddress(addr)
	msg.append(stuff)
	c.send(msg)
	motorStealthVal = round(stuff[0], -1)
	int(motorStealthVal)
	servo.set_servo(motorPin, motorStealthVal) #sets motor to val from iPhone

def moveForward_handler(add, tags, stuff, source): #function for Forward button +
	print "message received:"
	msg = OSC.OSCMessage()
	msg.setAddress(addr)
	msg.append(stuff)
	c.send(msg)
	motorVal = stuff[0]
	motor.set_servo(motorPin, motorVal)

def moveReverse_handler(add, tags, stuff, source): #function for Reverse button +
	print "message received:"
	msg = OSC.OSCMessage()
	msg.setAddress(addr)
	msg.append(stuff)
	c.send(msg)
	motorRevVal = stuff[0]
	motor.set_servo(motorPin, motorRevVal)
	
	
# adding my functions - all buttons listed -done
s.addMsgHandler("/car/stop", moveStop_handler)
s.addMsgHandler("/car/mode", moveMode_handler)
s.addMsgHandler("/car/direction", moveServo_handler)
s.addMsgHandler("/car/speed", moveSlow_handler)
s.addMsgHandler("/car/forward", moveForward_handler)
s.addMsgHandler("/car/reverse", moveReverse_handler)

# just checking which handlers we have added
print "Registered Callback-functions are :"
for addr in s.getOSCAddressSpace():
	print addr
	
# Start OSCServer
print "\nStarting OSCServer. Use ctrl+C to quit."
st = threading.Thread( target = s.serve_forever )
st.start()

# Loop while threads are running.
try :
	while 1 :
		time.sleep(10)
 
except KeyboardInterrupt :
	print "\nClosing OSCServer."
	s.close()
	print "Waiting for Server-thread to finish"
	st.join()
	print "Done"
	servo.stop_servo(servoPin)
					
