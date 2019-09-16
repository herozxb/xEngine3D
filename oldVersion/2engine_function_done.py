#! /usr/bin/env python
import pygame
import numpy as np

screen = pygame.display.set_mode((640, 480))
running = 1

matrix4x4Projection = np.array([[1.0, 0.0, 0.0, 0.0],[0.0, 1.0, 0.0, 0.0],[0.0, 0.0, 1.0, 0.0],[0.0, 0.0, 0.0, 1.0]])
matrix_rotateZ = np.array([[1.0, 0.0, 0.0, 0.0],[0.0, 1.0, 0.0, 0.0],[0.0, 0.0, 1.0, 0.0],[0.0, 0.0, 0.0, 1.0]])
matrix_rotateX = np.array([[1.0, 0.0, 0.0, 0.0],[0.0, 1.0, 0.0, 0.0],[0.0, 0.0, 1.0, 0.0],[0.0, 0.0, 0.0, 1.0]])



def multiplayMatrixVector(inputV,matrix4x4):
    outputV = vector3d(0,0,0)
    outputV.x = inputV.x * matrix4x4[0][0] + inputV.y * matrix4x4[1][0] + inputV.z * matrix4x4[2][0]  + matrix4x4[3][0]
    outputV.y = inputV.x * matrix4x4[0][1] + inputV.y * matrix4x4[1][1] + inputV.z * matrix4x4[2][1]  + matrix4x4[3][1]
    outputV.z = inputV.x * matrix4x4[0][2] + inputV.y * matrix4x4[1][2] + inputV.z * matrix4x4[2][2]  + matrix4x4[3][2]
    w = inputV.x * matrix4x4[0][3] + inputV.y * matrix4x4[1][3] + inputV.z * matrix4x4[2][3]  + matrix4x4[3][3]
    #print("==============3.0========================")
    #print(outputV.x )
    #print(outputV.y )
    #print(outputV.z )
    #print(w )
    
    if w != 0.0:
        outputV.x = outputV.x / w
        outputV.y = outputV.y / w
        outputV.z = outputV.z / w
        #print("==============3.1========================")
        #print(outputV.x )
        #print(outputV.y )
        #print(outputV.z )
        #print(w )
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

t2 = multiplayMatrixVector(t1.line1,matrix4x4Projection)

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

def makeTriangle(x0,y0,z0,x1,y1,z1,x2,y2,z2):
    s_0_1 = vector3d(x0, y0, z0)
    s_0_2 = vector3d(x1, y1, z1)
    s_0_3 = vector3d(x2, y2, z2)
    line0 = [s_0_1,s_0_2,s_0_3]
    onetriangle = triangle(line0)
    return onetriangle





meshCubetest = []

point_list = []
with open("teapot.obj") as f:
    
    for line in f.readlines():
        point = [i.rstrip() for i in line.split(' ')]
        
        #print(point)
        
        if point[0] == 'v':
            #print(point[1])
            #print(point[2])
            #print(point[3])
            x = vector3d(float(point[1]), float(point[2]), float(point[3]))
            point_list.append(x)
        
        if point[0] == 'f':
            #print(point[3])
            print(point_list[int(point[1])-1].x)
            print(point_list[int(point[1])-1].y)
            print(point_list[int(point[1])-1].z)
            print(point_list[int(point[2])-1].x)
            print(point_list[int(point[2])-1].y)
            print(point_list[int(point[2])-1].z)
            print(point_list[int(point[3])-1].x)
            print(point_list[int(point[3])-1].y)
            print(point_list[int(point[3])-1].z)
            oneTriangle = makeTriangle(point_list[int(point[1])-1].x,point_list[int(point[1])-1].y,point_list[int(point[1])-1].z,point_list[int(point[2])-1].x,point_list[int(point[2])-1].y,point_list[int(point[2])-1].z,point_list[int(point[3])-1].x,point_list[int(point[3])-1].y,point_list[int(point[3])-1].z)
            meshCubetest.append(oneTriangle)





pointlist = [ 0.0,0.0,0.0,0.0,1.0,0.0,1.0,1.0,0.0,
              0.0,0.0,0.0,1.0,1.0,0.0,1.0,0.0,0.0,
             
              1.0,0.0,0.0,1.0,1.0,0.0,1.0,1.0,1.0,
              1.0,0.0,0.0,1.0,1.0,1.0,1.0,0.0,1.0,
             
              1.0,0.0,1.0,1.0,1.0,1.0,0.0,1.0,1.0,
              1.0,0.0,1.0,0.0,1.0,1.0,0.0,0.0,1.0,
             
              0.0,0.0,1.0,0.0,1.0,1.0,0.0,1.0,0.0,
              0.0,0.0,1.0,0.0,1.0,0.0,0.0,0.0,0.0,
             
              0.0,1.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,
              0.0,1.0,0.0,1.0,1.0,1.0,1.0,1.0,0.0,
             
              1.0,0.0,1.0,0.0,0.0,1.0,0.0,0.0,0.0,
              1.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0,0.0
             ]

