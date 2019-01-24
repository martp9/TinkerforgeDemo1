#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Modules
import terminal
import sys
import tf
import StationGui


while True:
    # Get current temperature
    temperature = tf.getBrickletTemperature()
    pressure = tf.getBrickletBarometer()
    humidity = tf.getBrickletHumidityV2()
    illuminance = tf.getAmbientLightV2()

    print("temperature = "+ str(temperature/100.0)+"Â° C")
    print("pressure    = "+ str(pressure/1000.0)+"mPa")
    print("humidity    = "+ str(humidity/100.0)+"%")
    print("illuminance = "+ str(illuminance/100.0)+" lux")
    tf.getDecibel(80)
    tf.waitForMils(1000)
    terminal.clear()

print("done")
tf.exit()
