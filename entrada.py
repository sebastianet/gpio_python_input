#!/usr/bin/env python

# executem amb "sudo ./entrada.py"

import RPi.GPIO as GPIO                   # import GPIO library
import time                               # import time library to have time.time()
import datetime                           # import datetime library 
from time import sleep                    # import time library to have "sleep"

print "Version GGPIO =", GPIO.VERSION     # mostrar la versio de GPIO 

GPIO.setmode(GPIO.BOARD)                  # escollim numeracio "com a la placa"

ENTRADA = 36  # com entrada fem servir el tercer pin de baix a la dreta (see command "pinout") - GPIO16, pin 36
SORTIDA = 37  # com sortida fem servir el penultim pin de l'esquerra (see command "pinout") - GPIO27, pin 37

GPIO.setup(ENTRADA, GPIO.IN)    # set GPIO16 as input (button)  
GPIO.setup(SORTIDA, GPIO.OUT)   # set GPIO27 as output (LED)  

QQ = 2  # dont have a html file yet

try:  
    while True:                                                # this will carry on until you hit CTRL+C  

        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        if GPIO.input(ENTRADA):                                # if port 36 == 1  
            print "+++ " + st + " pin 36 is 1/HIGH/True - led ON  +++"  
            GPIO.output(SORTIDA, 1)                            # set port/pin value to 1/HIGH/True  
            if QQ != 1:
                QQ = 1
                
                f = open('./public/helloworld.html','w')
                message  = "<html>\n<head>\n"
                message += "<LINK REL=STYLESHEET HREF='./css/entrada.css' TYPE='text/css'>\n"
                message += "<title> (+) up (+) </title>\n"
                message += "</head>\n"
                message += "<body>\n<hr>\n<p>&nbsp;</p>\n<p class='dalt'> up at "
                message += st
                message += " </p>\n<p>&nbsp;</p>\n<hr>\n</body>\n</html>\n"
                f.write(message)
                f.close()

        else:  
            print "--- " + st + " pin 36 is 0/LOW/False - led OFF ---"  
            GPIO.output(SORTIDA, 0)                            # set port/pin value to 0/LOW/False  
            if QQ != 0:
                QQ = 0
                f = open('./public/helloworld.html','w')
                message  = "<html>\n<head>\n"
                message += "<LINK REL=STYLESHEET HREF='./css/entrada.css' TYPE='text/css'>\n"
                message += "<title> (-) down (-) </title>\n"
                message += "</head>\n"
                message += "<body>\n<hr>\n<p>&nbsp;</p>\n<p class='baix'> down at "
                message += st
                message += " </p>\n<p>&nbsp;</p>\n<hr>\n</body>\n</html>\n"
                f.write(message)
                f.close()

        sleep(0.5)         # wait 0.5 seconds  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  