meshCube1 = []
for i in range(12): # 0 ... 11
    tempTriangle = makeTriangle(pointlist[i*9+0]+2,pointlist[i*9+1]+2,pointlist[i*9+2]+2,pointlist[i*9+3]+2,pointlist[i*9+4]+2,pointlist[i*9+5]+2,pointlist[i*9+6]+2,pointlist[i*9+7]+2,pointlist[i*9+8]+2)
    meshCube1.append(tempTriangle)

meshCube3 = []
for i in range(12): # 0 ... 11
    tempTriangle = makeTriangle(pointlist[i*9+0]-2,pointlist[i*9+1]-2,pointlist[i*9+2]-2,pointlist[i*9+3]-2,pointlist[i*9+4]-2,pointlist[i*9+5]-2,pointlist[i*9+6]-2,pointlist[i*9+7]-2,pointlist[i*9+8]-2)
    meshCube3.append(tempTriangle)


meshCube4 = []
for i in range(12): # 0 ... 11
    tempTriangle = makeTriangle(pointlist[i*9+0]-3,pointlist[i*9+1]-3,pointlist[i*9+2]-3,pointlist[i*9+3]-3,pointlist[i*9+4]-3,pointlist[i*9+5]-3,pointlist[i*9+6]-3,pointlist[i*9+7]-3,pointlist[i*9+8]-3)
    meshCube4.append(tempTriangle)

#south
southTriangle1 = makeTriangle(0.0,0.0,0.0,0.0,1.0,0.0,1.0,1.0,0.0)
southTriangle2 = makeTriangle(0.0,0.0,0.0,1.0,1.0,0.0,1.0,0.0,0.0)


#east
eastTriangle1 = makeTriangle(1.0,0.0,0.0,1.0,1.0,0.0,1.0,1.0,1.0)
eastTriangle2 = makeTriangle(1.0,0.0,0.0,1.0,1.0,1.0,1.0,0.0,1.0)

#north
northTriangle1 = makeTriangle(1.0,0.0,1.0,1.0,1.0,1.0,0.0,1.0,1.0)
northTriangle2 = makeTriangle(1.0,0.0,1.0,0.0,1.0,1.0,0.0,0.0,1.0)

#west
westTriangle1 =  makeTriangle(0.0,0.0,1.0,0.0,1.0,1.0,0.0,1.0,0.0)
westTriangle2 = makeTriangle(0.0,0.0,1.0,0.0,1.0,0.0,0.0,0.0,0.0)

#top
topTriangle1 = makeTriangle(0.0,1.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0)
topTriangle2 = makeTriangle(0.0,1.0,0.0,1.0,1.0,1.0,1.0,1.0,0.0)

#bottom
bottomTriangle1 = makeTriangle(1.0,0.0,1.0,0.0,0.0,1.0,0.0,0.0,0.0)
bottomTriangle2 = makeTriangle(1.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0,0.0)


meshCube2 = []
meshCube2.append(southTriangle1)
meshCube2.append(southTriangle2)
meshCube2.append(eastTriangle1)
meshCube2.append(eastTriangle2)
meshCube2.append(northTriangle1)
meshCube2.append(northTriangle2)
meshCube2.append(westTriangle1)
meshCube2.append(westTriangle2)
meshCube2.append(topTriangle1)
meshCube2.append(topTriangle2)
meshCube2.append(bottomTriangle1)
meshCube2.append(bottomTriangle2)

meshCube = meshCube1 + meshCube2 + meshCube3 + meshCube4 + meshCubetest








import math
#project matrix
fNear = 0.1
fFar = 1000.0
fFov = 90.0
fAspectRatio = 480.0 / 640.0
fFovRad = 1.0 / math.tan( fFov * 0.5 / 180.0 * 3.1415926 )

matrix4x4Projection[0][0] = fAspectRatio * fFovRad
matrix4x4Projection[1][1] = fFovRad
matrix4x4Projection[2][2] = fFar / (fFar - fNear)
matrix4x4Projection[3][2] =  (-fFar * fNear) / (fFar - fNear)
matrix4x4Projection[2][3] = 1.0
matrix4x4Projection[3][3] = 0.0


print("----2---")
print(matrix4x4Projection)
print(fAspectRatio)
print(fFovRad)
print(fAspectRatio * fFovRad)


theta = 0
listTriangleProjected = []

