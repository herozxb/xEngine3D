#! /usr/bin/env python
import pygame
import numpy as np

screen = pygame.display.set_mode((640, 480),pygame.HWSURFACE|pygame.DOUBLEBUF)
running = 1




matrix4x4Projection = np.array([[1.0, 0.0, 0.0, 0.0],[0.0, 1.0, 0.0, 0.0],[0.0, 0.0, 1.0, 0.0],[0.0, 0.0, 0.0, 1.0]])
matrix_rotateZ = np.array([[1.0, 0.0, 0.0, 0.0],[0.0, 1.0, 0.0, 0.0],[0.0, 0.0, 1.0, 0.0],[0.0, 0.0, 0.0, 1.0]])
matrix_rotateX = np.array([[1.0, 0.0, 0.0, 0.0],[0.0, 1.0, 0.0, 0.0],[0.0, 0.0, 1.0, 0.0],[0.0, 0.0, 0.0, 1.0]])
matrix_camera = np.array([[1.0, 0.0, 0.0, 0.0],[0.0, 1.0, 0.0, 0.0],[0.0, 0.0, 1.0, 0.0],[0.0, 0.0, 0.0, 1.0]])
matrix_view = np.array([[1.0, 0.0, 0.0, 0.0],[0.0, 1.0, 0.0, 0.0],[0.0, 0.0, 1.0, 0.0],[0.0, 0.0, 0.0, 1.0]])
matrix_I = np.array([[1.0, 0.0, 0.0, 0.0],[0.0, 1.0, 0.0, 0.0],[0.0, 0.0, 1.0, 0.0],[0.0, 0.0, 0.0, 1.0]])

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


class triangle(object):
    def __init__(self, lines):
        self.line1 = lines[0]
        self.line2 = lines[1]
        self.line3 = lines[2]

x1 = vector3d(21, 20,19)
x2 = vector3d(21, 20,19)
x3 = vector3d(21, 20,19)
line1 = [x1,x2,x3]

class mesh(list):
    
    def __delitem__(self, key):
        self.__delattr__(key)
    def __getitem__(self, key):
        return self.__getattribute__(key)
    def __setitem__(self, key, value):
        self.__setattr__(key, value)

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

def make_mesh_from_file(strings):
    meshCube = []
    point_list = []
    with open(strings) as f:
    
        for line in f.readlines():
            point = [i.rstrip() for i in line.split(' ')]
  
            if point[0] == 'v':
                x = vector3d(float(point[1]), float(point[2]), float(point[3]))
                point_list.append(x)
        
            if point[0] == 'f':
                oneTriangle = makeTriangle(point_list[int(point[1])-1].x,point_list[int(point[1])-1].y,point_list[int(point[1])-1].z,point_list[int(point[2])-1].x,point_list[int(point[2])-1].y,point_list[int(point[2])-1].z,point_list[int(point[3])-1].x,point_list[int(point[3])-1].y,point_list[int(point[3])-1].z)
                meshCube.append(oneTriangle)
    return meshCube


meshCubetest = make_mesh_from_file("mountain.obj")



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

def matirx_rotate_Y(theta):
    
    matrix_rotateX[0][0] = math.cos( theta * 0.5 )
    matrix_rotateX[1][1] = 1
    matrix_rotateX[2][0] = math.sin( theta * 0.5 )
    matrix_rotateX[0][2] = -1 * math.sin( theta * 0.5 )
    matrix_rotateX[2][2] = math.cos( theta * 0.5 )
    matrix_rotateX[3][3] = 1
    
    return matrix_rotateX

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

def multiply_each_vector_by_number(vector,x,y,z):
    
    vector.x = vector.x * x
    vector.y = vector.y * y
    vector.z = vector.z * z
    
    return vector

def vector_minus_vector(vector1,vector2):

    vector = vector3d(0.1, 0.1,0.1)
    vector.x = vector1.x - vector2.x
    vector.y = vector1.y - vector2.y
    vector.z = vector1.z - vector2.z

    return vector

def vector_add_vector(vector1,vector2):
    
    vector = vector3d(0.1, 0.1,0.1)
    vector.x = vector1.x + vector2.x
    vector.y = vector1.y + vector2.y
    vector.z = vector1.z + vector2.z
    
    return vector

def vector_cross_product(vector_x,vector_y):
    vector_z = vector3d(0.1, 0.1,0.1)
    vector_z.x = vector_x.y * vector_y.z - vector_x.z * vector_y.y
    vector_z.y = vector_x.z * vector_y.x - vector_x.x * vector_y.z
    vector_z.z = vector_x.x * vector_y.y - vector_x.y * vector_y.x

    return vector_z

