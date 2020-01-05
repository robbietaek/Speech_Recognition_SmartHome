#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import print_function

import argparse
import json
import os.path
import pathlib2 as pathlib
import click
import google.oauth2.credentials
import RPi.GPIO as GPIO
import time
import pygame
import subprocess

from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file
from google.assistant.library.device_helpers import register_device


#이게 보니까 핀번호가 아니고 GPIO번호다. GPIO가 혹시 겹치면 그냥 내맘대로빈자리로 바꿔주면 된다.
servoPIN = 17
servoPIN1 = 27
control_pins = [23,24,8,7]
channel = 19

#이 부분도 그냥 위에 GPIO번호만 안 겹치면 오류가 안 남.
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)  #창문 서보모터
GPIO.setup(servoPIN1, GPIO.OUT)  #강아지 입 서보모터
GPIO.setup(21 ,GPIO.OUT) #불켜기
GPIO.setup(20 ,GPIO.OUT) #불켜기
GPIO.setup(26 ,GPIO.OUT) #에어컨
GPIO.setup(channel, GPIO.OUT)

p = GPIO.PWM(servoPIN, 40)
q = GPIO.PWM(servoPIN1, 30)


try:
    FileNotFoundError


except NameError:
    FileNotFoundError = IOError




def process_event(event, assistant, subprocess):

    if event.type == EventType.ON_ALERT_STARTED:
        assistant.stop_conversation()
        pygame.init()
        pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/drug.wav")
        pygame.mixer.music.play()


    if event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        print()
        q.start(15)
        try:
          q.ChangeDutyCycle(0.5)
        except:
          q.stop()
          GPIO.cleanup()
        pygame.init()
        pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/dog.wav")
        pygame.mixer.music.play()

    if event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED:
        text = event.args['text'].lower()

        if text.find('라디오 켜') !=-1:
            print('radio on')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc add http://50.31.180.202:80/",shell=True)
            subprocess.call("mpc play",shell=True)
            subprocess.call("repeat on",shell=True)

        if text.find('라디오 들') !=-1:
            print('radio on')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc add http://50.31.180.202:80/",shell=True)
            subprocess.call("mpc play",shell=True)
            subprocess.call("repeat on",shell=True)          

        if text.find('라디오 듣') !=-1:
            print('radio on')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc add http://50.31.180.202:80/",shell=True)
            subprocess.call("mpc play",shell=True)
            subprocess.call("repeat on",shell=True)              

        if text.find('라디오 키') !=-1:
            print('radio on')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc add http://50.31.180.202:80/",shell=True)
            subprocess.call("mpc play",shell=True)
            subprocess.call("repeat on",shell=True)


        if text.find('라디오 꺼') !=-1:
            print('radio off')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc stop",shell=True)

        if text.find('라디오 끄') !=-1:
            print('radio off')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc stop",shell=True)


        if text.find('재즈 켜') !=-1:
            print('radio on')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc add http://89.16.185.174:8000/stream",shell=True)
            subprocess.call("mpc play",shell=True)
            subprocess.call("repeat on",shell=True)

        if text.find('재즈 들') !=-1:
            print('radio on')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc add http://89.16.185.174:8000/stream",shell=True)
            subprocess.call("mpc play",shell=True)
            subprocess.call("repeat on",shell=True)

        if text.find('재즈 듣') !=-1:
            print('radio on')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc add http://89.16.185.174:8000/stream",shell=True)
            subprocess.call("mpc play",shell=True)
            subprocess.call("repeat on",shell=True)

        if text.find('재즈 키') !=-1:
            print('radio on')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc add http://89.16.185.174:8000/stream",shell=True)
            subprocess.call("mpc play",shell=True)
            subprocess.call("repeat on",shell=True)

        if text.find('재즈 꺼') !=-1:
            print('radio off')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc stop",shell=True)

        if text.find('재즈 끄') !=-1:
            print('radio off')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc stop",shell=True)


        if text.find('클래식 켜') !=-1:
            print('radio on')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc add http://89.16.185.174:8004/stream",shell=True)
            subprocess.call("mpc play",shell=True)
            subprocess.call("repeat on",shell=True)

        if text.find('클래식 들') !=-1:
            print('radio on')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc add http://89.16.185.174:8004/stream",shell=True)
            subprocess.call("mpc play",shell=True)
            subprocess.call("repeat on",shell=True)

        if text.find('클래식 듣') !=-1:
            print('radio on')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc add http://89.16.185.174:8004/stream",shell=True)
            subprocess.call("mpc play",shell=True)
            subprocess.call("repeat on",shell=True)

        if text.find('클래식 키') !=-1:
            print('radio on')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc add http://89.16.185.174:8004/stream",shell=True)
            subprocess.call("mpc play",shell=True)
            subprocess.call("repeat on",shell=True)

        if text.find('클래식 꺼') !=-1:
            print('radio off')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc stop",shell=True)

        if text.find('클래식 끄') !=-1:
            print('radio off')
            assistant.stop_conversation()
            subprocess.call("mpc clear",shell=True)
            subprocess.call("mpc stop",shell=True)

        if text.find('LED on') !=-1:
            print('led on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/ledon.wav")
            pygame.mixer.music.play()
            GPIO.output(21,True)
            GPIO.output(20,True)

        if text.find('light on') !=-1:
            print('led on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/ledon.wav")
            pygame.mixer.music.play()
            GPIO.output(21,True)
            GPIO.output(20,True)

        if text.find('불 키') !=-1:
            print('led on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/ledon.wav")
            pygame.mixer.music.play()
            GPIO.output(21,True)
            GPIO.output(20,True)

        if text.find('불 켜') !=-1:
            print('led on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/ledon.wav")
            pygame.mixer.music.play()
            GPIO.output(21,True)
            GPIO.output(20,True)            

        if text.find('전등 켜') !=-1:
            print('led off')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/ledoff.wav")
            pygame.mixer.music.play()
            GPIO.output(21,False)
            GPIO.output(20,False)

        if text.find('전등 키') !=-1:
            print('led off')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/ledoff.wav")
            pygame.mixer.music.play()
            GPIO.output(21,False)
            GPIO.output(20,False)

        if text.find('LED off') !=-1:
            print('led off')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/ledoff.wav")
            pygame.mixer.music.play()
            GPIO.output(21,False)
            GPIO.output(20,False)

        if text.find('light off') !=-1:
            print('led off')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/ledoff.wav")
            pygame.mixer.music.play()
            GPIO.output(21,False)
            GPIO.output(20,False)

        if text.find('불 꺼') !=-1:
            print('led off')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/ledoff.wav")
            pygame.mixer.music.play()
            GPIO.output(21,False)
            GPIO.output(20,False)

        if text.find('불 끄') !=-1:
            print('led off')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/ledoff.wav")
            pygame.mixer.music.play()
            GPIO.output(21,False)
            GPIO.output(20,False)

        if text.find('전등 꺼') !=-1:
            print('led off')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/ledoff.wav")
            pygame.mixer.music.play()
            GPIO.output(21,False)
            GPIO.output(20,False)

        if text.find('전등 끄') !=-1:
            print('led off')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/ledoff.wav")
            pygame.mixer.music.play()
            GPIO.output(21,False)
            GPIO.output(20,False)

        if text.find('다녀왔어') !=-1:
            print('home in')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/homein.wav")
            pygame.mixer.music.play()
            GPIO.output(21,True)
            GPIO.output(20,True)
            p.start(15)
            try:
              p.ChangeDutyCycle(0.5)
            except:
              p.stop()
              GPIO.cleanup()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
              [1,0,0,0],
              [1,1,0,0],
              [0,1,0,0],
              [0,1,1,0],
              [0,0,1,0],
              [0,0,1,1],
              [0,0,0,1],
              [1,0,0,1]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)


        if text.find('나 왔어') !=-1:
            print('home in')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/homein.wav")
            pygame.mixer.music.play()
            GPIO.output(21,True)
            GPIO.output(20,True)
            p.start(15)
            try:
              p.ChangeDutyCycle(0.5)
            except:
              p.stop()
              GPIO.cleanup()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
              [1,0,0,0],
              [1,1,0,0],
              [0,1,0,0],
              [0,1,1,0],
              [0,0,1,0],
              [0,0,1,1],
              [0,0,0,1],
              [1,0,0,1]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)


        if text.find('다녀왔습니다') !=-1:
            print('home in')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/homein.wav")
            pygame.mixer.music.play()
            GPIO.output(21,True)
            GPIO.output(20,True)
            p.start(15)
            try:
              p.ChangeDutyCycle(0.5)
            except:
              p.stop()
              GPIO.cleanup()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
              [1,0,0,0],
              [1,1,0,0],
              [0,1,0,0],
              [0,1,1,0],
              [0,0,1,0],
              [0,0,1,1],
              [0,0,0,1],
              [1,0,0,1]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)


        if text.find('다녀올게') !=-1:
            print('home out')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/homeout.wav")
            pygame.mixer.music.play()
            GPIO.output(21,False)
            GPIO.output(20,False)
            GPIO.output(26,False)
            p.start(0)
            try:
              p.ChangeDutyCycle(15)
            except:
              p.stop()
              GPIO.cleanup()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
               [1,0,0,1],
               [0,0,0,1],
               [0,0,1,1],
               [0,0,1,0],
               [0,1,1,0],
               [0,1,0,0],
               [1,1,0,0],
               [1,0,0,0]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)

        if text.find('나 갈게') !=-1:
            print('home out')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/homeout.wav")
            pygame.mixer.music.play()
            GPIO.output(21,False)
            GPIO.output(20,False)
            GPIO.output(26,False)
            p.start(0)
            try:
              p.ChangeDutyCycle(15)
            except:
              p.stop()
              GPIO.cleanup()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
               [1,0,0,1],
               [0,0,0,1],
               [0,0,1,1],
               [0,0,1,0],
               [0,1,1,0],
               [0,1,0,0],
               [1,1,0,0],
               [1,0,0,0]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)

        if text.find('다녀오겠습니다') !=-1:
            print('home out')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/homeout.wav")
            pygame.mixer.music.play()
            GPIO.output(21,False)
            GPIO.output(20,False)
            GPIO.output(26,False)
            p.start(0)
            try:
              p.ChangeDutyCycle(15)
            except:
              p.stop()
              GPIO.cleanup()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
               [1,0,0,1],
               [0,0,0,1],
               [0,0,1,1],
               [0,0,1,0],
               [0,1,1,0],
               [0,1,0,0],
               [1,1,0,0],
               [1,0,0,0]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)

        if text.find('get out') !=-1:
            print('home out')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/homeout.wav")
            pygame.mixer.music.play()
            GPIO.output(21,False)
            GPIO.output(20,False)
            GPIO.output(26,False)
            p.start(0)
            try:
              p.ChangeDutyCycle(15)
            except:
              p.stop()
              GPIO.cleanup()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
               [1,0,0,1],
               [0,0,0,1],
               [0,0,1,1],
               [0,0,1,0],
               [0,1,1,0],
               [0,1,0,0],
               [1,1,0,0],
               [1,0,0,0]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)


        if text.find('window open') !=-1:
            print('window open')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/windowopen.wav")
            pygame.mixer.music.play()
            p.start(15)
            try:
              p.ChangeDutyCycle(0.5)
            except:
              p.stop()
              GPIO.cleanup()


        if text.find('창문 열') !=-1:
            print('window open')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/windowopen.wav")
            pygame.mixer.music.play()
            p.start(15)
            try:
              p.ChangeDutyCycle(0.5)
            except:
              p.stop()
              GPIO.cleanup()

        if text.find('창문 올') !=-1:
            print('window open')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/windowopen.wav")
            pygame.mixer.music.play()
            p.start(15)
            try:
              p.ChangeDutyCycle(0.5)
            except:
              p.stop()
              GPIO.cleanup()

        if text.find('window close') !=-1:
            print('window close')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/windowclose.wav")
            pygame.mixer.music.play()
            p.start(0)
            try:
              p.ChangeDutyCycle(15)
            except:
              p.stop()
              GPIO.cleanup()

        if text.find('창문 닫') !=-1:
            print('window close')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/windowclose.wav")
            pygame.mixer.music.play()
            p.start(0)
            try:
              p.ChangeDutyCycle(15)
            except:
              p.stop()
              GPIO.cleanup()

        if text.find('창문 내') !=-1:
            print('window close')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/windowclose.wav")
            pygame.mixer.music.play()
            p.start(0)
            try:
              p.ChangeDutyCycle(15)
            except:
              p.stop()
              GPIO.cleanup()

        if text.find('더워') !=-1:
            print('led on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/windon.wav")
            pygame.mixer.music.play()
            GPIO.output(26,True)

        if text.find('에어컨 켜') !=-1:
            print('led on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/windon.wav")
            pygame.mixer.music.play()
            GPIO.output(26,True)

        if text.find('에어컨 키') !=-1:
            print('led on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/windon.wav")
            pygame.mixer.music.play()
            GPIO.output(26,True)


        if text.find('추워') !=-1:
            print('led off')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/windoff.wav")
            pygame.mixer.music.play()
            GPIO.output(26,False)

        if text.find('에어컨 꺼') !=-1:
            print('led off')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/windoff.wav")
            pygame.mixer.music.play()
            GPIO.output(26,False)

        if text.find('에어컨 끄') !=-1:
            print('led off')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/windoff.wav")
            pygame.mixer.music.play()
            GPIO.output(26,False)


        if text.find('커튼 올') !=-1:
            print('motor on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/curtainopen.wav")
            pygame.mixer.music.play()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
              [1,0,0,0],
              [1,1,0,0],
              [0,1,0,0],
              [0,1,1,0],
              [0,0,1,0],
              [0,0,1,1],
              [0,0,0,1],
              [1,0,0,1]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)

        if text.find('커튼 열') !=-1:
            print('motor on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/curtainopen.wav")
            pygame.mixer.music.play()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
              [1,0,0,0],
              [1,1,0,0],
              [0,1,0,0],
              [0,1,1,0],
              [0,0,1,0],
              [0,0,1,1],
              [0,0,0,1],
              [1,0,0,1]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)


        if text.find('커튼 닫') !=-1:
            print('motor on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/curtainclose.wav")
            pygame.mixer.music.play()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
               [1,0,0,1],
               [0,0,0,1],
               [0,0,1,1],
               [0,0,1,0],
               [0,1,1,0],
               [0,1,0,0],
               [1,1,0,0],
               [1,0,0,0]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)

        if text.find('커튼 치') !=-1:
            print('motor on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/curtainclose.wav")
            pygame.mixer.music.play()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
               [1,0,0,1],
               [0,0,0,1],
               [0,0,1,1],
               [0,0,1,0],
               [0,1,1,0],
               [0,1,0,0],
               [1,1,0,0],
               [1,0,0,0]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)

        if text.find('커튼 내') !=-1:
            print('motor on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/curtainclose.wav")
            pygame.mixer.music.play()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
               [1,0,0,1],
               [0,0,0,1],
               [0,0,1,1],
               [0,0,1,0],
               [0,1,1,0],
               [0,1,0,0],
               [1,1,0,0],
               [1,0,0,0]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)


        if text.find('커튼 쳐') !=-1:
            print('motor on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/curtainclose.wav")
            pygame.mixer.music.play()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
               [1,0,0,1],
               [0,0,0,1],
               [0,0,1,1],
               [0,0,1,0],
               [0,1,1,0],
               [0,1,0,0],
               [1,1,0,0],
               [1,0,0,0]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)



        if text.find('블라인드 올') !=-1:
            print('motor on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/curtainopen.wav")
            pygame.mixer.music.play()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
              [1,0,0,0],
              [1,1,0,0],
              [0,1,0,0],
              [0,1,1,0],
              [0,0,1,0],
              [0,0,1,1],
              [0,0,0,1],
              [1,0,0,1]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)

        if text.find('블라인드 열') !=-1:
            print('motor on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/curtainopen.wav")
            pygame.mixer.music.play()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
              [1,0,0,0],
              [1,1,0,0],
              [0,1,0,0],
              [0,1,1,0],
              [0,0,1,0],
              [0,0,1,1],
              [0,0,0,1],
              [1,0,0,1]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)


        if text.find('블라인드 닫') !=-1:
            print('motor on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/curtainclose.wav")
            pygame.mixer.music.play()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
               [1,0,0,1],
               [0,0,0,1],
               [0,0,1,1],
               [0,0,1,0],
               [0,1,1,0],
               [0,1,0,0],
               [1,1,0,0],
               [1,0,0,0]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)

        if text.find('블라인드 치') !=-1:
            print('motor on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/curtainclose.wav")
            pygame.mixer.music.play()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
               [1,0,0,1],
               [0,0,0,1],
               [0,0,1,1],
               [0,0,1,0],
               [0,1,1,0],
               [0,1,0,0],
               [1,1,0,0],
               [1,0,0,0]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)

        if text.find('블라인드 내') !=-1:
            print('motor on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/curtainclose.wav")
            pygame.mixer.music.play()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
               [1,0,0,1],
               [0,0,0,1],
               [0,0,1,1],
               [0,0,1,0],
               [0,1,1,0],
               [0,1,0,0],
               [1,1,0,0],
               [1,0,0,0]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)


        if text.find('블라인드 쳐') !=-1:
            print('motor on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/curtainclose.wav")
            pygame.mixer.music.play()
            for pin in control_pins:
              GPIO.setup(pin, GPIO.OUT)
              halfstep_seq = [
               [1,0,0,1],
               [0,0,0,1],
               [0,0,1,1],
               [0,0,1,0],
               [0,1,1,0],
               [0,1,0,0],
               [1,1,0,0],
               [1,0,0,0]
            ]
            for i in range(1024):
              for halfstep in range(8):
                for pin in range(4):
                  GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)



        if text.find('물 줘') !=-1:
            print('water on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/water.wav")
            pygame.mixer.music.play()
            GPIO.output(19, GPIO.HIGH)
            time.sleep(10)
            GPIO.output(19, GPIO.LOW)

        if text.find('물 좀 ') !=-1:
            print('water on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/water.wav")
            pygame.mixer.music.play()
            GPIO.output(19, GPIO.HIGH)
            time.sleep(10)
            GPIO.output(19, GPIO.LOW)

        if text.find('물 주') !=-1:
            print('water on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/water.wav")
            pygame.mixer.music.play()
            GPIO.output(19, GPIO.HIGH)
            time.sleep(10)
            GPIO.output(19, GPIO.LOW)

        if text.find('노래 들') !=-1:
            print('sing on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/music.wav")
            pygame.mixer.music.play()

        if text.find('노래 켜') !=-1:
            print('sing on')
            assistant.stop_conversation()
            pygame.init()
            pygame.mixer.music.load("/home/pi/env/lib/python3.5/site-packages/googlesamples/assistant/library/voice/music.wav")
            pygame.mixer.music.play()

        if text.find('노래 꺼') !=-1:
            print('sing off')
            assistant.stop_conversation()
            pygame.quit()


    print(event)

    if (event.type == EventType.ON_CONVERSATION_TURN_FINISHED and
            event.args and not event.args['with_follow_on_turn']):
        print()
        q.start(0)
        try:
          q.ChangeDutyCycle(15)
        except:
          q.stop()
          GPIO.cleanup()
    if event.type == EventType.ON_DEVICE_ACTION:
        for command, params in event.actions:
            print('Do command', command, 'with params', str(params))


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--device-model-id', '--device_model_id', type=str,
                        metavar='DEVICE_MODEL_ID', required=False,
                        help='the device model ID registered with Google')
    parser.add_argument('--project-id', '--project_id', type=str,
                        metavar='PROJECT_ID', required=False,
                        help='the project ID used to register this device')
    parser.add_argument('--nickname', type=str,
                        metavar='NICKNAME', required=False,
                        help='the nickname used to register this device')
    parser.add_argument('--device-config', type=str,
                        metavar='DEVICE_CONFIG_FILE',
                        default=os.path.join(
                            os.path.expanduser('~/.config'),
                            'googlesamples-assistant',
                            'device_config_library.json'
                        ),
                        help='path to store and read device configuration')
    parser.add_argument('--credentials', type=existing_file,
                        metavar='OAUTH2_CREDENTIALS_FILE',
                        default=os.path.join(
                            os.path.expanduser('~/.config'),
                            'google-oauthlib-tool',
                            'credentials.json'
                        ),
                        help='path to store and read OAuth2 credentials')
    parser.add_argument('--query', type=str,
                        metavar='QUERY',
                        help='query to send as soon as the Assistant starts')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ' + Assistant.__version_str__())

    args = parser.parse_args()
    with open(args.credentials, 'r') as f:
        credentials = google.oauth2.credentials.Credentials(token=None,
                                                            **json.load(f))

    device_model_id = None
    last_device_id = None
    try:
        with open(args.device_config) as f:
            device_config = json.load(f)
            device_model_id = device_config['model_id']
            last_device_id = device_config.get('last_device_id', None)
    except FileNotFoundError:
        pass

    if not args.device_model_id and not device_model_id:
        raise Exception('Missing --device-model-id option')

    # Re-register if "device_model_id" is given by the user and it differs
    # from what we previously registered with.
    should_register = (
        args.device_model_id and args.device_model_id != device_model_id)

    device_model_id = args.device_model_id or device_model_id

    with Assistant(credentials, device_model_id) as assistant:
        events = assistant.start()

        device_id = assistant.device_id
        print('device_model_id:', device_model_id)
        print('device_id:', device_id + '\n')

        # Re-register if "device_id" is different from the last "device_id":
        if should_register or (device_id != last_device_id):
            if args.project_id:
                register_device(args.project_id, credentials,
                                device_model_id, device_id, args.nickname)
                pathlib.Path(os.path.dirname(args.device_config)).mkdir(
                    exist_ok=True)
                with open(args.device_config, 'w') as f:
                    json.dump({
                        'last_device_id': device_id,
                        'model_id': device_model_id,
                    }, f)


        for event in events:
            if event.type == EventType.ON_START_FINISHED and args.query:
                assistant.send_text_query(args.query)

            process_event(event, assistant, subprocess)
            
            

if __name__ == '__main__':
    main()
