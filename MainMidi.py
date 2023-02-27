#! /usr/bin/env python
# -*- coding: utf-8 -*-
import serial                                     # Подключаем модуль для работы с uart
import time                                       # Подключаем модуль для работы со временем
import RPi.GPIO as GPIO                           # Подключаем модуль для работы с GPIO
from random import randint
 
BUZZ_PIN = 17                                     # Pin buzzer                                     
BUTTON_PIN = 2                                    # Pin button

ser = serial.Serial('/dev/ttyS0', baudrate=31250)
channel = 2 # this represents channel 

note = 36 #max 71 min 36
velocity = 100
note_off = 8
note_on = 9

# Test variable:
flagUp = 1
flagDown = 0

melodiNumber = 0
oldMelodiNumber = 0

GPIO.setwarnings(False)                          #disable warnings 
GPIO.setmode(GPIO.BCM)       
GPIO.setup(BUZZ_PIN,GPIO.OUT)
GPIO.output(BUZZ_PIN, False)

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Устанавливаем вывод в режим "вход" c подтяжкой

def button_callback(channel):
    global melodiNumber
        
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:
      time.sleep(0.09)
      if GPIO.input(BUTTON_PIN) == GPIO.LOW:
        GPIO.output(BUZZ_PIN, True)
        time.sleep(0.02)
        GPIO.output(BUZZ_PIN, False)
        
        melodiNumber = melodiNumber + 1
        if melodiNumber == 6:
          melodiNumber = 0
        
        print(melodiNumber)
    print("Button was pushed!")
    

def playNote(note, timeOnLocal, timeOffLocal):
    
    global melodiNumber
    global oldMelodiNumber
    
    ser.write(bytearray([(note_on << 4) | channel, note, velocity]))
    time.sleep(timeOnLocal)
    ser.write(bytearray([(note_off << 4) | channel, note, velocity]))
    time.sleep(timeOffLocal)
    
    print(str(note)+' '+str(timeOnLocal)+' '+str(timeOffLocal))
    
    if oldMelodiNumber != melodiNumber:
      oldMelodiNumber = melodiNumber
      return 1
    return 0
    
def valcesDogs():
    
        timeOn = 0.3
        timeOff = 0.1
        
        if playNote(65, timeOn, timeOff):return 1   
        if playNote(67, timeOn, timeOff):return 1                 
        if playNote(67, timeOn, timeOff):return 1
        if playNote(65, timeOn, timeOff):return 1   
        if playNote(67, timeOn, timeOff):return 1   
        if playNote(67, timeOn, timeOff):return 1 
            

        if playNote(64, timeOn, timeOff):return 1 
        if playNote(67, timeOn, timeOff):return 1 
        if playNote(67, timeOn, timeOff):return 1 
        if playNote(64, timeOn, timeOff):return 1 
        if playNote(67, timeOn, timeOff):return 1 
        if playNote(67, timeOn, timeOff):return 1 
          
        if playNote(62, timeOn, timeOff):return 1 
        if playNote(71, timeOn, timeOff):return 1  
        if playNote(71, timeOn, timeOff):return 1 
        if playNote(62, timeOn, timeOff):return 1  
        if playNote(71, timeOn, timeOff):return 1 
        if playNote(71, timeOn, timeOff):return 1 
      
        if playNote(60, timeOn, timeOff):return 1 
        if playNote(60, timeOn, timeOff):return 1
        if playNote(60, timeOn, timeOff):return 1 
        if playNote(60, timeOn, timeOff):return 1 
        if playNote(59, timeOn, timeOff):return 1  
        if playNote(57, timeOn, timeOff):return 1
              

