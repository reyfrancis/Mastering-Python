''' @TODO: Meriam's Dynamics Book Problem 271 in Chapter 3.
Solve for the correct values. '''


import math
import numpy as np

PI = math.pi

def Compute(mA, mB, vAx, vAy, vBx, vBy, CenterAngle, coeff):
    CenterAngle = InvTrigCorrection(CenterAngle)
    CenterAngle-=PI/2
    CenterAngle*=-1

    # Convert the vector velocity from (x, y) to (x', y') 
    vAx, vAy = RotateAxis(vAx, vAy, CenterAngle)

    vBx, vBy = RotateAxis(vBx, vBy, CenterAngle)
    # print(CenterAngle*(180/PI))

    velocity_update = [0, 0]

    velocity_update[1] = (mA*vAy+mB*vBy+(mA*vAy-mA*vBy)*coeff)/(mA+mB) 
    velocity_update[0] = velocity_update[1] - (vAy - vBy)*coeff

    vAy2 = velocity_update[0]
    vBy2 = velocity_update[1]

    # print(vAx, vAy2, vBx, vBy2)

    # Convert the vector velocity from (x, y) to (x', y') 
    vAx, vAy2 = RotateAxis(vAx, vAy2, -CenterAngle)
    vBx, vBy2 = RotateAxis(vBx, vBy2, -CenterAngle)
    return vAx, vAy2, vBx, vBy2


def InvTrigCorrection(angle):
    if angle < 0:
        angle+=2*PI
    if angle > PI and angle < 2*PI:
        angle-=PI
    return angle

def RotateAxis(x, y, angle):
    A = np.array([[math.cos(angle), -math.sin(angle)],
                  [math.sin(angle),  math.cos(angle)]])
    X = np.array([x, y])

    return np.dot(A, X)