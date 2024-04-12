import L1_log as log
from time import sleep
import L2_kinematics as kin
import L1_encoder as enc

while True:
    frameSpd = kin.getMotion()
    motSpd = kin.getPdCurrent()
    log.tmpFile(frameSpd[0],"xdot.txt")
    log.tmpFile(frameSpd[1],"thetadot.txt")
    log.tmpFile(motSpd[0],"pdl.txt")
    log.tmpFile(motSpd[1],"pdr.txt")
    print("xdot(m/s): ",frameSpd[0],"\tthetadot (rad/s):",frameSpd[1], "\t","phidotleft: ",motSpd[0],"\t","phidotright: ",motSpd[1])
    sleep(.2)

