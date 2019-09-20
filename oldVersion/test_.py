import pygame
import numpy as np


inputV = [1,2,3]
matrix = [[1.0, 0.0, 0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]


def Update(elapsedTime):

    global theta
    theta += 1.0 * elapsedTime
    #theta = 30.0
    matrix_rotateZ[0][0] = math.cos( theta )
    matrix_rotateZ[1][1] = math.sin( theta )
    matrix_rotateZ[2][2] = -1 * math.sin( theta )
    matrix_rotateZ[2][3] = math.cos( theta )
    matrix_rotateZ[3][2] = 1
    matrix_rotateZ[3][3] = 1
    




outputV = np.matmul(inputV,matrix)
print(outputV)
