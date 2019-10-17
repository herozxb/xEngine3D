#! /usr/bin/env python
import math
import pygame
import numpy as np
from math import isnan
from objects import vector3d,triangle,mesh
from linearAlgebra import matrix4x4Projection,matrix_rotateZ,matrix_rotateX,matrix_camera,matrix_view,matrix_I,multiplayMatrixVector,makeTriangle,make_mesh_from_file,Sort,matirx_rotate_X,matirx_rotate_Y,matirx_rotate_Z,add_each_vector_by_number,multiply_each_vector_by_number,vector_minus_vector,vector_add_vector,vector_cross_product,vector_normal_make,vector_dotProduct,matrix_point_at,matrix_quike_inverse
from clipFunctions import line_intersect_plane,calculate_distance_from_point_to_plane,triangle_clip_against_plane


screen = pygame.display.set_mode((640, 480),pygame.HWSURFACE|pygame.DOUBLEBUF)
running = 1

x1 = vector3d( 1, 1, 1 )
x2 = vector3d( 1, 1, 1 )
x3 = vector3d( 1, 1, 1 )
line1 = [x1,x2,x3]

meshCube = mesh()
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

#meshCube = meshCube1 + meshCube2 + meshCube3 + meshCube4 + meshCubeinput
#meshCube = meshCubeinput
meshCube = meshCubeinput

theta = 0
listTriangleProjected = []
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
    #print("fps = ", fps)
#pygame.display.flip()
#math.cos( theta * 0.5 )
