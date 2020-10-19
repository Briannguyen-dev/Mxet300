#!/usr/bin/python3

# L3_telemetry.py
# This program grabs data from the onboard sensors and log data in files
# for NodeRed access and integrate into a custom "flow".
# Access nodered at 192.168.8.1:1880 (by default, it's running on the Blue)

# Import Internal Programs
import L1_mpu as mpu
import L1_adc as adc
import L2_log as log
import L1_bmp as bmp
# Import External programs
import numpy as np
import time

# Run the main loop
while True:
    # voltage = adc.getDcJack()
    # print(voltage)
    accel = mpu.getAccel()                          # call the function from within L1_mpu.py
    (xAccel) = accel[0]                             # x axis is stored in the first element
    (yAccel) = accel[1]  
    (zAccel) = accel[2]                             #y axis is stored in the second element
    
    #voltage =  adc.getDcJack()
    #log.uniqueFile(voltage,"voltage.txt")
    
    print("x axis:", xAccel, "y axis:", yAccel, "z axis", zAccel)     # print the two values
    axes = np.array([xAccel, yAccel,zAccel])               # store just 2 axes in an array
    log.NodeRed2(axes)                              # send the data to txt files for NodeRed to access.
    # log.uniqueFile(voltage,"voltage.txt")           # another way to log data for NodeRed access
    
    #Temp=bmp.temp()
    #Pressure=bmp.pressure()
    #Alt=bmp.altitude()
    #axes= np.array([Temp,Pressure,Alt])
    #log.NodeRed2(axes)
    
    # log.uniqueFile(yAccel,"yAccel.txt")
    # log.tmpFile(xAccel,"xAccel.txt")              # another way to lof data for NodeRed access
    # log.tmpFile(yAccel,"yAccel.txt")
    time.sleep(0.2)
