#  MBTechWorks.com 2016
#  Control an LCD 1602 display from Raspberry Pi with Python programming

#!/usr/bin/python

# Pinout of the LCD:
# 1 : GND
# 2 : 5V power
# 3 : Display contrast    - Connect to middle pin potentiometer   
# 4 : RS (Register Select)
# 5 : R/W (Read Write)    - Ground this pin (important)
# 6 : Enable or Strobe
# 7 : Data Bit 0          - data pin 0, 1, 2, 3 are not used
# 8 : Data Bit 1          -   
# 9 : Data Bit 2          -   
# 10: Data Bit 3          -   
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V
# 16: LCD Backlight GND

import RPi.GPIO as GPIO
import time
import datetime #  m.s for system data and time

import sys, select, termios, os
from gpiozero import Button, LoadAverage,CPUTemperature


# GPIO to LCD mapping
LCD_RS = 7   # Pi pin 26
LCD_E  = 8   # Pi pin 24
LCD_D4 = 25  # Pi pin 22
LCD_D5 = 24  # Pi pin 18
LCD_D6 = 23  # Pi pin 16
LCD_D7 = 18  # Pi pin 12

# Device constants
LCD_CHR = True    # Character mode
LCD_CMD = False   # Command mode
LCD_CHARS = 16    # Characters per line (16 max)
LCD_LINE_1 = 0x80 # LCD memory location for 1st line
LCD_LINE_2 = 0xC0 # LCD memory location 2nd line

BUZZ = 17
button = Button(2)
# Define main program code
def main():
  
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E, GPIO.OUT)  # Set GPIO's to output mode
  GPIO.setup(LCD_RS, GPIO.OUT)
  GPIO.setup(LCD_D4, GPIO.OUT)
  GPIO.setup(LCD_D5, GPIO.OUT)
  GPIO.setup(LCD_D6, GPIO.OUT)
  GPIO.setup(LCD_D7, GPIO.OUT)
  
  GPIO.setup(BUZZ,GPIO.OUT)
  GPIO.output(BUZZ, False) 

# Initialize display
  lcd_init()

    
# Loop - send text and sleep 3 seconds between texts
# Change text to anything you wish, but must be 16 characters or less
  old_minute = 0 
  load_old = 0
  cpu_str_old = 0
  
  while True:

#and the access its now method simpler
    now = datetime.datetime.now()
    str_now = str(now)

    load = "CPU:"+str(int(LoadAverage(minutes=1).load_average*12))+"%"
    cpu = CPUTemperature(min_temp=50, max_temp=90)
    cpu_str = round(cpu.temperature,1)
    cpu_str = str(cpu_str)+"C"
    
    #str_hour= str(now.hour) 
    #str_minute= str(now.minute)
    #str_second= str(now.second)
    #str_sum = "str_hour" + "str_minute" + "str_second"
    
    print('Initial temperature: {}C'.format(cpu.temperature))
    
    minute=(now.minute)
    if (load_old != load)|(old_minute != minute)|(cpu_str_old != cpu_str):
      load_old = load 
      old_minute = minute
      cpu_str_old = cpu_str
      
      lcd_text(load +"  t:"+ cpu_str,LCD_LINE_1)
      lcd_text(str_now ,LCD_LINE_2)
      print("now")
    
    if button.is_pressed:
      time.sleep(0.07)
      if button.is_pressed:
        print("End")
        #break 
          
    time.sleep(0.1)
# End of main program code


# Initialize and clear display
def lcd_init():
  lcd_write(0x33,LCD_CMD) # Initialize
  lcd_write(0x32,LCD_CMD) # Set to 4-bit mode
  lcd_write(0x06,LCD_CMD) # Cursor move direction
  lcd_write(0x0C,LCD_CMD) # Turn cursor off
  lcd_write(0x28,LCD_CMD) # 2 line display
  lcd_write(0x01,LCD_CMD) # Clear display
  time.sleep(0.0005)     # Delay to allow commands to process

def lcd_write(bits, mode):
# High bits
  GPIO.output(LCD_RS, mode) # RS

  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)

# Toggle 'Enable' pin
  lcd_toggle_enable()

# Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)

# Toggle 'Enable' pin
  lcd_toggle_enable()

def lcd_toggle_enable():
  time.sleep(0.0005)
  GPIO.output(LCD_E, True)
  time.sleep(0.0005)
  GPIO.output(LCD_E, False)
  time.sleep(0.0005)

def lcd_text(message,line):
  # Send text to display
  message = message.ljust(LCD_CHARS," ")

  lcd_write(line, LCD_CMD)

  for i in range(LCD_CHARS):
    lcd_write(ord(message[i]),LCD_CHR)


#Begin program
try:
  main()
	  
except KeyboardInterrupt:
  pass
	
finally:
  GPIO.output(BUZZ, True) 
  lcd_write(0x01, LCD_CMD)
  lcd_text("System Exit!",LCD_LINE_1)
  lcd_text("bagube",LCD_LINE_2)
  time.sleep(0.1)
  GPIO.cleanup()
  #os.system("sudo reboot")
  os.system("poweroff")
