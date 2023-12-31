# from spike import PrimeHub, Lightmatrix, Button, statusLight, ForceSensor, notionsensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
# from spike.contral import waith_for_seconds, wait_until, Tier

from hub import light_matrix
from hub import light
import runloop
import time
import motor
import motor_pair
from hub import port
import random
import force_sensor
from hub import sound
import color
import color_sensor
import distance_sensor
from app import music
async def Main():
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)
    # music.play_drum(2)
    # await motor.run_for_degrees(port.C, 150, (540))
    await motor.run_for_degrees(port.D, 150, (580))
    await motor.run_for_degrees(port.E, 100, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (50), 0)
    await motor.run_for_degrees(port.A,-100, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (280), 0)
    await motor.run_for_degrees(port.D, 150, (-220))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-400), 0)
    await motor.run_for_degrees(port.A,-140, (350))
    await motor.run_for_degrees(port.D, 150, (580)) # mission 2
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (510), 0)
    await motor.run_for_degrees(port.E, 90, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (187), 0)
    await motor.run_for_degrees(port.E, 150, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 90, 0)
    await motor.run_for_degrees(port.D, -160, 540)
    await runloop.sleep_ms(1000)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-50), 0)
    await motor.run_for_degrees(port.D, 160, (580))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (50), 0)
    await motor.run_for_degrees(port.D, -160, 540)
    await runloop.sleep_ms(1000)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-50), 0)
    await motor.run_for_degrees(port.D, 160, (580)) # mission 3
    await motor.run_for_degrees(port.E,150, (-150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (250), 0)
    await motor.run_for_degrees(port.E,240, (-150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (460), 0)
    await motor.run_for_degrees(port.A,315, (-300))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-120), 0)
    await motor.run_for_degrees(port.C,170, (-700))
    await motor.run_for_degrees(port.C,-100, (700))
    await motor.run_for_degrees(port.D, 160, (-80))
    await motor.run_for_degrees(port.C,150, (700))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (60), 0)
    await motor.run_for_degrees(port.A,315, (300)) # mission 4
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (280), 0)
    await motor.run_for_degrees(port.E, 105, (304))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (250), 0)
    await motor.run_for_degrees(port.A,-120, (370))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-165), 0)
    await motor.run_for_degrees(port.A,-100, (280)) # Going home
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (800), 0)
    await motor.run_for_degrees(port.A,-100, (280))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (450), 0)
    await motor.run_for_degrees(port.A,-100, (280))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (200), 0)

runloop.run(Main())
