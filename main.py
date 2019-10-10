#! /usr/bin/env python
import math
import pygame
import numpy as np
from math import isnan

screen = pygame.display.set_mode((640, 480),pygame.HWSURFACE|pygame.DOUBLEBUF)
running = 1




matrix4x4Projection = np.array( [ [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0] ] )
matrix_rotateZ      = np.array( [ [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0] ] )
matrix_rotateX      = np.array( [ [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0] ] )
matrix_camera       = np.array( [ [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0] ] )
matrix_view         = np.array( [ [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0] ] )
matrix_I            = np.array( [ [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0] ] )

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


meshCubeinput = make_mesh_from_file("3dObject/mountain.obj")



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

#meshCube = meshCube1 + meshCube2 + meshCube3 + meshCube4 + meshCubetest
#meshCube = meshCubeinput
meshCube = meshCubeinput

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


def matirx_rotate_X(theta):
    
    matrix_rotateX[0][0] = 1
    matrix_rotateX[1][1] = math.cos( theta * 0.5 )
    matrix_rotateX[1][2] = math.sin( theta * 0.5 )
    matrix_rotateX[2][1] = -1 * math.sin( theta * 0.5 )
    matrix_rotateX[2][2] = math.cos( theta * 0.5 )
    matrix_rotateX[3][3] = 1
    
    return matrix_rotateX

def matirx_rotate_Y(theta):
    
    matrix_rotateX[0][0] = math.cos( theta * 0.5 )
    matrix_rotateX[1][1] = 1
    matrix_rotateX[2][0] = math.sin( theta * 0.5 )
    matrix_rotateX[0][2] = -1 * math.sin( theta * 0.5 )
    matrix_rotateX[2][2] = math.cos( theta * 0.5 )
    matrix_rotateX[3][3] = 1
    
    return matrix_rotateX

def matirx_rotate_Z(theta):

    matrix_rotateZ[0][0] = math.cos( theta )
    matrix_rotateZ[0][1] = math.sin( theta )
    matrix_rotateZ[1][0] = -1 * math.sin( theta )
    matrix_rotateZ[1][1] = math.cos( theta )
    matrix_rotateZ[2][2] = 1
    matrix_rotateZ[3][3] = 1

    return matrix_rotateZ



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



def line_intersect_plane( plane_point, plane_normal, line_start, line_end ):

    plane_normal      = vector_normal_make(plane_normal)
    plane_distance    = -1 *  vector_dotProduct( plane_normal, plane_point )
    a_distance        = vector_dotProduct( line_start, plane_normal )
    #print("plane_point",plane_point.x, plane_point.y, plane_point.z)
    #print("line_start",line_start.x, line_start.y, line_start.z)
    #print("a_distance",a_distance)
    b_distance        = vector_dotProduct( line_end, plane_normal )
    #print("line_end",line_end.x, line_end.y, line_end.z)
    #print("b_distance",b_distance)
    t                 = ( -1 * plane_distance - a_distance ) / ( b_distance - a_distance )
    line_start_to_end = vector_minus_vector( line_end, line_start ) 
    line_to_intersect = multiply_each_vector_by_number( line_start_to_end, t, t, t )  

    return vector_add_vector( line_start, line_to_intersect )


def calculate_distance_from_point_to_plane( point, plane_normal, plane_point ):

    plane_normal = vector_normal_make(plane_normal) 

    #print("=========3.1============")
    #print(point.x, point.y, point.z)
    #print(plane_normal.x, plane_normal.y, plane_normal.z)

    result = plane_normal.x * point.x + plane_normal.y * point.y + plane_normal.z * point.z - vector_dotProduct( plane_normal, plane_point )
    #print(result)

    return result

