#!/usr/bin/env python3
from ev3dev2.display import Display
from time import sleep

lcd = Display()
lcd.rectangle(clear_screen=False, x1=0, y1=0, x2=177, y2=80, fill_color='black')
lcd.text_pixels('Hello, there!', clear_screen=False, x=10, y=10, text_color='white')
lcd.text_pixels('Welcome!', clear_screen=False, x=10, y=20, text_color='white')
lcd.text_pixels('Enjoy robotics!', clear_screen=False, x=10, y=30, text_color='white')
lcd.update()
sleep(6)
lcd.text_pixels('Hello again!', clear_screen=True, x=10, y=10, text_color='white')
lcd.update()
sleep(6)