def Sort(sub_list):
    sub_list.sort(key = lambda x: x[0].line1.z + x[0].line2.z + x[0].line3.z, reverse = True)
    return sub_list



def matirx_rotate_Z(theta):

    matrix_rotateZ[0][0] = math.cos( theta )
    matrix_rotateZ[0][1] = math.sin( theta )
    matrix_rotateZ[1][0] = -1 * math.sin( theta )
    matrix_rotateZ[1][1] = math.cos( theta )
    matrix_rotateZ[2][2] = 1
    matrix_rotateZ[3][3] = 1

    return matrix_rotateZ

def matirx_rotate_X(theta):
    

    matrix_rotateX[0][0] = 1
    matrix_rotateX[1][1] = math.cos( theta * 0.5 )
    matrix_rotateX[1][2] = math.sin( theta * 0.5 )
    matrix_rotateX[2][1] = -1 * math.sin( theta * 0.5 )
    matrix_rotateX[2][2] = math.cos( theta * 0.5 )
    matrix_rotateX[3][3] = 1
    
    return matrix_rotateX


def add_each_vector_by_number(vector,x,y,z):
    vector.line1.z = vector.line1.z + x
    vector.line2.z = vector.line2.z + y
    vector.line3.z = vector.line3.z + z
    
    return vector

def vector_minus_vector(vector1,vector2):

    vector = vector3d(0.1, 0.1,0.1)
    vector.x = vector1.x - vector2.x
    vector.y = vector1.y - vector2.y
    vector.z = vector1.z - vector2.z

    return vector

def vector_cross_product(vector_x,vector_y):
    vector_z = vector3d(0.1, 0.1,0.1)
    vector_z.x = vector_x.y * vector_y.z - vector_x.z * vector_y.y
    vector_z.y = vector_x.z * vector_y.x - vector_x.x * vector_y.z
    vector_z.z = vector_x.x * vector_y.y - vector_x.y * vector_y.x

    return vector_z

def vector_normal_make(normal):

    length = math.sqrt( normal.x * normal.x + normal.y * normal.y + normal.z * normal.z )
    normal.x /= length
    normal.y /= length
    normal.z /= length

    return normal

def vector_dotProduct(vector1,vector2):

    dotProduct = vector1.x * vector2.x + vector1.y * vector2.y + vector1.z * vector2.z
    
    return dotProduct

