#Luke Burgess
#Code for Imaging Laser Powered Satellite Ascent to orbit

import math
from Blender import *
import bpy

##inputs input values for program

Radius_of_Cylinder = 0.02

Radius_of_Satilites = 0.1

Radius_of_Earth = 10.0

Number_of_Satellites = 7.0

Radius_of_Atmosphere = Radius_of_Earth * 1.005

Radius_of_Orbits = Radius_of_Earth * (math.sqrt(4))

Number_of_Visible_Rays = 200

Angular_Velocity_Uper = 20.0

Angular_Velocity_Lower = 4

Angle_relative_to_poles = -0.5

Phase_Angle = (-22.0/50)*(math.pi)

cylCount=0


def Dsphere( acu, R, name, v):
    ENloV = acu[0] #number of longitudenal lines
    ENlaV = acu[1] #number of latidudenal lines
    vert = [[v[0],R+v[1],v[2]]]
    latitude=math.pi/ENlaV
    longitude=2*math.pi/ENloV
    count=0
    face=[[0,ENloV,1]]
    while count<ENlaV:
        count=count+1
        y=float(math.cos(latitude*count)*vert[0][1])
        yx=float(math.sin(latitude*count)*vert[0][1])
        counted=0
        while counted<ENloV:
            counted=counted+1
            x=float(math.sin(longitude*counted)*yx)
            z=float(math.cos(longitude*counted)*yx)
            vert = vert+[[x+v[0],y+v[1],z+v[2]]]
            fac=counted+count*ENloV
            if 2>count:
                Nface = [[0,ENloV-counted,(ENloV-counted+1)]]
                if 1<count:
                    Nface = [[(fac-(ENloV)),(fac-(ENloV+1)),(fac-(2*ENloV+1)),(fac-(2*ENloV))]]
                    if counted == 1:
                        Nface = [[(fac-(ENloV)),(fac-(1)),(fac-(ENloV+1)),(fac-(2*ENloV))]]
                        face = face+Nface
                        makemesh( vert, face, name, 'sphere' ) 