def triangle_clip_against_plane( plane_point, plane_normal, traingle_put_in ):

    plane_normal      = vector_normal_make(plane_normal)    

    inside_points = []
    counter_of_inside_points = 0
    outside_points = []
    counter_of_outside_points = 0

    traingle_put_out_1 = makeTriangle(0,0,0,0,0,0,0,0,0)
    traingle_put_out_2 = makeTriangle(0,0,0,0,0,0,0,0,0)

    #print("=========3.0============")
    #print(plane_point.x, plane_point.y, plane_point.z)
    #print(plane_normal.x, plane_normal.y, plane_normal.z)
    #print(traingle_put_in.line1.x, traingle_put_in.line1.y, traingle_put_in.line1.z)
    #print(traingle_put_in.line2.x, traingle_put_in.line2.y, traingle_put_in.line2.z)
    #print(traingle_put_in.line3.x, traingle_put_in.line3.y, traingle_put_in.line3.z)

    distance_0 = calculate_distance_from_point_to_plane( traingle_put_in.line1, plane_normal ,plane_point )
    distance_1 = calculate_distance_from_point_to_plane( traingle_put_in.line2, plane_normal ,plane_point )
    distance_2 = calculate_distance_from_point_to_plane( traingle_put_in.line3, plane_normal ,plane_point )

    #print("=========2.0 distance is ============")
    #print(distance_0)
    #print(distance_1)
    #print(distance_2)


    if distance_0 >= 0:
        inside_points.append(traingle_put_in.line1)
        counter_of_inside_points = counter_of_inside_points + 1
    else:
        outside_points.append(traingle_put_in.line1)
        counter_of_outside_points = counter_of_outside_points + 1


    if distance_1 >= 0:
        inside_points.append(traingle_put_in.line2)
        counter_of_inside_points = counter_of_inside_points + 1
    else:
        outside_points.append(traingle_put_in.line2)
        counter_of_outside_points = counter_of_outside_points + 1


    if distance_2 >= 0:
        inside_points.append(traingle_put_in.line3)
        counter_of_inside_points = counter_of_inside_points + 1
    else:
        outside_points.append(traingle_put_in.line3)
        counter_of_outside_points = counter_of_outside_points + 1


    if counter_of_inside_points == 0:
        #print("no inside points")
        return [ 0, None, None] 

    if counter_of_inside_points == 3:

        traingle_put_out_1 = traingle_put_in
        #print("all points inside")
        return [ 1, traingle_put_in, None] 

    if counter_of_inside_points == 1 and counter_of_outside_points == 2 :
        #print("1 points inside")
        traingle_put_out_1.line1 = inside_points[0]
        traingle_put_out_1.line2 = line_intersect_plane( plane_point, plane_normal, inside_points[0], outside_points[0] ) 
        traingle_put_out_1.line3 = line_intersect_plane( plane_point, plane_normal, inside_points[0], outside_points[1] ) 

        return [ 1, traingle_put_out_1, None] 


    if counter_of_inside_points == 2 and counter_of_outside_points == 1 :
        #print("2 points inside")
        traingle_put_out_1.line1 = inside_points[0]
        traingle_put_out_1.line2 = inside_points[1]

        #print(inside_points[0].x,inside_points[0].y,inside_points[0].z)
        #print(inside_points[1].x,inside_points[1].y,inside_points[1].z)
        #print("----------------------------------------------------------")
        #print(outside_points[0].x,outside_points[0].y,outside_points[0].z)
        #print(outside_points[1].x,outside_points[1].y,outside_points[1].z)

        traingle_put_out_1.line3 = line_intersect_plane( plane_point, plane_normal, inside_points[0], outside_points[0] )
        #print("in function : ",traingle_put_out_1.line3.x,traingle_put_out_1.line3.y,traingle_put_out_1.line3.z)

        traingle_put_out_2.line1 = inside_points[1]
        traingle_put_out_2.line2 = traingle_put_out_1.line3
        traingle_put_out_2.line3 = line_intersect_plane( plane_point, plane_normal, inside_points[1], outside_points[0] ) 

        return [ 2, traingle_put_out_1, traingle_put_out_2 ] 


    return False




