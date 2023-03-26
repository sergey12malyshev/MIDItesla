#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script that generates a MIDI signal to the serial port
Author: Malyshev S.E.(https://github.com/sergey12malyshev)
Version = '1.3'
Python version: 3.7.3
Platform: Raspberry PI 3 Model B v1.2
Created: 24.10.2022
Updated: see git histiry
Todo: 
"""
import serial                                     
import time                                       
import RPi.GPIO as GPIO                           
from random import randint                        

# Global variable start:
ser = serial.Serial('/dev/ttyS0', baudrate=31250)

BUZZ_PIN = 17                                                                        
BUTTON_PIN = 2                                    

NOTE_MAX = 71
NOTE_MIN = 36
note = NOTE_MIN

flagUp = True
flagDown = False

melodyNumber = 0
oldmelodyNumber = 0
# Global variable end

GPIO.setwarnings(False)                          # Disable warnings 
GPIO.setmode(GPIO.BCM)       
GPIO.setup(BUZZ_PIN,GPIO.OUT)
GPIO.output(BUZZ_PIN, False)

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Устанавливаем вывод в режим "вход" c подтяжкой

def button_callback(channel):
    # https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
    global melodyNumber
        
    buzzerDrive(0.02)
    melodyNumber += 1
    if melodyNumber == 10:
        melodyNumber = 0
        
    print("Button was pushed!")    
    print(f"Set melody: {melodyNumber}")


def buzzerDrive(timeSleep):
    GPIO.output(BUZZ_PIN, True)
    time.sleep(timeSleep)
    GPIO.output(BUZZ_PIN, False)    
    
    
def playNote(note: int, timeOnLocal: float, timeOffLocal: float):
    global melodyNumber, oldmelodyNumber
    
    NOTE_OFF = 8   # (0x8n) Комманда выключить ноту
    NOTE_ON = 9    # (0x9n) Комманда включить ноту
    velocity = 100 # Сила нажатия клавиши, interrupter её не воспринимает (должна быть больше 0)
    channel = 2    # This represents channel 
    
    def controlInputNotes():
        if note > NOTE_MAX or note < NOTE_MIN:
            print("ERROR value input note")
            buzzerDrive(0.6)
            
    controlInputNotes()    
    ser.write(bytearray([(NOTE_ON << 4) | channel, note, velocity]))
    time.sleep(timeOnLocal)
    ser.write(bytearray([(NOTE_OFF << 4) | channel, note, velocity]))
    time.sleep(timeOffLocal)
    
    print(str(note)+' '+str(timeOnLocal)+' '+str(timeOffLocal))
    
    if oldmelodyNumber != melodyNumber:
        oldmelodyNumber = melodyNumber
        main()


def resetMidi():
    SYS_RESET = 0xFF # Системное сообщение - сброс всех устройств https://ccrma.stanford.edu/~craig/articles/linuxmidi/misc/essenmidi.html
    ser.write(bytearray([SYS_RESET, 0, 0])) # Сдвига на 4 и сложения с номером канала нет т.к. системное сообщение
    time.sleep(0.1)
    
# Melody functions start
def popcorn():
    timeOn = 0.095
    timeOff = 0.135
    
    def popcorn_1tact(timeOnLocal, timeOffLocal): 
        i = 0
        popcorn = [57, 55,  57, 52, 49, 52, 45]  
        while i < len(popcorn):
            playNote(popcorn[i], timeOnLocal, timeOffLocal)
            i += 1
        
    def popcorn_2tact(timeOnLocal, timeOffLocal):
        i = 0
        popcorn = [57, 59, 60, 59, 60, 57,  59, 57, 59, 55,  57, 59, 57, 53,  57]  
        while i < len(popcorn):
            playNote(popcorn[i], timeOnLocal, timeOffLocal)
            i += 1
            
    def popcorn_3tact(timeOnLocal, timeOffLocal):
        i = 0
        popcorn = [57, 59, 60, 59, 60, 57,  59, 57, 59, 55,  57, 55, 57, 59,  60]  
        while i < len(popcorn):
            playNote(popcorn[i], timeOnLocal, timeOffLocal)
            i += 1
    
    def pause():
        time.sleep(timeOff * 1.5)
        
    popcorn_1tact(timeOn, timeOff)
    pause()
    popcorn_1tact(timeOn, timeOff)
    pause()
    popcorn_2tact(timeOn, timeOff)
    pause()
    popcorn_1tact(timeOn, timeOff)
    pause()
    popcorn_1tact(timeOn, timeOff)
    pause()
    popcorn_3tact(timeOn, timeOff)
    pause()
    pause()
     
def mortalKombat():
    timeOn = 0.2
    timeOff = 0.07
    i = 0
    
    mortalKombat = [
        57, 57, 60, 57,  62, 57, 64, 62,   
        60, 60, 64, 60,  67, 60, 64, 60, 
        55, 55, 59, 55,  60, 55, 62, 60,   
        53, 53, 57, 53,  60, 53, 60, 59
        ]
                    
    mortalKombat2 = [
        57, 57, 57, 57, 55, 60,  57, 57, 57, 55, 52,
        57, 57, 57, 57, 55, 60,  57, 57, 57, 57, 57, 57, 57
        ]
    
    while i < len(mortalKombat):
        playNote(mortalKombat[i], timeOn, timeOff)
        i += 1      
           
           
def valcesDogs():
    timeOn = 0.3
    timeOff = 0.1
    i = 0
    
    valcesDogsNote = [
        65, 67, 67, 65, 67, 67,   # this 1 tact 
        64, 67, 67, 64, 67, 67,   # this 2 tact 
        62, 71, 71, 62, 71, 71,   # this 3 tact
        60, 60, 60, 60, 59, 57    # this 4 tact
        ]
    
    
    while i < len(valcesDogsNote):
        playNote(valcesDogsNote[i], timeOn, timeOff)
        i += 1
      
      
def mario():
    timeOn = 0.2
    timeOff = 0.07
    timeOnDiv2 = timeOn / 2
    timeOffMult2 = timeOff * 2
    
    def mario_tact1(timeOn, timeOff):
        playNote(67, timeOnDiv2, timeOff)  
        playNote(66, timeOnDiv2, timeOff)  
        playNote(65, timeOnDiv2, timeOff)  
        playNote(63, timeOnDiv2, timeOffMult2)
        playNote(64, timeOnDiv2, timeOffMult2)
        
    def mario_tact2(timeOn, timeOff):
        playNote(56, timeOnDiv2, timeOff)  
        playNote(57, timeOnDiv2, timeOff)  
        playNote(60, timeOnDiv2, timeOffMult2)
        playNote(57, timeOnDiv2, timeOff)  
        playNote(60, timeOnDiv2, timeOff)  
        playNote(62, timeOnDiv2, timeOff * 4)
        
    def mario_tact3(timeOn, timeOff):
        playNote(60, timeOn, timeOffMult2)  
        playNote(55, timeOnDiv2, timeOff * 4)
        playNote(52, timeOn, timeOffMult2)  
        playNote(57, timeOnDiv2, timeOffMult2)
        playNote(59, timeOnDiv2, timeOffMult2)
        playNote(58, timeOnDiv2, timeOff)  
        playNote(57, timeOn, timeOff)    

    playNote(64, timeOnDiv2, timeOff)  
    playNote(64, timeOnDiv2, timeOffMult2)
    playNote(64, timeOnDiv2, timeOffMult2)
    playNote(60, timeOnDiv2, timeOff)  
    playNote(64, timeOn, timeOff)    

    playNote(67, timeOn * 2, timeOffMult2)
    playNote(55, timeOn * 2, timeOffMult2)

    mario_tact3(timeOn, timeOff)

    playNote(55, timeOn * 3 / 4, timeOff)
    playNote(64, timeOn * 3 / 4, timeOff)
    playNote(67, timeOn * 3 / 4, timeOff)
    playNote(69, timeOn, timeOff)    
    playNote(65, timeOnDiv2, timeOff)  
    playNote(67, timeOnDiv2, timeOffMult2)

    playNote(64, timeOnDiv2, timeOffMult2)
    playNote(60, timeOnDiv2, timeOff)  
    playNote(62, timeOnDiv2, timeOff)  
    playNote(59, timeOnDiv2, timeOff * 4)

    mario_tact3(timeOn, timeOff)

    playNote(55, timeOn * 2 / 3, timeOff)
    playNote(64, timeOn * 2 / 3, timeOff)
    playNote(67, timeOn * 2 / 3, timeOff)
    playNote(69, timeOn, timeOff)    
    playNote(65, timeOnDiv2, timeOff)  
    playNote(67, timeOnDiv2, timeOffMult2)

    playNote(64, timeOnDiv2, timeOffMult2)
    playNote(60, timeOnDiv2, timeOff)  
    playNote(62, timeOnDiv2, timeOff)  
    playNote(59, timeOnDiv2, timeOff * 8)

    mario_tact1(timeOn, timeOff)
    mario_tact2(timeOn, timeOff)
    mario_tact1(timeOn, timeOff)

    playNote(60, timeOnDiv2, timeOffMult2)
    playNote(60, timeOnDiv2, timeOff)  
    playNote(60, timeOn, timeOff * 8)  

    mario_tact1(timeOn, timeOff)
    mario_tact2(timeOn, timeOff)

    playNote(63, timeOn, timeOffMult2)  
    playNote(62, timeOnDiv2, timeOff * 4)

    playNote(60, timeOn, timeOff * 12) 
    
    
def imperialMarch():
    timeOn = 0.35
    timeOff = 0.18
    timeOnDiv2 = timeOn / 2
    timeOnDiv4 = timeOn / 4
    timeOffDiv2 = timeOff / 2
    
    def imperialMarch_tact(timeOn, timeOff):
        playNote(67, timeOn, timeOff)       
        playNote(55, timeOn * 0.75, timeOffDiv2)
        playNote(55, timeOnDiv4, timeOffDiv2)   
        playNote(67, timeOn, timeOff)       
        playNote(66, timeOn * 0.75, timeOffDiv2)
        playNote(65, timeOnDiv4, timeOffDiv2)   
    
        playNote(64, timeOnDiv4, timeOffDiv2)            
        playNote(63, timeOnDiv4, timeOffDiv2)   
        playNote(64, timeOnDiv2, timeOff * 2)   
        playNote(56, timeOnDiv2, timeOffDiv2)   
        playNote(61, timeOn, timeOff)       
        playNote(60, timeOn * 0.75, timeOffDiv2)
        playNote(59, timeOnDiv4, timeOffDiv2)   
    
        playNote(58, timeOnDiv4, timeOffDiv2)          
        playNote(57, timeOnDiv4, timeOffDiv2)   
        playNote(58, timeOnDiv2, timeOff * 2)   
        playNote(51, timeOnDiv2, timeOffDiv2)   
        playNote(54, timeOn, timeOff)       
        playNote(51, timeOn * 0.75, timeOffDiv2)
        playNote(54, timeOnDiv4, timeOffDiv2)   
    
    def imperialMarch_tact2(timeOn, timeOff):
        playNote(55, timeOn, timeOff)       
        playNote(51, timeOn * 0.75, timeOffDiv2)
        playNote(58, timeOnDiv4, timeOffDiv2)   
        playNote(55, timeOn * 2, timeOff * 2)       
        
    # this 1 tact
    playNote(55, timeOn, timeOff)       
    playNote(55, timeOn, timeOff)       
    playNote(55, timeOn, timeOff)       
    playNote(51, timeOn * 0.75, timeOffDiv2)
    playNote(58, timeOnDiv4, timeOffDiv2)   
    # this 2 tact
    imperialMarch_tact2(timeOn, timeOff)
    # this 3 tact
    playNote(62, timeOn, timeOff)       
    playNote(62, timeOn, timeOff)       
    playNote(62, timeOn, timeOff)       
    playNote(63, timeOn * 0.75, timeOffDiv2)
    playNote(58, timeOnDiv4, timeOffDiv2)   
    # this 4 tact
    playNote(54, timeOn, timeOff)       
    playNote(51, timeOn * 0.75, timeOffDiv2)
    playNote(58, timeOnDiv4, timeOffDiv2)   
    playNote(55, timeOn * 2, timeOff * 2)   
    # this 5 tact and 6 tact and 7 tact
    imperialMarch_tact(timeOn, timeOff) 
    # this 8 tact
    playNote(59, timeOn, timeOff)       
    playNote(55, timeOn * 0.75, timeOffDiv2)
    playNote(59, timeOnDiv4, timeOffDiv2)   
    playNote(62, timeOn * 2, timeOff * 2)   
    # this 9 and 10 and 11 tact
    imperialMarch_tact(timeOn, timeOff) 
    # this 12 tact
    imperialMarch_tact2(timeOn, timeOff)

def missionImpossible():
    timeOn = 0.25
    timeOff = 0.09
    timeOnDiv2 = timeOn / 2
    timeOffDiv2 = timeOff / 2
    i = 0
    
    def tact1():
        playNote(55, timeOn, timeOff * 2)  
        playNote(55, timeOnDiv2, timeOff * 4)      
        playNote(58, timeOn, timeOff)    
        playNote(60, timeOn, timeOff)    
    
        playNote(55, timeOn, timeOff * 2)  
        playNote(55, timeOnDiv2, timeOff * 4)  
        playNote(53, timeOn, timeOff)    
        playNote(54, timeOn, timeOff)    
    
    def solo1():
        playNote(70, timeOnDiv2, timeOff)    
        playNote(67, timeOnDiv2, timeOff)    
        playNote(62, timeOn * 4, timeOff)    
        playNote(58, timeOn, timeOff)      
        playNote(60, timeOn, timeOff)      
    
    def solo2():
        playNote(70, timeOnDiv2, timeOff)    
        playNote(67, timeOnDiv2, timeOff)    
        playNote(61, timeOn * 4, timeOff)    
        playNote(53, timeOn, timeOff)      
        playNote(54, timeOn, timeOff)
        
    def solo3():
        playNote(70, timeOnDiv2, timeOff)    
        playNote(67, timeOnDiv2, timeOff)    
        playNote(60, timeOn * 4, timeOff)    
        playNote(58, timeOn, timeOff)      
        playNote(60, timeOn, timeOff)
        
    def solo4():
        playNote(58, timeOnDiv2, timeOff)    
        playNote(60, timeOn, timeOff)    
        playNote(55, timeOn + (timeOnDiv2), timeOff)    
        playNote(55, timeOnDiv2, timeOff * 4)  
        playNote(53, timeOn, timeOff)    
        playNote(54, timeOn, timeOff)  
        
    while i < 8: 
        playNote(62, 0.1, 0.01)
        i += 1     
    playNote(62, timeOnDiv2, timeOffDiv2)
    playNote(64, timeOnDiv2, timeOffDiv2)
    playNote(65, timeOnDiv2, timeOffDiv2)
    playNote(66, timeOnDiv2, timeOffDiv2)
    
    tact1()
    tact1() 
    solo1()
    solo2()
    solo3()
    solo4()
    tact1()
    
    
def omen():
    timeOn = 0.33
    timeOff = 0.05
    timeOnDiv2 = timeOn / 2
    timeOnDiv4 = timeOn / 4 
    
    def oneTact():
        playNote(59, timeOn + (timeOnDiv2), timeOff)
        playNote(70, timeOnDiv2, timeOff)
        playNote(71, timeOnDiv2, timeOff)
        playNote(70, timeOnDiv2, timeOff)
        playNote(71, timeOnDiv2, timeOff)
        playNote(70, timeOnDiv2, timeOff)
    
    def twoTact():
        playNote(59, timeOnDiv2, timeOff)
        playNote(65, timeOnDiv2, timeOff)
        playNote(59, timeOnDiv2, timeOff)
        playNote(62, timeOnDiv4, timeOff)
        playNote(60, timeOnDiv4, timeOff)
         
    oneTact()
    playNote(62, timeOn + (timeOnDiv2), timeOff)
    playNote(61, timeOnDiv2, timeOff)
    playNote(62, timeOnDiv2, timeOff)
    playNote(61, timeOnDiv2, timeOff)
    playNote(62, timeOnDiv2, timeOff)
    playNote(66, timeOnDiv2, timeOff)
    oneTact()
    playNote(59, timeOn + (timeOnDiv2), timeOff)
    playNote(70, timeOnDiv2, timeOff)
    playNote(71, timeOnDiv2, timeOff)
    playNote(70, timeOnDiv2, timeOff)
    playNote(71, timeOnDiv2, timeOff)
    playNote(70, timeOnDiv2, timeOff * 1.2)
    
   
def test_ladderNotes():
    global note, flagUp, flagDown
    
    timeOn = 0.12
    timeOff = 0.07
    
    if flagUp:
        note += 1
        if (note >= NOTE_MAX):
            note = NOTE_MAX
            flagUp = False
            flagDown = True
      
    if flagDown:
        note -= 1
        if (note <= NOTE_MIN):
            note = NOTE_MIN
            flagUp = True
            flagDown = False
    
    playNote(note, timeOn, timeOff)
 
 
def randomNotes():
    random_note = randint(36,71)
    playNote(random_note, 0.5, 0.05)
# Melody functions end

GPIO.add_event_detect(2, GPIO.FALLING, callback=button_callback, bouncetime=250)


def main():
    while True:
        mN = melodyNumber 
        
        if (mN == 0):
            mortalKombat()
        elif (mN == 1):
            mario()
        elif (mN == 2):
            imperialMarch()  
        elif (mN == 3):
            valcesDogs()
        elif (mN == 4):
            popcorn()
        elif (mN == 5):
            omen()
        elif (mN == 6):
            missionImpossible()
        elif (mN == 7):
            test_ladderNotes()
        elif (mN == 8):
            randomNotes()
        else:
            resetMidi()
 
try:                                    
    main()
    
except:                                                                   
    GPIO.cleanup()                      
                                           
    print("Программа завершена, "        
          "выводы GPIO возвращены "     
          "в исходное состояние.")      
        
 