class vector3d(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def return_array(self):
        return [self.x, self.y, self.z]


x = vector3d(21, 20,19)

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

def makeTriangle(x0,y0,z0,x1,y1,z1,x2,y2,z2):
    s_0_1 = vector3d(x0, y0, z0)
    s_0_2 = vector3d(x1, y1, z1)
    s_0_3 = vector3d(x2, y2, z2)
    line0 = [s_0_1,s_0_2,s_0_3]
    onetriangle = triangle(line0)
    return onetriangle


meshCubetest = []

point_list = []
with open("girl.obj") as f:
    
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
            print(point_list[int(point[1][0])-1].x)
            print(point_list[int(point[1][0])-1].y)
            print(point_list[int(point[1][0])-1].z)
            print(point_list[int(point[2][0])-1].x)
            print(point_list[int(point[2][0])-1].y)
            print(point_list[int(point[2][0])-1].z)
            print(point_list[int(point[3][0])-1].x)
            print(point_list[int(point[3][0])-1].y)
            print(point_list[int(point[3][0])-1].z)
            #oneTriangle = makeTriangle(point_list[int(point[1])-1].x,point_list[int(point[1])-1].y,point_list[int(point[1])-1].z,point_list[int(point[2])-1].x,point_list[int(point[2])-1].y,point_list[int(point[2])-1].z,point_list[int(point[3])-1].x,point_list[int(point[3])-1].y,point_list[int(point[3])-1].z)
#meshCubetest.append(oneTriangle)
