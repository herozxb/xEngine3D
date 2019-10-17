#! /usr/bin/env python
import math
import numpy as np
from objects import vector3d,triangle,mesh

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

def makeTriangle(x0,y0,z0,x1,y1,z1,x2,y2,z2):
    s_0_1 = vector3d(x0, y0, z0)
    s_0_2 = vector3d(x1, y1, z1)
    s_0_3 = vector3d(x2, y2, z2)
    line0 = [s_0_1,s_0_2,s_0_3]
    onetriangle = triangle(line0)
    return onetriangle

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




