from vex import FORWARD, REVERSE, SECONDS, Motor, Ports, VelocityUnits, wait

motor = Motor(Ports.PORT1)

print("Starting!")
motor.spin(FORWARD, 20, VelocityUnits.PERCENT)
wait(5, SECONDS)

print("Ramping Up!")
motor.spin(FORWARD, 100, VelocityUnits.PERCENT)
wait(5, SECONDS)

print("Resting")
motor.stop()
wait(5, SECONDS)

print("Reversing!")
motor.spin(REVERSE, 100, VelocityUnits.PERCENT)
wait(5, SECONDS)

print("Ramping Down!")
motor.spin(REVERSE, 20, VelocityUnits.PERCENT)
wait(5, SECONDS)

motor.stop()
print("Done!")
