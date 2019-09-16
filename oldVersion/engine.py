#! /usr/bin/env python
import pygame
import numpy as np

screen = pygame.display.set_mode((640, 480))
running = 1

matrix4x4 = np.array([[1.0, 0.0, 0.0, 0.0],[0.0, 1.0, 0.0, 0.0],[0.0, 0.0, 1.0, 0.0],[0.0, 0.0, 0.0, 1.0]])
matrix_rotateZ = np.array([[1.0, 0.0, 0.0, 0.0],[0.0, 1.0, 0.0, 0.0],[0.0, 0.0, 1.0, 0.0],[0.0, 0.0, 0.0, 1.0]])
matrix_rotateX = np.array([[1.0, 0.0, 0.0, 0.0],[0.0, 1.0, 0.0, 0.0],[0.0, 0.0, 1.0, 0.0],[0.0, 0.0, 0.0, 1.0]])



def multiplayMatrixVector(inputV,matrix4x4):
    outputV = vector3d(0,0,0)
    outputV.x = inputV.x * matrix4x4[0][0] + inputV.y * matrix4x4[1][0] + inputV.z * matrix4x4[2][0]  + matrix4x4[3][0]
    outputV.y = inputV.x * matrix4x4[0][1] + inputV.y * matrix4x4[1][1] + inputV.z * matrix4x4[2][1]  + matrix4x4[3][1]
    outputV.z = inputV.x * matrix4x4[0][2] + inputV.y * matrix4x4[1][2] + inputV.z * matrix4x4[2][2]  + matrix4x4[3][2]
    w = inputV.x * matrix4x4[0][3] + inputV.y * matrix4x4[1][3] + inputV.z * matrix4x4[2][3]  + matrix4x4[3][3]
    
    if w != 0.0:
        outputV.x = outputV.x / w
        outputV.y = outputV.y / w
        outputV.z = outputV.z / w

    
    return outputV