###################################################### Program Start #########################################################################


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
                print("---left---")
                vectorCamera.x += 8.0 * elapsedTime
            if(event.key == pygame.K_LEFT):
                print("---right---")
                vectorCamera.x -= 8.0 * elapsedTime

            if(event.key == pygame.K_UP):
                print("---up---")
                vectorCamera.y -= 8.0 * elapsedTime
            if(event.key == pygame.K_DOWN):
                print("---down---")
                vectorCamera.y += 8.0 * elapsedTime
                    
                    
            if(event.key == pygame.K_a):
                print("---left turn---")
                fYaw -= 2.0 * elapsedTime

            if(event.key == pygame.K_d):
                print("---right turn---")
                fYaw += 2.0 * elapsedTime

            if(event.key == pygame.K_w):
                print("---forward---")
                vectorCamera = vector_add_vector(vectorCamera,vForward)
            if(event.key == pygame.K_s):
                print("---backward---")
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

        # Rotate in X-Axis
        triRotatedZX.line1 = multiplayMatrixVector(triRotatedZ.line1,Matirx_Rotate_X)
        triRotatedZX.line2 = multiplayMatrixVector(triRotatedZ.line2,Matirx_Rotate_X)
        triRotatedZX.line3 = multiplayMatrixVector(triRotatedZ.line3,Matirx_Rotate_X)
        
        # Offset into the screen
        triTranslated = add_each_vector_by_number(triRotatedZX,10,10,10)
        
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

				# Convert World Space      --> View Space
                triViewed.line1 = multiplayMatrixVector(triTranslated.line1,matrix_view)
                triViewed.line2 = multiplayMatrixVector(triTranslated.line2,matrix_view)
                triViewed.line3 = multiplayMatrixVector(triTranslated.line3,matrix_view)

                number_clipped_triangle = 0
                clipped_triangle = []
                clip_result = triangle_clip_against_plane( vector3d( 0.0, 0.0, 0.1 ), vector3d( 0.0, 0.0, 1.0 ), triViewed )

                if clip_result == False:
                    print("wrong!")

                number_clipped_triangle = clip_result[0]

                #print("============1.0============")
                #print(number_clipped_triangle)

                if clip_result[1] is not None:
                    #print("============1.0.1============")
                    clipped_triangle.append(clip_result[1])
                    #print(clipped_triangle[0].line1.x,clipped_triangle[0].line1.y,clipped_triangle[0].line1.z)
                    #print(clipped_triangle[0].line2.x,clipped_triangle[0].line2.y,clipped_triangle[0].line2.z)
                    #print(clipped_triangle[0].line3.x,clipped_triangle[0].line3.y,clipped_triangle[0].line3.z)
                    if clip_result[2] is not None:
                        #print("============1.0.2============")
                        clipped_triangle.append(clip_result[2])
                        #print(clipped_triangle[1].line1.x,clipped_triangle[1].line1.y,clipped_triangle[1].line1.z)
                        #print(clipped_triangle[1].line2.x,clipped_triangle[1].line2.y,clipped_triangle[1].line2.z)
                        #print(clipped_triangle[1].line3.x,clipped_triangle[1].line3.y,clipped_triangle[1].line3.z)





                for i in range(number_clipped_triangle):
                    #print("============1.1============")            
                    #Project triangles from 3D --> 2D  
                    #print(clipped_triangle[i].line1.x,clipped_triangle[i].line1.y,clipped_triangle[i].line1.z)
                    #print(clipped_triangle[i].line2.x,clipped_triangle[i].line2.y,clipped_triangle[i].line2.z)
                    #print(clipped_triangle[i].line3.x,clipped_triangle[i].line3.y,clipped_triangle[i].line3.z)


                    triProjected.line1 = multiplayMatrixVector(clipped_triangle[i].line1,matrix4x4Projection)
                    triProjected.line2 = multiplayMatrixVector(clipped_triangle[i].line2,matrix4x4Projection)
                    triProjected.line3 = multiplayMatrixVector(clipped_triangle[i].line3,matrix4x4Projection)


                    #print("=========1.2.0 triProjected is ============")
                    #print(triProjected.line1.x,triProjected.line1.y,triProjected.line1.z)
                    #print(triProjected.line2.x,triProjected.line2.y,triProjected.line2.z)
                    #print(triProjected.line3.x,triProjected.line3.y,triProjected.line3.z)



                    #print("============1.3============")  
                    triProjected.line1.x += 1.0
                    triProjected.line1.y += 1.0
                    triProjected.line2.x += 1.0
                    triProjected.line2.y += 1.0
                    triProjected.line3.x += 1.0
                    triProjected.line3.y += 1.0
                    multiply_each_vector_by_number(triProjected.line1,0.5*640.0,0.5*480.0,1)
                    multiply_each_vector_by_number(triProjected.line2,0.5*640.0,0.5*480.0,1)
                    multiply_each_vector_by_number(triProjected.line3,0.5*640.0,0.5*480.0,1)
                    #print("============1.4============") 
            # Rasterize triangle
                    if dotProductOflight<0 :
                        dotProductOflight =0.001
                    #print("============1.5============") 

                    #if isnan(triProjected.line2.x):
                        #print("=============Nan number of vector================")
                        #exit(0)
                    global listTriangleProjected
                    listTriangleProjected.append([triProjected,dotProductOflight])
        
    sortedListofTriangleProjected = Sort(listTriangleProjected)

    listTriangleProjected = []
    
    '''
    for trianglesSorted, dotProductOflightSorted in sortedListofTriangleProjected:
        pygame.draw.polygon(screen,(0, 0, 255*dotProductOflightSorted),[(trianglesSorted.line1.x, trianglesSorted.line1.y), (trianglesSorted.line2.x, trianglesSorted.line2.y), (trianglesSorted.line3.x, trianglesSorted.line3.y)],0)
    pygame.display.flip()

    '''
    for trianglesSorted, dotProductOflightSorted in sortedListofTriangleProjected:
        clipped_1 = makeTriangle(0,0,0,0,0,0,0,0,0)
        clipped_2 = makeTriangle(0,0,0,0,0,0,0,0,0)
        
        triangle_to_draw = []
        triangle_to_draw.append( [trianglesSorted,dotProductOflightSorted] )
        #print("[dotProductOflight] = ", dotProductOflightSorted)
        new_triangles = 1
        
        for p in range(4):
            number_triangle_to_add = 0
            
            while new_triangles > 0 :
                test = triangle_to_draw.pop(0)
                test = test[0]
                #print("=========1.2.0 triProjected is popped ============")
                #print(test.line1.x,test.line1.y,test.line1.z)
                #print(test.line2.x,test.line2.y,test.line2.z)
                #print(test.line3.x,test.line3.y,test.line3.z)
                
                if isnan(test.line3.x):
                    print("=============Nan number of vector================")
                    exit(0)
                
                new_triangles = new_triangles - 1
                #print("new_triangles:" + str(new_triangles))
                
                if p == 0:
                    #print("p = " + str(p))
                    clip_result = triangle_clip_against_plane( vector3d( 0.0, 0.0, 0.0 ), vector3d( 0.0, 1.0, 0.0 ), test )
                    number_triangle_to_add = clip_result[0]
                    #print("number_triangle_to_add", number_triangle_to_add)
                    clipped_1              = clip_result[1]
                    #print("clipped_1",clipped_1)
                    #if clipped_1 is not None:
                        #print(clipped_1.line1.x,clipped_1.line1.y,clipped_1.line1.z)
                        #print(clipped_1.line2.x,clipped_1.line2.y,clipped_1.line2.z)
                        #print(clipped_1.line3.x,clipped_1.line3.y,clipped_1.line3.z)
                    clipped_2              = clip_result[2]
                    #print("clipped_2",clipped_2)
                    #if clipped_2 is not None:
                        #print(clipped_2.line1.x,clipped_2.line1.y,clipped_2.line1.z)
                        #print(clipped_2.line2.x,clipped_2.line2.y,clipped_2.line2.z)
                        #print(clipped_2.line3.x,clipped_2.line3.y,clipped_2.line3.z)
                        
                if p == 1:
                    #print("p = " + str(p))
                    clip_result = triangle_clip_against_plane( vector3d( 0.0, 480.0 - 1, 0.0 ), vector3d( 0.0, -1.0, 0.0 ), test )
                    number_triangle_to_add = clip_result[0]
                    #print("number_triangle_to_add", number_triangle_to_add)
                    clipped_1              = clip_result[1]
                    #print("clipped_1",clipped_1)
                    #if clipped_1 is not None:
                        #print(clipped_1.line1.x,clipped_1.line1.y,clipped_1.line1.z)
                        #print(clipped_1.line2.x,clipped_1.line2.y,clipped_1.line2.z)
                        #print(clipped_1.line3.x,clipped_1.line3.y,clipped_1.line3.z)
                    clipped_2              = clip_result[2]
                    #print("clipped_2",clipped_2)
                    #if clipped_2 is not None:
                        #print(clipped_2.line1.x,clipped_2.line1.y,clipped_2.line1.z)
                        #print(clipped_2.line2.x,clipped_2.line2.y,clipped_2.line2.z)
                        #print(clipped_2.line3.x,clipped_2.line3.y,clipped_2.line3.z)

                if p == 2:
                    #print("p = " + str(p))
                    clip_result = triangle_clip_against_plane( vector3d( 0.0, 0.0, 0.0 ), vector3d( 1.0, 0.0, 0.0 ), test )
                    number_triangle_to_add = clip_result[0]
                    #print("number_triangle_to_add", number_triangle_to_add)
                    clipped_1              = clip_result[1]
                    #print("clipped_1",clipped_1)
                    #if clipped_1 is not None:
                        #print(clipped_1.line1.x,clipped_1.line1.y,clipped_1.line1.z)
                        #print(clipped_1.line2.x,clipped_1.line2.y,clipped_1.line2.z)
                        #print(clipped_1.line3.x,clipped_1.line3.y,clipped_1.line3.z)
                    clipped_2              = clip_result[2]
                    #print("clipped_2",clipped_2)
                    #if clipped_2 is not None:
                        #print(clipped_2.line1.x,clipped_2.line1.y,clipped_2.line1.z)
                        #print(clipped_2.line2.x,clipped_2.line2.y,clipped_2.line2.z)
                        #print(clipped_2.line3.x,clipped_2.line3.y,clipped_2.line3.z)

                if p == 3:
                    #print("p = " + str(p))
                    clip_result = triangle_clip_against_plane( vector3d( 640.0 - 1 , 0.0, 0.0 ), vector3d( -1.0, 0.0, 0.0 ), test )
                    number_triangle_to_add = clip_result[0]
                    #print("number_triangle_to_add", number_triangle_to_add)
                    clipped_1              = clip_result[1]
                    #print("clipped_1",clipped_1)
                    #if clipped_1 is not None:
                        #print(clipped_1.line1.x,clipped_1.line1.y,clipped_1.line1.z)
                        #print(clipped_1.line2.x,clipped_1.line2.y,clipped_1.line2.z)
                        #print(clipped_1.line3.x,clipped_1.line3.y,clipped_1.line3.z)
                    clipped_2              = clip_result[2]
                    #print("clipped_2",clipped_2)
                    #if clipped_2 is not None:
                        #print(clipped_2.line1.x,clipped_2.line1.y,clipped_2.line1.z)
                        #print(clipped_2.line2.x,clipped_2.line2.y,clipped_2.line2.z)
                        #print(clipped_2.line3.x,clipped_2.line3.y,clipped_2.line3.z)

                #print("number_triangle_to_add : " + str(number_triangle_to_add))
                #print("dotProductOflight = ", dotProductOflight)
                for w in range(number_triangle_to_add):
                    if w == 0 :
                        triangle_to_draw.append([clipped_1,dotProductOflightSorted])
                    #print( "w1 : " + str(w))
                    if w == 1 :
                        triangle_to_draw.append([clipped_2,dotProductOflightSorted])
        #print( "w2 : " + str(w))
                            
            new_triangles = len(triangle_to_draw)
                #print("new_triangles:" + str(new_triangles))


                #print("length to draw = ", len(triangle_to_draw))
        for triangles_sorted_to_draw, dotProductOflight_to_draw in triangle_to_draw:
            #print("===2===")
            #print("dotProductOflight_to_draw =" ,dotProductOflight_to_draw)
            pygame.draw.polygon(screen,(0, 0, 255*dotProductOflight_to_draw),[(triangles_sorted_to_draw.line1.x, triangles_sorted_to_draw.line1.y), (triangles_sorted_to_draw.line2.x, triangles_sorted_to_draw.line2.y), (triangles_sorted_to_draw.line3.x, triangles_sorted_to_draw.line3.y)],0)

    pygame.display.flip()


import time
clock = pygame.time.Clock()
while running:
    #event = pygame.event.poll()
    #if event.type == pygame.QUIT:
    #    running = 0
    screen.fill((0, 0, 0))
#time.sleep(0.001)
    Update(0.1)
    clock.tick()
    fps = clock.get_fps()
    print("fps = ", fps)
#pygame.display.flip()
math.cos( theta * 0.5 )
