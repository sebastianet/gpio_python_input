#!/usr/bin/env python

# executem amb "sudo ./sortida.py"

import RPi.GPIO as GPIO
import time

# escollim numeracio "com a la placa"
GPIO.setmode(GPIO.BOARD)

# com sortida fem servir el penultim pin de l'esquerra (see command "pinout") - GPIO27, pin 37
SORTIDA = 37

# programem el pin com de "sortida"
GPIO.setup(SORTIDA, GPIO.OUT)

print '(1) encenem el llum'
GPIO.output(SORTIDA, GPIO.HIGH)

print '(2) esperem 3 segons'
time.sleep(3)

print '(3) apaguem el llum'
GPIO.output(SORTIDA, GPIO.LOW)

print '(4) netejem i acabem'
GPIO.cleanup()
