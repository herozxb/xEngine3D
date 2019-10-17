#! /usr/bin/env python
import math
import numpy as np
from objects import vector3d,triangle,mesh
from linearAlgebra import matrix4x4Projection,matrix_rotateZ,matrix_rotateX,matrix_camera,matrix_view,matrix_I,multiplayMatrixVector,makeTriangle,make_mesh_from_file,Sort,matirx_rotate_X,matirx_rotate_Y,matirx_rotate_Z,add_each_vector_by_number,multiply_each_vector_by_number,vector_minus_vector,vector_add_vector,vector_cross_product,vector_normal_make,vector_dotProduct,matrix_point_at,matrix_quike_inverse 

def line_intersect_plane( plane_point, plane_normal, line_start, line_end ):

    plane_normal      = vector_normal_make(plane_normal)
    plane_distance    = -1 *  vector_dotProduct( plane_normal, plane_point )
    a_distance        = vector_dotProduct( line_start, plane_normal )
    b_distance        = vector_dotProduct( line_end, plane_normal )
    t                 = ( -1 * plane_distance - a_distance ) / ( b_distance - a_distance )
    line_start_to_end = vector_minus_vector( line_end, line_start ) 
    line_to_intersect = multiply_each_vector_by_number( line_start_to_end, t, t, t )  

    return vector_add_vector( line_start, line_to_intersect )


def calculate_distance_from_point_to_plane( point, plane_normal, plane_point ):

    plane_normal = vector_normal_make(plane_normal) 
    result = plane_normal.x * point.x + plane_normal.y * point.y + plane_normal.z * point.z - vector_dotProduct( plane_normal, plane_point )
    return result

def triangle_clip_against_plane( plane_point, plane_normal, traingle_put_in ):

    plane_normal      = vector_normal_make(plane_normal)    

    inside_points = []
    counter_of_inside_points = 0
    outside_points = []
    counter_of_outside_points = 0

    traingle_put_out_1 = makeTriangle(0,0,0,0,0,0,0,0,0)
    traingle_put_out_2 = makeTriangle(0,0,0,0,0,0,0,0,0)

    distance_0 = calculate_distance_from_point_to_plane( traingle_put_in.line1, plane_normal ,plane_point )
    distance_1 = calculate_distance_from_point_to_plane( traingle_put_in.line2, plane_normal ,plane_point )
    distance_2 = calculate_distance_from_point_to_plane( traingle_put_in.line3, plane_normal ,plane_point )

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
        return [ 0, None, None] 

    if counter_of_inside_points == 3:

        traingle_put_out_1 = traingle_put_in
        return [ 1, traingle_put_in, None] 

    if counter_of_inside_points == 1 and counter_of_outside_points == 2 :
        traingle_put_out_1.line1 = inside_points[0]
        traingle_put_out_1.line2 = line_intersect_plane( plane_point, plane_normal, inside_points[0], outside_points[0] ) 
        traingle_put_out_1.line3 = line_intersect_plane( plane_point, plane_normal, inside_points[0], outside_points[1] ) 

        return [ 1, traingle_put_out_1, None] 


    if counter_of_inside_points == 2 and counter_of_outside_points == 1 :
        traingle_put_out_1.line1 = inside_points[0]
        traingle_put_out_1.line2 = inside_points[1]
        traingle_put_out_1.line3 = line_intersect_plane( plane_point, plane_normal, inside_points[0], outside_points[0] )
        traingle_put_out_2.line1 = inside_points[1]
        traingle_put_out_2.line2 = traingle_put_out_1.line3
        traingle_put_out_2.line3 = line_intersect_plane( plane_point, plane_normal, inside_points[1], outside_points[0] ) 

        return [ 2, traingle_put_out_1, traingle_put_out_2 ] 


    return False


