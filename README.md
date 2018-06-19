# RPi-Button-Interface
This program provides Button interface with different LED colors raspberry pi
  
# Development Environment
  * OS: Raspbian for Raspberry Pi
  * Libraries required: 
        SPI library of Python
        PIL (Python Imaging Library) library

# Hardware connection
  * EPD    =>    Raspberry Pi
  * VCC    ->    3.3
  * GND    ->    GND
  * Button1->    GPIO 16
  * Button2->    GPIO 26
  * LED1   ->    GPIO 12
  * LED2   ->    GPIO 13
  * LED3   ->    GPIO 18

# How to use
  1. install the Python libraries.
  2. change the current directory to where the file located.
  3. run the code with: 
     sudo python butterInterface.py