def vector_normal_make(normal):

    length = math.sqrt( normal.x * normal.x + normal.y * normal.y + normal.z * normal.z )
    if length == 0:
        length = 0.01

    normal.x /= length
    normal.y /= length
    normal.z /= length


    
    return normal

def vector_dotProduct(vector1,vector2):

    dotProduct = vector1.x * vector2.x + vector1.y * vector2.y + vector1.z * vector2.z
    
    return dotProduct

def matrix_point_at(position_vector,target_vector,up_vector):
    forward_vector = vector3d(0.1,0.1,0.1)
    forward_vector = vector_minus_vector(target_vector , position_vector)
    forward_vector = vector_normal_make(forward_vector)

    a = vector3d(0.1,0.1,0.1)
    a.x = forward_vector.x * vector_dotProduct(up_vector,forward_vector)
    a.y = forward_vector.y * vector_dotProduct(up_vector,forward_vector)
    a.z = forward_vector.z * vector_dotProduct(up_vector,forward_vector)
    
    new_up_vector = vector3d(0.1,0.1,0.1)
    new_up_vector = vector_minus_vector(up_vector,a)
    new_up_vector = vector_normal_make(new_up_vector)

    new_right_vector = vector3d(0.1,0.1,0.1)
    new_right_vector = vector_cross_product(new_up_vector,forward_vector)


    matrix4x4 = np.array([[1.0, 0.0, 0.0, 0.0],[0.0, 1.0, 0.0, 0.0],[0.0, 0.0, 1.0, 0.0],[0.0, 0.0, 0.0, 1.0]])


    matrix4x4[0][0] = new_right_vector.x
    matrix4x4[1][0] = new_up_vector.x
    matrix4x4[2][0] = forward_vector.x
    matrix4x4[3][0] = position_vector.x
    matrix4x4[0][1] = new_right_vector.y
    matrix4x4[1][1] = new_up_vector.y
    matrix4x4[2][1] = forward_vector.y
    matrix4x4[3][1] = position_vector.y
    matrix4x4[0][2] = new_right_vector.z
    matrix4x4[1][2] = new_up_vector.z
    matrix4x4[2][2] = forward_vector.z
    matrix4x4[3][2] = position_vector.z
    matrix4x4[0][3] = 0.0
    matrix4x4[1][3] = 0.0
    matrix4x4[2][3] = 0.0
    matrix4x4[3][3] = 1.0

    return matrix4x4

def matrix_quike_inverse(m):
    matrix4x4 = np.array([[0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0]])


    matrix4x4[0][0] = m[0][0]
    matrix4x4[1][0] = m[0][1]
    matrix4x4[2][0] = m[0][2]

    matrix4x4[0][1] = m[1][0]
    matrix4x4[1][1] = m[1][1]
    matrix4x4[2][1] = m[1][2]

    matrix4x4[0][2] = m[2][0]
    matrix4x4[1][2] = m[2][1]
    matrix4x4[2][2] = m[2][2]
    
    matrix4x4[0][3] = 0.0
    matrix4x4[1][3] = 0.0
    matrix4x4[2][3] = 0.0
    
    matrix4x4[3][0] = -1*(m[3][0] * matrix4x4[0][0] + m[3][1] * matrix4x4[1][0] + m[3][2] * matrix4x4[2][0])
    matrix4x4[3][1] = -1*(m[3][0] * matrix4x4[0][1] + m[3][1] * matrix4x4[1][1] + m[3][2] * matrix4x4[2][1])
    matrix4x4[3][2] = -1*(m[3][0] * matrix4x4[0][2] + m[3][1] * matrix4x4[1][2] + m[3][2] * matrix4x4[2][2]);


    matrix4x4[3][3] = 1.0
    
    return matrix4x4

