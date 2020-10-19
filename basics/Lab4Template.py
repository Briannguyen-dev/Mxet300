# Team Number: 4
# TM 1: Brian Nguyen 
# TM 2: Even Mariest 
# Date: 10/6/2020
# Code purpose: Get True orientation from SCUTTLE robot, as well as current speed and change in angle.
#NodeRed Code: https://gist.github.com/Briannguyen-dev/bc138b16c2c1f19936d4983a5291ce8c

# Import Internal Programs
import L2_kinematics as kin
import L2_log as log
import L2_heading as heading

# Import External programs
import numpy as np
import time

# DEFINE THE FUNCTIONS FOR THE PROGRAM
def Lab4task2():
  #do some items here
  pdees = kin.getPdCurrent()
  pdl = pdees[0] #gets pdl
  pdr = pdees[1] #gets pdr
  
  move = kin.getMotion()
  xdot = move[0] #gets xdot
  thetadot = move[1] #gets thetadot
  
  log.tmpFile(pdl, "pdl.txt")
  log.tmpFile(pdr, "pdr.txt")
  log.tmpFile(xdot, "xdot.txt")
  log.tmpFile(thetadot, "thetadot.txt")
  
def Lab5task2():
  axes = heading.getXY()
  axesScaled = heading.scale(axes)
  h = heading.getHeading(axesScaled)
  headingDegrees = round(h*180/np.pi, 2)
  log.tmpFile(headingDegrees, "headingDegrees.txt")

 
# UNCOMMENT THE LOOP BELOW TO RUN THE PROGRAM CONTINUOUSLY
while 1:
    Lab4task2()
    Lab5task2()
    time.sleep(0.2) # delay a short period