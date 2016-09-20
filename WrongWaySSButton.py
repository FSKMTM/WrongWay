import RPi.GPIO as GPIO
import time
from time import sleep     # this lets us have a time delay (see line 12)  
import sys
import serial
import time

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # set GPIO 25 as input  
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
Time_test = 0
Time_start = time.time()
Time_end = 0
time_signal_1 = 0
time_signal_2 = 0
s = serial.Serial()
s.baudrate = 9600
s.timeout = 0
s.port = "/dev/ttyAMA0"
i = 0
z = 0

try:
    # Open serial port
    s.open()
except serial.SerialException, e:
    # There was an error
    sys.stderr.write("could not open port %r: %s\n" % (port, e))
    sys.exit(1)
s.write("$$$ALL,OFF\r")


while True:   
      GPIO.wait_for_edge(22, GPIO.RISING)
      timeS1 = time.time() * 1000000 
      GPIO.wait_for_edge(22, GPIO.FALLING)
      timeS2 = time.time() * 1000000
      timeS_d1 = timeS2 - timeS1
      a = 1
      u = 1
      timeS_d2 = 0
      timesignal = 0
      duration = 0
      if timeS_d1 > 13000:
         if timeS_d1 < 15000:
            while duration < 150000:
                  GPIO.wait_for_edge(22, GPIO.FALLING)
                  timeS3 = time.time() * 1000000
                  GPIO.wait_for_edge(22, GPIO.RISING)
                  cas = time.ctime()
                  timeS4 = time.time() * 1000000
                  timeS_d2 = timeS4 - timeS3
                  if u == 1:
                     timeS_d3 = timeS3 - timeS2
                  u = u + 1
                  duration = timeS4 - timeS2
                  timesignal = timesignal + timeS_d2
            a = u - 2
            if a != 0:
               timeaverage = (timesignal - timeS_d2) / a
      
      if a <= 9:
         if a >= 5:
            if duration >= 165000:
               if duration <= 183000:
                  if timeS_d3 >= 16000:
                     if timeS_d3 <= 17000:
                        if timeaverage >= 9500:
                           if timeaverage <= 11500:
                              time_signal_1 = time.time()
                              ss1 = a
                  if timeS_d3 >= 21500:
                     if timeS_d3 <= 26500:
                        if timeaverage >= 5500:
                           if timeaverage <= 7500:
                              time_signal_2 = time.time()*1000
                              ss2 = a
      if time_signal_1 != 0:
         if time_signal_2 != 0:
            if (time_signal_2 - time_signal_1) <= 10:
               if (time_signal_2 - time_signal_1) >= 1:
                  if (ss2 - ss1) >= 0:
                      input = 0
		      while input == 0:
		            print "Wrong way"
		            #Krog
		            s.write("$$$P4,3,ON\r")
		            s.write("$$$P4,4,ON\r")
		            s.write("$$$P4,5,ON\r")
		            s.write("$$$P4,6,ON\r")
		            s.write("$$$P4,7,ON\r")
		            s.write("$$$P5,2,ON\r")
		            s.write("$$$P5,3,ON\r")
		            s.write("$$$P5,7,ON\r")
		            s.write("$$$P5,8,ON\r")
		            s.write("$$$P6,1,ON\r")
		            s.write("$$$P6,2,ON\r")
		            s.write("$$$P6,8,ON\r")
		            s.write("$$$P6,9,ON\r")
		            s.write("$$$P7,1,ON\r")
		            s.write("$$$P7,9,ON\r")
		            s.write("$$$P8,1,ON\r")
		            s.write("$$$P8,9,ON\r")
		            s.write("$$$P9,1,ON\r")
		            s.write("$$$P9,2,ON\r")
		            s.write("$$$P9,8,ON\r")
		            s.write("$$$P9,9,ON\r")
		            s.write("$$$P10,2,ON\r")
		            s.write("$$$P10,3,ON\r")
		            s.write("$$$P10,7,ON\r")
		            s.write("$$$P10,8,ON\r")
		            s.write("$$$P11,3,ON\r")
		            s.write("$$$P11,4,ON\r")
		            s.write("$$$P11,5,ON\r")
		            s.write("$$$P11,6,ON\r")
		            s.write("$$$P11,7,ON\r")

		            #Crta
		            s.write("$$$P6,5,ON\r")
		            s.write("$$$P7,5,ON\r")
		            s.write("$$$P8,5,ON\r")
		            s.write("$$$P9,5,ON\r")
		            time.sleep(1)
		            s.write("$$$ALL,OFF\r")
		            time.sleep(0.1)
            
		            #Napis
		            #S
		            s.write("$$$P1,2,ON\r")
		            s.write("$$$P1,3,ON\r")
		            s.write("$$$P1,6,ON\r")
		            s.write("$$$P2,1,ON\r")
		            s.write("$$$P2,4,ON\r")
		            s.write("$$$P2,7,ON\r")
		            s.write("$$$P3,2,ON\r")
		            s.write("$$$P3,5,ON\r")
		            s.write("$$$P3,6,ON\r")
		            #Podcrtano
		            s.write("$$$P1,9,ON\r")
		            s.write("$$$P2,9,ON\r")
		            s.write("$$$P3,9,ON\r")
		            s.write("$$$P4,9,ON\r")
		            #T   
		            s.write("$$$P4,1,ON\r")
		            s.write("$$$P5,1,ON\r")
		            s.write("$$$P6,1,ON\r")
		            s.write("$$$P5,2,ON\r")
		            s.write("$$$P5,3,ON\r")
		            s.write("$$$P5,4,ON\r")
		            s.write("$$$P5,5,ON\r")
		            s.write("$$$P5,6,ON\r")
		            s.write("$$$P5,7,ON\r")
		            #Podcrtano
		            s.write("$$$P5,9,ON\r")
		            s.write("$$$P6,9,ON\r")
		            s.write("$$$P7,9,ON\r")
		            s.write("$$$P8,9,ON\r")
		            #O
		            s.write("$$$P8,1,ON\r")
		            s.write("$$$P9,1,ON\r")
		            s.write("$$$P7,2,ON\r")
		            s.write("$$$P7,3,ON\r")
		            s.write("$$$P7,4,ON\r")
		            s.write("$$$P7,5,ON\r")
		            s.write("$$$P7,6,ON\r")
		            s.write("$$$P8,7,ON\r")
		            s.write("$$$P9,7,ON\r")
		            s.write("$$$P10,6,ON\r")
		            s.write("$$$P10,5,ON\r")
		            s.write("$$$P10,4,ON\r")
		            s.write("$$$P10,3,ON\r")
		            s.write("$$$P10,2,ON\r")
		            #Podcrtano
		            s.write("$$$P9,9,ON\r")
		            s.write("$$$P10,9,ON\r")
		            s.write("$$$P11,9,ON\r")
		            s.write("$$$P12,9,ON\r")
		            #P
		            s.write("$$$P12,1,ON\r")
		            s.write("$$$P12,2,ON\r")
		            s.write("$$$P12,3,ON\r")
		            s.write("$$$P12,4,ON\r")
		            s.write("$$$P12,5,ON\r")
		            s.write("$$$P12,6,ON\r")
		            s.write("$$$P12,7,ON\r")
		            s.write("$$$P13,1,ON\r")
		            s.write("$$$P14,1,ON\r")
		            s.write("$$$P14,2,ON\r")
		            s.write("$$$P14,3,ON\r")
		            s.write("$$$P13,3,ON\r")
		            #Podcrtano
		            s.write("$$$P13,9,ON\r")
		            s.write("$$$P14,9,ON\r")
		
		            time.sleep(1)
		            s.write("$$$ALL,OFF\r")
		            time.sleep(0.1)
		            input = GPIO.input(4)            
	              time_signal_1 = 0
	              time_signal_2 = 0

GPIO.cleanup()
