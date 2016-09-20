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

try:
    # Open serial port
    s.open()
except serial.SerialException, e:
    # There was an error
    sys.stderr.write("could not open port %r: %s\n" % (port, e))
    sys.exit(1)

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
#                     print "\n%d" %timeS3
 #                    print "%d\n" %timeS2
  #                print "%d\r" %timeS_d2
                  u = u + 1
                  duration = timeS4 - timeS2
                  timesignal = timesignal + timeS_d2
   #         print "\n%d\r" %timeS_d3
            a = u - 2
    #        print "%d\r" %a
            if a != 0:
               timeaverage = (timesignal - timeS_d2) / a
     #       print "%d\r" %timeaverage
      #      print "%d\r\n" %duration
      
      if a == 8:
         if duration >= 165000:
            if duration <= 183000:
               if timeS_d3 >= 16000:
                  if timeS_d3 <= 17000:
                     if timeaverage >= 9500:
                        if timeaverage <= 11500:
                           print "\n\n            Signal 1 %s          \n\n" %cas
                           s.write("1")
                           time.sleep(1)
                           s.write("$$$ALL,OFF\r")
                           time_signal_1 = time.time()
               if timeS_d3 >= 21500:
                  if timeS_d3 <= 26500:
                     if timeaverage >= 5500:
                        if timeaverage <= 7500:
                           print "Signal 2 %s" %cas
                           s.write("2")
                           time.sleep(0.5)
                           s.write("$$$ALL,OFF\r")

                           time_signal_2_new = time.time()*1000
                           time_signal_2_diff = time_signal_2_new - time_signal_2
#                           print "%d" %time_signal_2_diff
                           if time_signal_2_diff >= 1000:
                              i = i + 1
#                              print "\n\nVec kot sekunda %d.!!\n\n" %i
                           time_signal_2 = time.time()*1000

      if time_signal_1 != 0:
         if time_signal_2 != 0:
            if (time_signal_2 - time_signal_1) <= 10:
               if (time_signal_2 - time_signal_1) >= 1:
                  input = 0
                  while input == 0:
                        print "Wrong way"
                        s.write("Wrong way")
                        time.sleep(4)
                        input =  GPIO.input(4)
                  time_signal_1 = 0
                  time_signal_2 = 0
                  s.write("$$$ALL,OFF\r")
       
      Time_end = time.time()
      Time_test = Time_end - Time_start

GPIO.cleanup()