def mario():
    
        timeOn = 0.2
        timeOff = 0.07
        
        if playNote(64, timeOn/2, timeOff)  :return 1
        if playNote(64, timeOn/2, timeOff*2):return 1
        if playNote(64, timeOn/2, timeOff*2):return 1
        if playNote(60, timeOn/2, timeOff)  :return 1
        if playNote(64, timeOn, timeOff)    :return 1

        if playNote(67, timeOn*2, timeOff*2):return 1
        if playNote(55, timeOn*2, timeOff*2):return 1

        if playNote(60, timeOn, timeOff*2)  :return 1
        if playNote(55, timeOn/2, timeOff*4):return 1
        if playNote(52, timeOn, timeOff*2)  :return 1

        if playNote(57, timeOn/2, timeOff*2):return 1
        if playNote(59, timeOn/2, timeOff*2):return 1
        if playNote(58, timeOn/2, timeOff)  :return 1
        if playNote(57, timeOn, timeOff)    :return 1

        if playNote(55, timeOn*3/4, timeOff):return 1
        if playNote(64, timeOn*3/4, timeOff):return 1
        if playNote(67, timeOn*3/4, timeOff):return 1
        if playNote(69, timeOn, timeOff)    :return 1
        if playNote(65, timeOn/2, timeOff)  :return 1
        if playNote(67, timeOn/2, timeOff*2):return 1

        if playNote(64, timeOn/2, timeOff*2):return 1
        if playNote(60, timeOn/2, timeOff)  :return 1
        if playNote(62, timeOn/2, timeOff)  :return 1
        if playNote(59, timeOn/2, timeOff*4):return 1

        if playNote(60, timeOn, timeOff*2)  :return 1
        if playNote(55, timeOn/2, timeOff*4):return 1
        if playNote(52, timeOn, timeOff*2)  :return 1

        if playNote(57, timeOn/2, timeOff*2):return 1
        if playNote(59, timeOn/2, timeOff*2):return 1
        if playNote(58, timeOn/2, timeOff)  :return 1
        if playNote(57, timeOn, timeOff)    :return 1

        if playNote(55, timeOn*2/3, timeOff):return 1
        if playNote(64, timeOn*2/3, timeOff):return 1
        if playNote(67, timeOn*2/3, timeOff):return 1
        if playNote(69, timeOn, timeOff)    :return 1
        if playNote(65, timeOn/2, timeOff)  :return 1
        if playNote(67, timeOn/2, timeOff*2):return 1

        if playNote(64, timeOn/2, timeOff*2):return 1
        if playNote(60, timeOn/2, timeOff)  :return 1
        if playNote(62, timeOn/2, timeOff)  :return 1
        if playNote(59, timeOn/2, timeOff*8):return 1

        if playNote(67, timeOn/2, timeOff)  :return 1
        if playNote(66, timeOn/2, timeOff)  :return 1
        if playNote(65, timeOn/2, timeOff)  :return 1
        if playNote(63, timeOn/2, timeOff*2):return 1
        if playNote(64, timeOn/2, timeOff*2):return 1

        if playNote(56, timeOn/2, timeOff)  :return 1
        if playNote(57, timeOn/2, timeOff)  :return 1
        if playNote(60, timeOn/2, timeOff*2):return 1
        if playNote(57, timeOn/2, timeOff)  :return 1
        if playNote(60, timeOn/2, timeOff)  :return 1
        if playNote(62, timeOn/2, timeOff*4):return 1

        if playNote(67, timeOn/2, timeOff)  :return 1
        if playNote(66, timeOn/2, timeOff)  :return 1
        if playNote(65, timeOn/2, timeOff)  :return 1
        if playNote(63, timeOn/2, timeOff*2):return 1
        if playNote(64, timeOn/2, timeOff*2):return 1

        if playNote(60, timeOn/2, timeOff*2):return 1
        if playNote(60, timeOn/2, timeOff)  :return 1
        if playNote(60, timeOn, timeOff*8)  :return 1

        if playNote(67, timeOn/2, timeOff)  :return 1
        if playNote(66, timeOn/2, timeOff)  :return 1
        if playNote(65, timeOn/2, timeOff)  :return 1
        if playNote(63, timeOn/2, timeOff*2):return 1
        if playNote(64, timeOn/2, timeOff*2):return 1

        if playNote(56, timeOn/2, timeOff)  :return 1
        if playNote(57, timeOn/2, timeOff)  :return 1
        if playNote(60, timeOn/2, timeOff*2):return 1
        if playNote(57, timeOn/2, timeOff)  :return 1
        if playNote(60, timeOn/2, timeOff)  :return 1
        if playNote(62, timeOn/2, timeOff*4):return 1

        if playNote(63, timeOn, timeOff*2)  :return 1
        if playNote(62, timeOn/2, timeOff*4):return 1

        if playNote(60, timeOn, timeOff*12) :return 1
    
def test():
        global note, flagUp, flagDown
        timeOn = 0.12
        timeOff = 0.07
        
        if flagUp == 1:
            
         note +=1
         if (note >= 71):
          flagUp = 71
          flagDown = 1
          
        if flagDown == 1:
         note -=1
         if (note <= 36):
          note = 36
          flagUp = 1
          flagDown = 0
        
        if playNote(note, timeOn, timeOff) :return 1