vectorCamera = vector3d(0.0, 0.0,0.0)
vectorLookDirection = vector3d(0.0,0.0,1.0)
fYaw = 0
def Update(elapsedTime):
    
    global vectorLookDirection
    global vectorCamera
    global fYaw
    vForward = multiply_each_vector_by_number(vectorLookDirection, 8.0 * elapsedTime,8.0 * elapsedTime,8.0 * elapsedTime);
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_RIGHT):
                print("---1---")
                vectorCamera.x += 8.0 * elapsedTime
            if(event.key == pygame.K_LEFT):
                print("---2---")
                vectorCamera.x -= 8.0 * elapsedTime

            if(event.key == pygame.K_UP):
                print("---3---")
                vectorCamera.y += 8.0 * elapsedTime
            if(event.key == pygame.K_DOWN):
                print("---4---")
                vectorCamera.y -= 8.0 * elapsedTime
                    
                    
            if(event.key == pygame.K_a):
                print("---5---")
                fYaw -= 2.0 * elapsedTime

            if(event.key == pygame.K_d):
                print("---6---")
                fYaw += 2.0 * elapsedTime

            if(event.key == pygame.K_w):
                print("---7---")
                vectorCamera = vector_add_vector(vectorCamera,vForward)
            if(event.key == pygame.K_s):
                print("---8---")
                vectorCamera = vector_minus_vector(vectorCamera,vForward)
                    
                    
    global theta
    theta += 0.1 * elapsedTime
    theta = 0

    Matirx_Rotate_X = matirx_rotate_X(theta)

    Matirx_Rotate_Z = matirx_rotate_Z(180/180*3.1415926)
    
    for triangles in meshCube:
 
        triProjected  = triangle(line1)
        triTranslated = triangle(line1)
        triRotatedZ  = triangle(line1)
        triRotatedZX = triangle(line1)
        triViewed = triangle(line1)
        
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
        triTranslated = add_each_vector_by_number(triRotatedZX,100,100,100)
        
        normal = vector3d(0.1, 0.1,0.1)
        vectorline1 = vector3d(0.1, 0.1,0.1)
        vectorline2 = vector3d(0.1, 0.1,0.1)

        vectorline1 = vector_minus_vector(triTranslated.line2,triTranslated.line1)
        vectorline2 = vector_minus_vector(triTranslated.line3,triTranslated.line1)

        normal = vector_cross_product(vectorline1,vectorline2)
        normal = vector_normal_make(normal)
        

        
        
        #vectorLookDirection = multiply_each_vector_by_number(vectorLookDirection,-1,-1,-1)
        
        vectorUp = vector3d(0.0,1.0,0.0)
        vectorTarget = vector3d(0.0,0.0,1.0)

        Matirx_Rotate_Y = matirx_rotate_Y(fYaw)
        vectorLookDirection = multiplayMatrixVector(vectorTarget, Matirx_Rotate_Y)

        vectorTarget = vector_add_vector(vectorCamera,vectorLookDirection)
        
        matrix_camera = matrix_point_at(vectorCamera,vectorTarget,vectorUp)
        
        matrix_view = matrix_quike_inverse(matrix_camera)




        dotProductOfVectors = vector_dotProduct(normal,vector_minus_vector(triTranslated.line1,vectorCamera) )

        if dotProductOfVectors < 0 :
		
                lightdirection = vector3d(0.0, 0.0,-1.0)
                
                lightdirection = vector_normal_make(lightdirection)

                dotProductOflight = vector_dotProduct(normal,lightdirection)
		#Project triangles from 3D --> 2D
        
        
                triViewed.line1 = multiplayMatrixVector(triTranslated.line1,matrix_view)
                triViewed.line2 = multiplayMatrixVector(triTranslated.line2,matrix_view)
                triViewed.line3 = multiplayMatrixVector(triTranslated.line3,matrix_view)
        
        
                triProjected.line1 = multiplayMatrixVector(triViewed.line1,matrix4x4Projection)
                triProjected.line2 = multiplayMatrixVector(triViewed.line2,matrix4x4Projection)
                triProjected.line3 = multiplayMatrixVector(triViewed.line3,matrix4x4Projection)

                triProjected.line1.x += 1.0
                triProjected.line1.y += 1.0
                triProjected.line2.x += 1.0
                triProjected.line2.y += 1.0
                triProjected.line3.x += 1.0
                triProjected.line3.y += 1.0
                multiply_each_vector_by_number(triProjected.line1,0.5*640.0,0.5*480.0,1)
                multiply_each_vector_by_number(triProjected.line2,0.5*640.0,0.5*480.0,1)
                multiply_each_vector_by_number(triProjected.line3,0.5*640.0,0.5*480.0,1)

		# Rasterize triangle
                if dotProductOflight<0 :
                    dotProductOflight =0.001
                
                global listTriangleProjected
                listTriangleProjected.append([triProjected,dotProductOflight])
        
    sortedListofTriangleProjected = Sort(listTriangleProjected)

    listTriangleProjected = []
    for trianglesSorted, dotProductOflightSorted in sortedListofTriangleProjected:
        pygame.draw.polygon(screen,(0, 0, 255*dotProductOflightSorted),[(trianglesSorted.line1.x, trianglesSorted.line1.y), (trianglesSorted.line2.x, trianglesSorted.line2.y), (trianglesSorted.line3.x, trianglesSorted.line3.y)],0)

    pygame.display.flip()


import time
while running:
    #event = pygame.event.poll()
    #if event.type == pygame.QUIT:
    #    running = 0
    screen.fill((0, 0, 0))
#time.sleep(0.001)
    Update(0.1)
#pygame.display.flip()
math.cos( theta * 0.5 )