def DCylinder( start, finish, radius ): #this is actualy a rectangular cube
    x=0
    y=1
    #cylCount=cylCount+1
    name='Cylinder'#+cylCount
    R=radius
    L= DL(start, finish) 
    RV=[[ R*(finish[y] - start[y])/(L+0.0000001), R*(start[x] - finish[x])/(L+0.0000001) ]]
    SA=[[(start[x]-RV[0][x]),(start[y]-RV[0][y]),0]]
    SB=[[(start[x]+RV[0][x]),(start[y]+RV[0][y]),0]]
    FA=[[(finish[x]-RV[0][x]),(finish[y]-RV[0][y]),0]]
    FB=[[(finish[x]+RV[0][x]),(finish[y]+RV[0][y]),0]]
    vert= SA +FA+[[start[0],start[1],R]]+[[finish[0],finish[1],R]]+SB+FB+[[start[0],start[1],0-R]]+[[finish[0],finish[1
    face=[[0,1,3,2]]+[[2,3,5,4]]+[[4,5,7,6]]+[[6,7,1,0]]

def makemesh( vert, face, Mes, Obj ):
    editmode = Window.EditMode() # are we in edit mode? If so ...
    if editmode: Window.EditMode(0) # leave edit mode before getting the mesh
# define vertices and faces for rays from a sat
Mesh = bpy.data.meshes.new(Mes) # create a new mesh
Mesh.verts.extend(vert) # add vertices to mesh
Mesh.faces.extend(face) # add faces to the mesh (also adds edges)
Mesh.vertexColors = 1 # enable vertex color
scn = bpy.data.scenes.active # link object to current scene
ob = scn.objects.new(Mesh, Obj) # name Oject
if Mes=='circle':
    ob_mesh= Object.Get(Obj)
    myMeshMod = ob_mesh.modifiers
    mod = myMeshMod.append(Modifier.Types.SUBSURF)
    mod[Modifier.Settings.LEVELS] = 4
    ob_mesh.makeDisplayList() # Needed to apply the modifier 
    Window.RedrawAll() # View the change
    if Mes=='Earth':
        ob_mesh= Object.Get(Obj)
        myMeshMod = ob_mesh.modifiers
        mod = myMeshMod.append(Modifier.Types.SUBSURF)
        mod[Modifier.Settings.LEVELS] = 4
        ob_mesh.makeDisplayList() # Needed to apply the modifier 
        Window.RedrawAll() # View the change
        if editmode: Window.EditMode(1) # optional, just being nice
        def DL( vectA, vectB ):
            DA=math.pow( (vectA[0]) - (vectB[0]), 2)
            DB=math.pow( (vectA[1]) - (vectB[1]), 2)
            L=math.sqrt( DA + DB )
        return L 
    def sphere(vect):
        sp=math.sqrt((vect[0][0])^2 + (vect[0][1])^2 + (vect[0][2])^2)
        so=math.acos( vect[0][2] / sp )
        su=math.atan( vect[0][1] / vect[0][0] )
        svect=[[sp,so,su]]
    return svect

def rect(vect):
    rx=vect[0][0]*math.sin(vect[0][1])*math.cos(vect[0][2])
    ry=vect[0][0]*math.sin(vect[0][1])*math.sin(vect[0][2])
    rz=vect[0][0]*math.cos(vect[0][1])
    rvect=[[rx,ry,rz]]
return rvect

#creating a sphear/earth
Re = Radius_of_Earth #radius of earth
Dsphere( [20, 10], Re, 'Earth', [0,0,0] )

#making a system for the sat transmission volume
#system uses the perpenddicular planes of orbit method
ROC=Radius_of_Cylinder
ROS=Radius_of_Satilites
NOS=Number_of_Satellites #number of sats in one orbital

ROO=Radius_of_Orbits #Radius of Orbit

NVR=Number_of_Visible_Rays #number of rays

ROA=Radius_of_Atmosphere

ARP=Angle_relative_to_poles

PH=Phase_Angle

DeltaAngle = (math.pi*2)/NVR

PowerCraftAngPosition=[0.001+PH]

PowerCraftPositions=rect([[ROO,(math.pi/2),(0.001+PH)]])

AccCraftAngPostion=[0]

FinalAngVel=math.sqrt(ROO/ROA)*DeltaAngle

AngAcc=((FinalAngVel-(RTO)*(math.pi*2)/NVR))/NVR

AccCraftPostion=rect([[ROA,(math.pi/2),0 ]])

t=0

while t<NVR:
    cx=t
    t=t+1
    #first obtian and plot positions for power suplying craft
    PowerCraftAngPosition = PowerCraftAngPosition + [DeltaAngle+PowerCraftAngPosition[cx]]
    PowerCraftPositions=PowerCraftPositions+rect([[ROO,math.pi/2,(PowerCraftAngPosition[t])]])
    DCylinder( rect([[ROO,math.pi/2,DeltaAngle*cx]])[0], rect([[ROO,math.pi/2,DeltaAngle*t]])[0], ROC )
    DCylinder( rect([[ ROA, (math.pi/2), DeltaAngle*cx ]])[0] , rect([[ ROA, (math.pi/2), DeltaAngle*t ]])[0], ROC )
    
    #now put in the craft with an increasing orbital velocity
    AccCraftAngPostion=AccCraftAngPostion+[AccCraftAngPostion[cx]+((RTO)*(math.pi*2)/NVR)/NVR+(AngAcc)*math.pi
    AccCraftPostion=AccCraftPostion+rect([[ ROA, (math.pi/2), AccCraftAngPostion[t] ]])
    
    #now figure out how to draw the lines between them
    #using if statements to control line creation
    if (AccCraftAngPostion[t]<(2*math.pi)):
        if ((PowerCraftAngPosition[t])>(AccCraftAngPostion[t]+math.pi/(NOS))):
            PowerCraftAngPosition[t]=PowerCraftAngPosition[t]-math.pi/(NOS/2)
            rectvalue=rect([[ROO,(math.pi/2),PowerCraftAngPosition[t]]])
            DCylinder( rectvalue[0] , AccCraftPostion[t], ROC )
            if ((PowerCraftAngPosition[t])<(AccCraftAngPostion[t]-math.pi/(NOS))):
                PowerCraftAngPosition[t]=PowerCraftAngPosition[t]+math.pi/(NOS/2)
                rectvalue=rect([[ROO,(math.pi/2),PowerCraftAngPosition[t]]])
                DCylinder( rectvalue[0] , AccCraftPostion[t], ROC )
                if (PowerCraftAngPosition[t])<=(AccCraftAngPostion[cx]+math.pi/NOS):
                    if (PowerCraftAngPosition[t])>=(AccCraftAngPostion[cx]-math.pi/NOS):
                        rectvalue=rect([[ROO,(math.pi/2),PowerCraftAngPosition[t]]])[0]
                        DCylinder( rectvalue , AccCraftPostion[t], ROC )
