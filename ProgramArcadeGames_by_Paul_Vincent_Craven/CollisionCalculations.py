'''@TODO: Meriam's Dynamics Book Problem 271 in Chapter 3.
Solve for the correct values.'''


import math
import numpy as np

PI = math.pi

def Compute(mA, mB, vAx, vAy, vBx, vBy, CenterAngle, coeff):
    CenterAngle = InvTrigCorrection(CenterAngle)
    CenterAngle-=PI/2

    #Convert the vector velocity from (x, y) to (x', y') 
    vAx, vAy = RotateAxis(vAx, vAy, CenterAngle)
    vBx, vBy = RotateAxis(vBx, vBy, CenterAngle)

    velocity_update = [0, 0]

    velocity_update[1] = (mA*vAy+mB*vBy+(mA*vAy-mA*vBy)*coeff)/(mA+mB) 
    velocity_update[0] = velocity_update[1] - (vAy - vBy)*coeff

    vAy2 = velocity_update[0]
    vBy2 = velocity_update[1]

    print(vAx, vAy2, vBx, vBy2)

    #Convert the vector velocity from (x, y) to (x', y') 
    vAx, vAy2 = RotateAxis(vAx, vAy2, -CenterAngle)
    vBx, vBy2 = RotateAxis(vBx, vBy2, -CenterAngle)

    print(vAx, vAy2, vBx, vBy2)

def InvTrigCorrection(angle):
    if angle < 0:
        angle+=2*PI
    return angle

def RotateAxis(x, y, angle):
    A = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle),  np.cos(angle)]])
    X = np.array([x, y])

    return np.dot(A, X)

Compute(10, 2, -3*math.sin(25*(PI/180)), 3*math.cos(25*(PI/180)), 12*math.cos(50*(PI/180)), -12*math.sin(50*(PI/180)), 20*(PI/180), 0.5)