def Update(elapsedTime):

    global theta
    theta += 5.0 * elapsedTime

    Matirx_Rotate_X = matirx_rotate_X(theta)
    Matirx_Rotate_Z = matirx_rotate_Z(theta)
    
    for triangles in meshCube:
        #print("---3---")

        #print(triangles.line1.x)
        #print(triangles.line1.y)
        #print(triangles.line1.z)
        #print(triangles.line2.x)
        #print(triangles.line2.y)
        #print(triangles.line2.z)
        #print(triangles.line3.x)
        #print(triangles.line3.y)
        #print(triangles.line3.z)

        #triangle triProjected
        #triangle triTranslated
        #triangle triRotatedZ
        #triangle triRotatedZX
        triProjected  = triangle(line1)
        triTranslated = triangle(line1)
        triRotatedZ  = triangle(line1)
        triRotatedZX = triangle(line1)
        
        
        # Rotate in Z-Axis
        triRotatedZ.line1 = multiplayMatrixVector(triangles.line1,Matirx_Rotate_Z)
        triRotatedZ.line2 = multiplayMatrixVector(triangles.line2,Matirx_Rotate_Z)
        triRotatedZ.line3 = multiplayMatrixVector(triangles.line3,Matirx_Rotate_Z)
        #print(triRotatedZ.line1.x)
        
        
        #// Rotate in X-Axis
        triRotatedZX.line1 = multiplayMatrixVector(triRotatedZ.line1,Matirx_Rotate_X)
        triRotatedZX.line2 = multiplayMatrixVector(triRotatedZ.line2,Matirx_Rotate_X)
        triRotatedZX.line3 = multiplayMatrixVector(triRotatedZ.line3,Matirx_Rotate_X)
        #print(triRotatedZX.line1.x)
        
        # Offset into the screen
        triTranslated = add_each_vector_by_number(triRotatedZX,10,10,10)
        #triTranslated.line1.z = triRotatedZX.line1.z + 10.0
        #triTranslated.line2.z = triRotatedZX.line2.z + 10.0
        #triTranslated.line3.z = triRotatedZX.line3.z + 10.0
        #print(triTranslated.line1.x)

        #print("==============4.0========================")

	    # norm of the surface
        
        normal = vector3d(0.1, 0.1,0.1)
        vectorline1 = vector3d(0.1, 0.1,0.1)
        vectorline2 = vector3d(0.1, 0.1,0.1)

        vectorline1 = vector_minus_vector(triTranslated.line2,triTranslated.line1)
        #vectorline1.x = triTranslated.line2.x - triTranslated.line1.x
        #vectorline1.y = triTranslated.line2.y - triTranslated.line1.y
        #vectorline1.z = triTranslated.line2.z - triTranslated.line1.z

        vectorline2 = vector_minus_vector(triTranslated.line3,triTranslated.line1)
        #vectorline2.x = triTranslated.line3.x - triTranslated.line1.x
        #vectorline2.y = triTranslated.line3.y - triTranslated.line1.y
        #vectorline2.z = triTranslated.line3.z - triTranslated.line1.z

        normal = vector_cross_product(vectorline1,vectorline2)
        #normal.x = vectorline1.y * vectorline2.z - vectorline1.z * vectorline2.y
        #normal.y = vectorline1.z * vectorline2.x - vectorline1.x * vectorline2.z
        #normal.z = vectorline1.x * vectorline2.y - vectorline1.y * vectorline2.x
        
        #length = math.sqrt( normal.x * normal.x + normal.y * normal.y + normal.z * normal.z )
        #normal.x /= length
        #normal.y /= length
        #normal.z /= length

        normal = vector_normal_make(normal)
        
        vectorCamera = vector3d(0.1, 0.1,0.1)
        dotProductOfVectors = vector_dotProduct(normal,vector_minus_vector(triTranslated.line1,vectorCamera) )
        #dotProductOfVectors = normal.x * (triTranslated.line1.x - vectorCamera.x) + normal.y * (triTranslated.line1.y - vectorCamera.y) + normal.z * (triTranslated.line1.z - vectorCamera.z)

        if dotProductOfVectors < 0 :
		
                lightdirection = vector3d(0.0, 0.0,-1.0)
                #length = math.sqrt( lightdirection.x * lightdirection.x + lightdirection.y * lightdirection.y + lightdirection.z * lightdirection.z )
                #lightdirection.x /= length
                #lightdirection.y /= length
                #lightdirection.z /= length
                
                lightdirection = vector_normal_make(lightdirection)

                dotProductOflight = vector_dotProduct(normal,lightdirection)
                #dotProductOflight = normal.x * lightdirection.x + normal.y * lightdirection.y  + normal.z * lightdirection.z

                print("==========8===============")
                print(dotProductOflight)

		#Project triangles from 3D --> 2D
                triProjected.line1 = multiplayMatrixVector(triTranslated.line1,matrix4x4Projection)
                triProjected.line2 = multiplayMatrixVector(triTranslated.line2,matrix4x4Projection)
                triProjected.line3 = multiplayMatrixVector(triTranslated.line3,matrix4x4Projection)
		#print(triProjected.line1.x)
		#print(triProjected.line1.y)
		#print(triProjected.line1.z)
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

		# Rasterize triangle
                #pygame.draw.polygon(screen,(0, 0, 255),[(triProjected.line1.x, triProjected.line1.y), (triProjected.line2.x, triProjected.line2.y), (triProjected.line3.x, triProjected.line3.y)],True)
                
                
                #if dotProductOflight<0 :
                #    dotProductOflight =0.001
                #pygame.draw.polygon(screen,(0, 0, 255*dotProductOflight),[(triProjected.line1.x, triProjected.line1.y), (triProjected.line2.x, triProjected.line2.y), (triProjected.line3.x, triProjected.line3.y)],0)
                if dotProductOflight<0 :
                    dotProductOflight =0.001
                
                global listTriangleProjected
                listTriangleProjected.append([triProjected,dotProductOflight])
        
    sortedListofTriangleProjected = Sort(listTriangleProjected)
#print("===========9============")
    listTriangleProjected = []
    for trianglesSorted, dotProductOflightSorted in sortedListofTriangleProjected:
        #print("============10===========")
        #print(trianglesSorted.line1.x)
#print(trianglesSorted.line1.y)
#print(dotProductOflightSorted)
        pygame.draw.polygon(screen,(0, 0, 255*dotProductOflightSorted),[(trianglesSorted.line1.x, trianglesSorted.line1.y), (trianglesSorted.line2.x, trianglesSorted.line2.y), (trianglesSorted.line3.x, trianglesSorted.line3.y)],0)


		#input("Press Enter to continue...")

import time
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    screen.fill((0, 0, 0))
#pygame.draw.line(screen, (0, 0, 255), (0, 0), (639, 479))
#pygame.draw.line(screen, (0, 0, 255), (639, 0), (0, 479))
#time.sleep(0.01)
    Update(0.1)
    pygame.display.flip()