class vector3d(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def return_array(self):
        return [self.x, self.y, self.z]


x = vector3d(21, 20,19)
assert x.x == 21
print(x.x)

class triangle(object):
    def __init__(self, lines):
        self.line1 = lines[0]
        self.line2 = lines[1]
        self.line3 = lines[2]
x1 = vector3d(21, 20,19)
x2 = vector3d(21, 20,19)
x3 = vector3d(21, 20,19)
line1 = [x1,x2,x3]

t1 = triangle(line1)


print("========1============")
print(t1.line1)

t2 = multiplayMatrixVector(t1.line1,matrix4x4)

class mesh(list):
    
    def __delitem__(self, key):
        self.__delattr__(key)
    def __getitem__(self, key):
        return self.__getattribute__(key)
    def __setitem__(self, key, value):
        self.__setattr__(key, value)
    
    
    #    def add_triangle(self, triangle):
    #    self.append(triangle)

    #def count_in_list(n):
#    return mesh[n]

m = mesh()
m["1"] = t1
print("----1---")
print(m["1"].line1.x)

meshCube = mesh()




#inputV = [ 1.0 ,2.0 ,3.0 ,4.0 ]
#print(multiplayMatrixVector(inputV,matrix4x4))



#south
s_0_1 = vector3d(0.0, 0.0, 0.0)
s_0_2 = vector3d(0.0, 1.0, 0.0)
s_0_3 = vector3d(1.0, 1.0, 0.0)
line0 = [s_0_1,s_0_2,s_0_3]
southTriangle1 = triangle(line0)

s_1_1 = vector3d(0.0, 0.0, 0.0)
s_1_2 = vector3d(1.0, 1.0, 0.0)
s_1_3 = vector3d(1.0, 0.0, 0.0)
line1 = [s_1_1,s_1_2,s_1_3]
southTriangle2 = triangle(line1)

#east
s_0_1 = vector3d(1.0, 0.0, 0.0)
s_0_2 = vector3d(1.0, 1.0, 0.0)
s_0_3 = vector3d(1.0, 1.0, 1.0)
line0 = [s_0_1,s_0_2,s_0_3]
eastTriangle1 = triangle(line0)

s_1_1 = vector3d(1.0, 0.0, 0.0)
s_1_2 = vector3d(1.0, 1.0, 1.0)
s_1_3 = vector3d(1.0, 0.0, 1.0)
line1 = [s_1_1,s_1_2,s_1_3]
eastTriangle2 = triangle(line1)

#north
s_0_1 = vector3d(1.0, 0.0, 1.0)
s_0_2 = vector3d(1.0, 1.0, 1.0)
s_0_3 = vector3d(0.0, 1.0, 1.0)
line0 = [s_0_1,s_0_2,s_0_3]
northTriangle1 = triangle(line0)

s_1_1 = vector3d(1.0, 0.0, 1.0)
s_1_2 = vector3d(0.0, 1.0, 1.0)
s_1_3 = vector3d(0.0, 0.0, 1.0)
line1 = [s_1_1,s_1_2,s_1_3]
northTriangle2 = triangle(line1)

#west
s_0_1 = vector3d(0.0, 0.0, 1.0)
s_0_2 = vector3d(0.0, 1.0, 1.0)
s_0_3 = vector3d(0.0, 1.0, 0.0)
line0 = [s_0_1,s_0_2,s_0_3]
westTriangle1 = triangle(line0)

s_1_1 = vector3d(0.0, 0.0, 1.0)
s_1_2 = vector3d(0.0, 1.0, 0.0)
s_1_3 = vector3d(0.0, 0.0, 0.0)
line1 = [s_1_1,s_1_2,s_1_3]
westTriangle2 = triangle(line1)

#top
s_0_1 = vector3d(0.0, 1.0, 0.0)
s_0_2 = vector3d(0.0, 1.0, 1.0)
s_0_3 = vector3d(1.0, 1.0, 1.0)
line0 = [s_0_1,s_0_2,s_0_3]
topTriangle1 = triangle(line0)

s_1_1 = vector3d(0.0, 1.0, 0.0)
s_1_2 = vector3d(1.0, 1.0, 1.0)
s_1_3 = vector3d(1.0, 1.0, 0.0)
line1 = [s_1_1,s_1_2,s_1_3]
topTriangle2 = triangle(line1)

#bottom
s_0_1 = vector3d(1.0, 0.0, 1.0)
s_0_2 = vector3d(0.0, 0.0, 1.0)
s_0_3 = vector3d(0.0, 0.0, 0.0)
line0 = [s_0_1,s_0_2,s_0_3]
bottomTriangle1 = triangle(line0)

s_1_1 = vector3d(1.0, 0.0, 1.0)
s_1_2 = vector3d(0.0, 0.0, 0.0)
s_1_3 = vector3d(1.0, 0.0, 0.0)
line1 = [s_1_1,s_1_2,s_1_3]
bottomTriangle2 = triangle(line1)

'''
meshCube["SOUTH_1"] = southTriangle1
meshCube["SOUTH_2"] = southTriangle2
meshCube["EAST_1"] = eastTriangle1
meshCube["EAST_2"] = eastTriangle2
meshCube["NORTH_1"] = northTriangle1
meshCube["NORTH_2"] = northTriangle2
meshCube["WEST_1"] = westTriangle1
meshCube["WEST_2"] = westTriangle2
meshCube["TOP_1"] = topTriangle1
meshCube["TOP_2"] = topTriangle2
meshCube["BOTTOM_1"] = bottomTriangle1
meshCube["BOTTOM_2"] = bottomTriangle2
'''
meshCube = []
meshCube.append(southTriangle1)
meshCube.append(southTriangle2)
meshCube.append(eastTriangle1)
meshCube.append(eastTriangle2)
meshCube.append(northTriangle1)
meshCube.append(northTriangle2)
meshCube.append(westTriangle1)
meshCube.append(westTriangle2)
meshCube.append(topTriangle1)
meshCube.append(topTriangle2)
meshCube.append(bottomTriangle1)
meshCube.append(bottomTriangle2)
'''
meshCube["EAST_1"] = eastTriangle1
meshCube["EAST_2"] = eastTriangle2
meshCube["NORTH_1"] = northTriangle1
meshCube["NORTH_2"] = northTriangle2
meshCube["WEST_1"] = westTriangle1
meshCube["WEST_2"] = westTriangle2
meshCube["TOP_1"] = topTriangle1
meshCube["TOP_2"] = topTriangle2
meshCube["BOTTOM_1"] = bottomTriangle1
meshCube["BOTTOM_2"] = bottomTriangle2
'''
import math
#project matrix
fNear = 0.1
fFar = 1000.0
fFov = 90.0
fAspectRatio = 480.0 / 640.0
fFovRad = 1.0 / math.tan( fFov * 0.5 / 180.0 * 3.1415926 )

matrix4x4[0][0] = fAspectRatio * fFovRad
matrix4x4[1][1] = fFovRad
matrix4x4[2][2] = fFar / (fFar - fNear)
matrix4x4[3][2] =  (-fFar * fNear) / (fFar - fNear)
matrix4x4[2][3] = 1.0
matrix4x4[3][3] = 0.0


print("----2---")
print(matrix4x4)
print(fAspectRatio)
print(fFovRad)
print(fAspectRatio * fFovRad)


theta = 0

def Update(elapsedTime):

    global theta
    theta += 1.0 * elapsedTime
    #theta = 30.0
    matrix_rotateZ[0][0] = math.cos( theta )
    matrix_rotateZ[0][1] = math.sin( theta )
    matrix_rotateZ[1][0] = -1 * math.sin( theta )
    matrix_rotateZ[1][1] = math.cos( theta )
    matrix_rotateZ[2][2] = 1
    matrix_rotateZ[3][3] = 1
    
    print("-------7------")
    print(matrix_rotateZ)

    matrix_rotateX[0][0] = 1
    matrix_rotateX[1][1] = math.cos( theta * 0.5 )
    matrix_rotateX[1][2] = math.sin( theta * 0.5 )
    matrix_rotateX[2][1] = -1 * math.sin( theta * 0.5 )
    matrix_rotateX[2][2] = math.cos( theta * 0.5 )
    matrix_rotateX[3][3] = 1


    for triangles in meshCube:
        #print("---3---")
        #print(triangles)
        #triangle triProjected
        #triangle triTranslated
        #triangle triRotatedZ
        #triangle triRotatedZX
        triProjected  = triangle(line1)
        triTranslated = triangle(line1)
        triRotatedZ  = triangle(line1)
        triRotatedZX = triangle(line1)
        # Rotate in Z-Axis
        triRotatedZ.line1 = multiplayMatrixVector(triangles.line1,matrix_rotateZ)
        triRotatedZ.line2 = multiplayMatrixVector(triangles.line2,matrix_rotateZ)
        triRotatedZ.line3 = multiplayMatrixVector(triangles.line3,matrix_rotateZ)
        #print(triRotatedZ.line1.x)
        #// Rotate in X-Axis
        triRotatedZX.line1 = multiplayMatrixVector(triRotatedZ.line1,matrix_rotateX)
        triRotatedZX.line2 = multiplayMatrixVector(triRotatedZ.line2,matrix_rotateX)
        triRotatedZX.line3 = multiplayMatrixVector(triRotatedZ.line3,matrix_rotateX)
        #print(triRotatedZX.line1.x)
        # Offset into the screen
        triTranslated = triRotatedZX
        triTranslated.line1.z = triRotatedZX.line1.z + 3.0
        triTranslated.line2.z = triRotatedZX.line2.z + 3.0
        triTranslated.line3.z = triRotatedZX.line3.z + 3.0
        #print(triTranslated.line1.x)

        #Project triangles from 3D --> 2D
        triProjected.line1 = multiplayMatrixVector(triTranslated.line1,matrix4x4)
        triProjected.line2 = multiplayMatrixVector(triTranslated.line2,matrix4x4)
        triProjected.line3 = multiplayMatrixVector(triTranslated.line3,matrix4x4)
        #print(triProjected.line1.x)
        #Scale into view
        triProjected.line1.x += 1.0
        triProjected.line1.y += 1.0
        triProjected.line2.x += 1.0
        triProjected.line2.y += 1.0
        triProjected.line3.x += 1.0
        triProjected.line3.y += 1.0
            
        triProjected.line1.x *= 0.5 * 640.0
        triProjected.line1.y *= 0.5 * 480.0
        triProjected.line2.x *= 0.5 * 640.0
        triProjected.line2.y *= 0.5 * 480.0
        triProjected.line3.x *= 0.5 * 640.0
        triProjected.line3.y *= 0.5 * 480.0


        print("==============5.0========================")
        print(triProjected.line1.x)
        print(triProjected.line1.y)
        # Rasterize triangle
        pygame.draw.polygon(screen,(0, 255, 0),[(triProjected.line1.x, triProjected.line1.y), (triProjected.line2.x, triProjected.line2.y), (triProjected.line3.x, triProjected.line3.y)],True)

import time
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    screen.fill((0, 0, 0))
#pygame.draw.line(screen, (0, 0, 255), (0, 0), (639, 479))
#pygame.draw.line(screen, (0, 0, 255), (639, 0), (0, 479))
    time.sleep(0.01)
    Update(0.01)
    pygame.display.flip()

