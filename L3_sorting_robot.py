##import L2_inverse_kinematics as ik
import L2_speed_control as sc
import numpy as np
##maybe need sleep import 

##Global positions of the inportant loctions
position = [
    [0, 0],                # Starting position
    [60, 0],               # item collecting area
    [-141, 180],           # Area 1
    [-141, 326],           # Area 2
    [100.05, 180],         # Area 3
    [100.05,326],          # Area 4
]


## rotation speed
pi = np.pi                  # utilize the numpy library to define pi
pi/4                        #speed of rotation for the wheels

## angle of SCUTTLE to reach each position
target_angle = 0.0
current_angle = 0.0
turning_angle = 0.0

#turning angle
if (|target_angle - current_angle| > 180)
    -360 + |target_angle - current_angle| = turning_angle
    
else (|target_angle - current_angle| <= 180)
    target_angle - current_angle = turning_angle

#angle of displacment
if (turning_angle > 0)
    #set duration of turn
    #set the wheel speed
    #

else (turning_angle < 0)


np.arctan2(position[1,1], position[1,0]), #item collecting area (check for errors later)  
    ##if 
                                        #angle to position 2 from item collecting area
                                        #angle to position 3 from item collecting area
                                        #angle to position 4 from item collecting area
                                        #angle to position 5 from item collecting area


## error correction code to detect tape on the ground 
