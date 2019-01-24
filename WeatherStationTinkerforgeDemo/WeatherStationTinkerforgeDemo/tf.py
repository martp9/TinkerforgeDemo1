#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
# Sensor ID
UIDt = "zFb" # Temperature
UIDb = "Fdy" # Barometer
UIDh = "Di4" # Humidity
UIDa = "yER" # Ambi Light
UIDs = "Fu2" # Sound Pressure Level
UIDm = "DMe" # Motorized Linear Poti

# Import
from time import sleep

# Tinkerforge 
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_temperature import BrickletTemperature
from tinkerforge.bricklet_barometer import BrickletBarometer
from tinkerforge.bricklet_humidity_v2 import BrickletHumidityV2
from tinkerforge.bricklet_ambient_light_v2 import AmbientLightV2
from tinkerforge.bricklet_sound_pressure_level import BrickletSoundPressureLevel
from tinkerforge.bricklet_motorized_linear_poti import BrickletMotorizedLinearPoti

# Sensors
ipcon = IPConnection() # Create IP connection
temp = BrickletTemperature(UIDt, ipcon) # Create device object
baro = BrickletBarometer(UIDb, ipcon) 
humi = BrickletHumidityV2(UIDh, ipcon)
ambi = AmbientLightV2(UIDa, ipcon)
spl  = BrickletSoundPressureLevel(UIDs, ipcon)
mlp = BrickletMotorizedLinearPoti(UIDm, ipcon)

ipcon.connect(HOST, PORT) # Connect to brickd
# Don't use device before ipcon is connected

def getBrickletTemperature():
    return temp.get_temperature()

def getBrickletBarometer():
    return baro.get_air_pressure()

def getBrickletHumidityV2():
    return humi.get_humidity()

def getAmbientLightV2():
    return ambi.get_illuminance()

def getDecibel(db=70):
    # Register decibel callback to function move
    spl.register_callback(spl.CALLBACK_DECIBEL, move)
    # Configure threshold for decibel "greater than 60 dB(A)"
    # with a debounce period of 1s (1000ms)
    print(spl.set_decibel_callback_configuration(1000, False, ">", db*10, 0))

def move(decibel):
    mlp.set_motor_position(100, mlp.DRIVE_MODE_FAST, False)
    sleep(2)
    setMotorZeroPos()

def setMotorZeroPos():
    mlp.set_motor_position(0, mlp.DRIVE_MODE_SMOOTH, False)

def waitForMils(ms=1):
    sleep(ms/1000)

def exit():
    ipcon.disconnect()