def imperialMarch():
    
        timeOn = 0.35
        timeOff = 0.18
        # this 1 tact
        if playNote(55, timeOn, timeOff)       :return 1
        if playNote(55, timeOn, timeOff)       :return 1
        if playNote(55, timeOn, timeOff)       :return 1
        if playNote(51, timeOn*0.75, timeOff/2):return 1
        if playNote(58, timeOn/4, timeOff/2)   :return 1
        # this 2 tact
        if playNote(55, timeOn, timeOff)       :return 1
        if playNote(51, timeOn*0.75, timeOff/2):return 1
        if playNote(58, timeOn/4, timeOff/2)   :return 1
        if playNote(55, timeOn*2, timeOff*2)   :return 1
        # this 3 tact
        if playNote(62, timeOn, timeOff)       :return 1
        if playNote(62, timeOn, timeOff)       :return 1
        if playNote(62, timeOn, timeOff)       :return 1
        if playNote(63, timeOn*0.75, timeOff/2):return 1
        if playNote(58, timeOn/4, timeOff/2)   :return 1
        # this 4 tact
        if playNote(54, timeOn, timeOff)       :return 1
        if playNote(51, timeOn*0.75, timeOff/2):return 1
        if playNote(58, timeOn/4, timeOff/2)   :return 1
        if playNote(55, timeOn*2, timeOff*2)   :return 1
        # this 5 tact
        if playNote(67, timeOn, timeOff)       :return 1
        if playNote(55, timeOn*0.75, timeOff/2):return 1
        if playNote(55, timeOn/4, timeOff/2)   :return 1
        if playNote(67, timeOn, timeOff)       :return 1
        if playNote(66, timeOn*0.75, timeOff/2):return 1
        if playNote(65, timeOn/4, timeOff/2)   :return 1
        # this 6 tact
        if playNote(64, timeOn/4, timeOff/2)   :return 1       
        if playNote(63, timeOn/4, timeOff/2)   :return 1
        if playNote(64, timeOn/2, timeOff*2)   :return 1
        if playNote(56, timeOn/2, timeOff/2)   :return 1
        if playNote(61, timeOn, timeOff)       :return 1
        if playNote(60, timeOn*0.75, timeOff/2):return 1
        if playNote(59, timeOn/4, timeOff/2)   :return 1
        # this 7 tact
        if playNote(58, timeOn/4, timeOff/2)   :return 1       
        if playNote(57, timeOn/4, timeOff/2)   :return 1
        if playNote(58, timeOn/2, timeOff*2)   :return 1
        if playNote(51, timeOn/2, timeOff/2)   :return 1
        if playNote(54, timeOn, timeOff)       :return 1
        if playNote(51, timeOn*0.75, timeOff/2):return 1
        if playNote(54, timeOn/4, timeOff/2)   :return 1
        # this 8 tact
        if playNote(59, timeOn, timeOff)       :return 1
        if playNote(55, timeOn*0.75, timeOff/2):return 1
        if playNote(59, timeOn/4, timeOff/2)   :return 1
        if playNote(62, timeOn*2, timeOff*2)   :return 1
        # this 9 tact
        if playNote(67, timeOn, timeOff)       :return 1
        if playNote(55, timeOn*0.75, timeOff/2):return 1
        if playNote(55, timeOn/4, timeOff/2)   :return 1
        if playNote(67, timeOn, timeOff)       :return 1
        if playNote(66, timeOn*0.75, timeOff/2):return 1
        if playNote(65, timeOn/4, timeOff/2)   :return 1
        # this 10 tact
        if playNote(64, timeOn/4, timeOff/2)   :return 1         
        if playNote(63, timeOn/4, timeOff/2)   :return 1
        if playNote(64, timeOn/2, timeOff*2)   :return 1
        if playNote(56, timeOn/2, timeOff/2)   :return 1
        if playNote(61, timeOn, timeOff)       :return 1
        if playNote(60, timeOn*0.75, timeOff/2):return 1
        if playNote(59, timeOn/4, timeOff/2)   :return 1
        # this 11 tact
        if playNote(58, timeOn/4, timeOff/2)   :return 1       
        if playNote(57, timeOn/4, timeOff/2)   :return 1
        if playNote(58, timeOn/2, timeOff*2)   :return 1
        if playNote(51, timeOn/2, timeOff/2)   :return 1
        if playNote(54, timeOn, timeOff)       :return 1
        if playNote(51, timeOn*0.75, timeOff/2):return 1
        if playNote(54, timeOn/4, timeOff/2)   :return 1
        # this 12 tact
        if playNote(55, timeOn, timeOff)       :return 1
        if playNote(51, timeOn*0.75, timeOff/2):return 1
        if playNote(58, timeOn/4, timeOff/2)   :return 1
        if playNote(55, timeOn*2, timeOff*2)   :return 1
           
def random():
       random_note = randint(36,71)
       playNote(random_note, 0.12, 0.07)
       
def disable():
       ser.write(bytearray([(note_off << 4) | channel, 40, velocity]))
       
       
GPIO.add_event_detect(2,GPIO.FALLING,callback=button_callback)    
try:                                    # Пытаемся выполнить следующий код:
  while True:
        if (melodiNumber == 0):
           valcesDogs()
        else:
         if (melodiNumber == 1):
           mario()
         else:
          if (melodiNumber == 2):
            imperialMarch()
          else:
            if (melodiNumber == 3):
              test()
            else:
             if (melodiNumber == 4):
               random()
             else:
               disable()

except:                                 # Если код выполнить не удалось
                                        #   (поднято исключение или
                                        #    другое прерывание выполнения)
    GPIO.cleanup()                      #   Возвращаем выводы в
                                        #   исходное состояние.
    print("Программа завершена, "       #   Выводим сообщение.
          "выводы GPIO возвращены "     #
          "в исходное состояние.")      #
        
