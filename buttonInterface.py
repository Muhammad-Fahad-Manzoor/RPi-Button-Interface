import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#Button1 to GPIO16
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#Button2 to GPIO26
GPIO.setup(12, GPIO.OUT)  #LED1 to GPIO12
GPIO.setup(13, GPIO.OUT)  #LED2 to GPIO13
GPIO.setup(18, GPIO.OUT)  #LED3 to GPIO18


try:
    while True:
	 print('Finds button states')
         btn1_state = GPIO.input(16)
	 btn2_state = GPIO.input(26)

         if btn1_state == True: #False means Button NOT pressed
	     print('BTN1 is pressed')
             GPIO.output(12, True)
             time.sleep(5)
             GPIO.output(12, False)
             time.sleep(5)
             print('BTN1 state ends')
             
         if btn2_state == True: #False means Button NOT pressed
	     print('BTN2 is pressed')
             GPIO.output(13, True)
             time.sleep(5)
             GPIO.output(13, False)
             time.sleep(5)
             print('BTN2 state ends')
   
         else:
             print('No BTN press')
	     GPIO.output(18, True)
	     time.sleep(5)
             GPIO.output(18, False)
	     time.sleep(5)
	     print('led state ends')
	     
except:
    GPIO.cleanup()
    print('cleaning up...')
    