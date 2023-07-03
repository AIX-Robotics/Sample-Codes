#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B
from time import sleep
from sys import stderr

large_motor = LargeMotor(OUTPUT_B)

print('Starting!')
large_motor.on_for_seconds(speed=20, seconds=5)

print('Ramping up!')
large_motor.on_for_seconds(speed=100, seconds=5)

print('Resting')
sleep(5)

print('Reversing!')
large_motor.on_for_seconds(speed=-100, seconds=5)

print('Ramping down!')
large_motor.on_for_seconds(speed=-20, seconds=5)

print('Done!')
print('I mean I am really done!', file=stderr)
