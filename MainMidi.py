#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script that generates a MIDI signal to the serial port
Author: Malyshev S.E.(https://github.com/sergey12malyshev)
Version = '1.1'
Created: 24.10.2022
Updated: see git histiry
Todo: 
"""
import serial                                     
import time                                       
import RPi.GPIO as GPIO                           
from random import randint                        

# Global variable start:
BUZZ_PIN = 17                                                                        
BUTTON_PIN = 2                                    

ser = serial.Serial('/dev/ttyS0', baudrate=31250)
note = 36 #max 71 min 36

flagUp = True
flagDown = False

melodyNumber = 0
oldmelodyNumber = 0
# Global variable end

GPIO.setwarnings(False)                          #disable warnings 
GPIO.setmode(GPIO.BCM)       
GPIO.setup(BUZZ_PIN,GPIO.OUT)
GPIO.output(BUZZ_PIN, False)

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Устанавливаем вывод в режим "вход" c подтяжкой

def button_callback(channel):
    global melodyNumber
        
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:
        time.sleep(0.09)
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            GPIO.output(BUZZ_PIN, True)
            time.sleep(0.02)
            GPIO.output(BUZZ_PIN, False)
        
            melodyNumber = melodyNumber + 1
            if melodyNumber == 8:
                melodyNumber = 0
        
            print(f"Set melody: {melodyNumber}")
    print("Button was pushed!")
    

def playNote(note: int, timeOnLocal: float, timeOffLocal: float):
    global melodyNumber, oldmelodyNumber
    
    NOTE_OFF = 8   # (0x8n) Комманда выключить ноту
    NOTE_ON = 9    # (0x9n) Комманда включить ноту
    velocity = 100 # сила нажатия клавиши, interrupter её не воспринимает (должна быть больше 0)
    channel = 2    # this represents channel 
    
    ser.write(bytearray([(NOTE_ON << 4) | channel, note, velocity]))
    time.sleep(timeOnLocal)
    ser.write(bytearray([(NOTE_OFF << 4) | channel, note, velocity]))
    time.sleep(timeOffLocal)
    
    print(str(note)+' '+str(timeOnLocal)+' '+str(timeOffLocal))
    
    if oldmelodyNumber != melodyNumber:
        oldmelodyNumber = melodyNumber
        return 1
    return 0

# melody functions start
def popcorn():
    timeOn = 0.095
    timeOff = 0.135
    
    def popcorn_1tact(timeOnLocal, timeOffLocal): # python поддерживает вложенные функции
        i = 0
        popcorn = [57, 55,  57, 52, 49, 52, 45]   # список нот
        while i < len(popcorn):
            if playNote(popcorn[i], timeOnLocal, timeOffLocal): 
                return 1
            i += 1
        
    def popcorn_2tact(timeOnLocal, timeOffLocal):
        i = 0
        popcorn = [57, 59, 60, 59, 60, 57,  59, 57, 59, 55,  57, 59, 57, 53,  57]  
        while i < len(popcorn):
            if playNote(popcorn[i], timeOnLocal, timeOffLocal): 
                return 1
            i += 1
            
    def popcorn_3tact(timeOnLocal, timeOffLocal):
        i = 0
        popcorn = [57, 59, 60, 59, 60, 57,  59, 57, 59, 55,  57, 55, 57, 59,  60]  
        while i < len(popcorn):
            if playNote(popcorn[i], timeOnLocal, timeOffLocal): 
                return 1
            i += 1
    
    if popcorn_1tact(timeOn, timeOff):return 1
    time.sleep(timeOff*1.5)
    if popcorn_1tact(timeOn, timeOff):return 1
    time.sleep(timeOff*1.5)
    if popcorn_2tact(timeOn, timeOff):return 1
    time.sleep(timeOff*1.5)
    if popcorn_1tact(timeOn, timeOff):return 1
    time.sleep(timeOff*1.5)
    if popcorn_1tact(timeOn, timeOff):return 1
    time.sleep(timeOff*1.5)
    if popcorn_3tact(timeOn, timeOff):return 1
    time.sleep(timeOff*1.6)
    
def mortalKombat():
    timeOn = 0.2
    timeOff = 0.07
    i = 0
    
    mortalKombat = [
    57, 57, 60, 57,  62, 57, 64, 62,   
    60, 60, 64, 60,  67, 60, 64, 60, 
    55, 55, 59, 55,  60, 55, 62, 60,   
    53, 53, 57, 53,  60, 53, 60, 59]
                    
    mortalKombat2 = [
    57, 57, 57, 57, 55, 60,  57, 57, 57, 55, 52,
    57, 57, 57, 57, 55, 60,  57, 57, 57, 57, 57, 57, 57]
    
    while i < len(mortalKombat):
        if playNote(mortalKombat[i], timeOn, timeOff): 
            return 1
        i += 1      
           
def valcesDogs():
    timeOn = 0.3
    timeOff = 0.1
    i = 0
    
    valcesDogsNote = [
    65, 67, 67, 65, 67, 67,   # this 1 tact 
    64, 67, 67, 64, 67, 67,   # this 2 tact 
    62, 71, 71, 62, 71, 71,   # this 3 tact
    60, 60, 60, 60, 59, 57]   # this 4 tact
    
    while i < len(valcesDogsNote):
        if playNote(valcesDogsNote[i], timeOn, timeOff): 
            return 1
        i += 1
          
def mario():
    timeOn = 0.2
    timeOff = 0.07
    
    def mario_tact1(timeOn, timeOff):
        if playNote(67, timeOn/2, timeOff)  :return 1
        if playNote(66, timeOn/2, timeOff)  :return 1
        if playNote(65, timeOn/2, timeOff)  :return 1
        if playNote(63, timeOn/2, timeOff*2):return 1
        if playNote(64, timeOn/2, timeOff*2):return 1
        
    def mario_tact2(timeOn, timeOff):
        if playNote(56, timeOn/2, timeOff)  :return 1
        if playNote(57, timeOn/2, timeOff)  :return 1
        if playNote(60, timeOn/2, timeOff*2):return 1
        if playNote(57, timeOn/2, timeOff)  :return 1
        if playNote(60, timeOn/2, timeOff)  :return 1
        if playNote(62, timeOn/2, timeOff*4):return 1
        
    def mario_tact3(timeOn, timeOff):
        if playNote(60, timeOn, timeOff*2)  :return 1
        if playNote(55, timeOn/2, timeOff*4):return 1
        if playNote(52, timeOn, timeOff*2)  :return 1
        if playNote(57, timeOn/2, timeOff*2):return 1
        if playNote(59, timeOn/2, timeOff*2):return 1
        if playNote(58, timeOn/2, timeOff)  :return 1
        if playNote(57, timeOn, timeOff)    :return 1

    if playNote(64, timeOn/2, timeOff)  :return 1
    if playNote(64, timeOn/2, timeOff*2):return 1
    if playNote(64, timeOn/2, timeOff*2):return 1
    if playNote(60, timeOn/2, timeOff)  :return 1
    if playNote(64, timeOn, timeOff)    :return 1

    if playNote(67, timeOn*2, timeOff*2):return 1
    if playNote(55, timeOn*2, timeOff*2):return 1

    if mario_tact3(timeOn, timeOff):     return 1

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

    if mario_tact3(timeOn, timeOff):return 1

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

    if mario_tact1(timeOn, timeOff):     return 1
    if mario_tact2(timeOn, timeOff):     return 1
    if mario_tact1(timeOn, timeOff):     return 1

    if playNote(60, timeOn/2, timeOff*2):return 1
    if playNote(60, timeOn/2, timeOff)  :return 1
    if playNote(60, timeOn, timeOff*8)  :return 1

    if mario_tact1(timeOn, timeOff):     return 1
    if mario_tact2(timeOn, timeOff):     return 1

    if playNote(63, timeOn, timeOff*2)  :return 1
    if playNote(62, timeOn/2, timeOff*4):return 1

    if playNote(60, timeOn, timeOff*12) :return 1
    
    
def imperialMarch():
    timeOn = 0.35
    timeOff = 0.18
    
    def imperialMarch_tact(timeOn, timeOff):
        if playNote(67, timeOn, timeOff)       :return 1
        if playNote(55, timeOn*0.75, timeOff/2):return 1
        if playNote(55, timeOn/4, timeOff/2)   :return 1
        if playNote(67, timeOn, timeOff)       :return 1
        if playNote(66, timeOn*0.75, timeOff/2):return 1
        if playNote(65, timeOn/4, timeOff/2)   :return 1
    
        if playNote(64, timeOn/4, timeOff/2)   :return 1         
        if playNote(63, timeOn/4, timeOff/2)   :return 1
        if playNote(64, timeOn/2, timeOff*2)   :return 1
        if playNote(56, timeOn/2, timeOff/2)   :return 1
        if playNote(61, timeOn, timeOff)       :return 1
        if playNote(60, timeOn*0.75, timeOff/2):return 1
        if playNote(59, timeOn/4, timeOff/2)   :return 1
    
        if playNote(58, timeOn/4, timeOff/2)   :return 1       
        if playNote(57, timeOn/4, timeOff/2)   :return 1
        if playNote(58, timeOn/2, timeOff*2)   :return 1
        if playNote(51, timeOn/2, timeOff/2)   :return 1
        if playNote(54, timeOn, timeOff)       :return 1
        if playNote(51, timeOn*0.75, timeOff/2):return 1
        if playNote(54, timeOn/4, timeOff/2)   :return 1
    
    def imperialMarch_tact2(timeOn, timeOff):
        if playNote(55, timeOn, timeOff)       :return 1
        if playNote(51, timeOn*0.75, timeOff/2):return 1
        if playNote(58, timeOn/4, timeOff/2)   :return 1
        if playNote(55, timeOn*2, timeOff*2)   :return 1    
        
    # this 1 tact
    if playNote(55, timeOn, timeOff)       :return 1
    if playNote(55, timeOn, timeOff)       :return 1
    if playNote(55, timeOn, timeOff)       :return 1
    if playNote(51, timeOn*0.75, timeOff/2):return 1
    if playNote(58, timeOn/4, timeOff/2)   :return 1
    # this 2 tact
    if imperialMarch_tact2(timeOn, timeOff):return 1
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
    # this 5 tact and 6 tact and 7 tact
    if imperialMarch_tact(timeOn, timeOff) :return 1
    # this 8 tact
    if playNote(59, timeOn, timeOff)       :return 1
    if playNote(55, timeOn*0.75, timeOff/2):return 1
    if playNote(59, timeOn/4, timeOff/2)   :return 1
    if playNote(62, timeOn*2, timeOff*2)   :return 1
    # this 9 and 10 and 11 tact
    if imperialMarch_tact(timeOn, timeOff) :return 1
    # this 12 tact
    if imperialMarch_tact2(timeOn, timeOff):return 1

def test_ladderNotes():
    global note, flagUp, flagDown
    
    timeOn = 0.12
    timeOff = 0.07
    
    if flagUp:
        note +=1
        if (note >= 71):
            note = 71
            flagUp = False
            flagDown = True
      
    if flagDown:
        note -=1
        if (note <= 36):
            note = 36
            flagUp = True
            flagDown = False
    
    if playNote(note, timeOn, timeOff) :return 1
           
def randomNotes():
    random_note = randint(36,71)
    playNote(random_note, 0.5, 0.05)
# melody functions end
       
def disable():
    SYS_RESET = 0xFF #Системное сообщение - сброс всех устройств https://ccrma.stanford.edu/~craig/articles/linuxmidi/misc/essenmidi.html
    ser.write(bytearray([SYS_RESET, 0, 0])) # Сдвига на 4 и сложения с номером канала нет т.к. системное сообщение
    time.sleep(0.1)                                    
       
GPIO.add_event_detect(2, GPIO.FALLING, callback = button_callback)    
try:                                    # Пытаемся выполнить следующий код:
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
            test_ladderNotes()
        elif (mN == 6):
            randomNotes()
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
        
