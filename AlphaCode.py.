############################################################
#Collision Avoidance Method Alpha
#Luke Burgess
#Made in June of 2013
#For Blender 2.66a
#------------------------------------------------------------
#Required libraries for proper script execution 
import bpy, math, csv, codecs
from bpy.props import FloatProperty,EnumProperty,BoolProperty
import math
from mathutils import Vector
from functools import reduce
from bpy_extras.object_utils import object_data_add
#End of header - Start Data(CSV) transfer script 
#############################################################
        
#This will be used to scale down any input data.
PlanetRadius=1
PlanetRadius=1/PlanetRadius

#This is the number of identical objects (mini-sats.)
n = 12          #located in different places
s = 1/50        #size of object
GN = ["SatA","SatB","SatC","SatD","SatE","SatF","SatG","SatH","SatI","SatJ","SatK","SatL","SatM","SatN","SatO","SatP","SatQ","SatR","SatS","SatT","SatU","SatV","SatW","SatX","SatY"]

time = 100      #Number of seconds total
nocp = 10       #number of calculated positons
start = 1       #system frame start point
fps=20          #frames per second

R = 3           #Radius of Orbit
Dst=7           #Distance of mother ship

#---prepare a scene-------------------------------------------
end=time*fps         #position of last datapoint
frame_range=range(start,end)      #range of values for frames
bpy.context.scene.frame_start = start
bpy.context.scene.frame_end = end #Total number of frames set
#-------------------------------------------------------------

#---add new Textures------------------------------------------
cTex = bpy.data.textures.new('CloudText', type = 'CLOUDS')
cTex.noise_scale = 1.0
cTex.noise_depth = 5
vTex = bpy.data.textures.new('DestorText', type = 'DISTORTED_NOISE')
vTex.noise_scale = 0.2
#---New materials---------------------------------------------
line = bpy.data.materials.new('Line')
line.type = 'WIRE'
red = bpy.data.materials.new('Red')
red.diffuse_color = (0.2,0,0)
blue = bpy.data.materials.new('Blue')
blue.diffuse_color = (0,0,0.4)
green = bpy.data.materials.new('Green')
green.diffuse_color = (0,.3,0)
grey= bpy.data.materials.new('Grey')
grey.diffuse_color = (0.2,0.2,0.2)
dgrey= bpy.data.materials.new('DGrey')
dgrey.diffuse_color = (0.05,0.05,0.05)
pannel = bpy.data.materials.new('Pannel')
pannel.diffuse_color = (0,0,0.12)
pannel.use_shadeless = True
pTex=pannel.texture_slots.add()
pTex.texture = vTex
pTex.texture_coords = 'UV'
pTex.use_map_color_diffuse = True 
pTex.color = (0,0,0)
laser = bpy.data.materials.new('Laser')
laser.type = 'SURFACE'
laser.use_cast_approximate=False
laser.use_cast_buffer_shadows=False
laser.use_cast_shadows_only=False
laser.use_only_shadow=False
laser.use_ray_shadow_bias=False
laser.type = 'VOLUME'
laser.volume.density = 0.4
laser.volume.density_scale = 4
laser.volume.scattering = 0.3
laser.volume.emission_color = (1,0,0)
laser.volume.emission = 1
laser.ambient = 1
#-------------------------------------------------------------

#---Build a Satellite-----------------------------------------
def new_Sat_add(scale):
    bpy.ops.object.select_all(action='DESELECT')
    group_name = GN.pop()
    group = bpy.data.groups.new(group_name)
    bpy.ops.mesh.primitive_torus_add(
        major_radius=5.3, 
        minor_radius=0.25, 
        major_segments=64, 
        minor_segments=12, 
        use_abso=False, 
        abso_major_rad=1.0, 
        abso_minor_rad=0.5, 
        view_align=False, 
        location=(0.0, 0.0, 1), 
        rotation=(0.0, 0.0, 0.0))
    bpy.context.object.data.materials.append(red)
    bpy.ops.object.group_link(group=group_name)
    for x in range(0, 6):
        y=math.cos(math.pi*x/3)*5
        z=math.sin(math.pi*x/3)*5
        bpy.ops.mesh.primitive_cone_add(
            vertices=64, 
            depth=2.0,
            location=(y,z,.1), 
            rotation=(0.0, 0.0, 0.0))
        bpy.context.object.data.materials.append(dgrey)
        bpy.ops.object.group_link(group=group_name)
        bpy.ops.mesh.primitive_cube_add(
            location=(y,z,1),
            rotation=(0.0, 0.0, 0.0))
        bpy.context.object.data.materials.append(green)
        bpy.ops.object.group_link(group=group_name)
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=64, 
        radius=5,
        depth=0.1, 
        location=(0.0, 0.0, -0.5))
    bpy.context.object.data.materials.append(grey)
    bpy.ops.object.group_link(group=group_name)
    bpy.ops.mesh.primitive_cone_add(
        vertices=64, 
        radius1=5,
        radius2=3, 
        depth=4, 
        location=(0.0, 0.0, 2), 
        rotation=(0.0, 0.0, 0.0))
    bpy.context.object.data.materials.append(blue)
    bpy.ops.object.select_same_group(group=group_name)
    bpy.ops.object.join()
    bpy.context.active_object.scale=(scale,scale,scale)
#-------------------------------------------------------------

#---Initialization of Asteroid/Comet--------------------------
bpy.ops.mesh.primitive_cube_add()
bpy.context.object.data.materials.append(dgrey)
#Changes name of Cube to PolySphere
bpy.context.active_object.name = "PolySphere"
#Positions PolySphere to scene centre
bpy.context.active_object.location = [0, 0, 0]
#Adds Subsurf Modifier
bpy.ops.object.modifier_add(type='SUBSURF')
#Selects Subsurf Modifier for editing
bpy.context.object.modifiers['Subsurf'].levels = 4
#Applys Subsurf Modifier
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf")

#Adds a Displacement Modifier
bpy.ops.object.modifier_add(type='DISPLACE')
bpy.context.object.modifiers['Displace'].name = 'DISPLACEMENT'
bpy.context.object.modifiers['DISPLACEMENT'].texture = bpy.data.textures['CloudText']
bpy.context.object.modifiers['DISPLACEMENT'].strength = 0.9

#Adds smooth shading
bpy.ops.object.shade_smooth()
#Change to Objectmode
#bpy.ops.object.editmode_toggle()

bpy.context.active_object.data.materials.append(
bpy.data.materials[0])
#-------------------------------------------------------------
n=n/3       #Our 3 dimensions result in 3 orbital planes
R=R*PlanetRadius
c=1
ob=1
na=2*math.pi/n
an=(math.pi/(time))
fromTo=range(0,4) #n+1
#---Initialization of Satilites cloned---------------------------
for ob in fromTo:
    new_Sat_add(s)              #make       #size set
    bpy.context.active_object.rotation_euler.x=math.pi*.75
    bpy.context.active_object.rotation_euler.z=0-math.pi*.10
    for c in frame_range: 
        #Set new values for the object every keyframe
        bpy.context.scene.frame_set(frame = c)
        x=0                                     #new X position
        y=R*(math.sin(c*an+na*ob))       #new Y position
        z=R*(math.cos(an*c+na*ob))       #new Z position  
        bpy.context.active_object.location = [x,y,z]
        bpy.context.active_object.keyframe_insert(
        data_path='location',
        group="location")
 
    new_Sat_add(s)            #make       #size set
    bpy.context.active_object.rotation_euler.x=math.pi*.60
    bpy.context.active_object.rotation_euler.z=0-math.pi*.25
    for c in frame_range: 
        #Set new values for the object every keyframe
        bpy.context.scene.frame_set(frame = c)
        x=R*(math.cos(an*c+na*ob+na/3))       #new X position
        y=-R*(math.sin(c*an+na*ob+na/3))      #new Y position
        z=0                                     #new Z position  
        bpy.context.active_object.location = [x,y,z]
        bpy.context.active_object.keyframe_insert(
        data_path='location',
        group="location")
        
    new_Sat_add(s)             #make
    bpy.context.active_object.rotation_euler.x=math.pi*.75
    bpy.context.active_object.rotation_euler.z=0-math.pi*.30
    for c in frame_range: 
        #Set new values for the object every keyframe
        bpy.context.scene.frame_set(frame = c)
        x=R*(math.cos(an*c+na*ob+2*na/3))       #new X position
        y=0                                     #new Y position
        z=R*(math.sin(c*an+na*ob+2*na/3))      #new Z position  
        bpy.context.active_object.location = [x,y,z]
        bpy.context.active_object.keyframe_insert(
        data_path='location',
        group="location")   
            
#----------------------------------------------------------------

bpy.ops.mesh.primitive_circle_add(
    vertices=128, #32
    radius=R,
    location=(0,0,0))
bpy.context.object.data.materials.append(line)

nrot=((math.pi/2, -0.0, 0.0))
bpy.context.scene.objects.active.rotation_euler=nrot

bpy.ops.mesh.primitive_circle_add(
    vertices=128, #32
    radius= R,
    location=(0,0,0))
bpy.context.object.data.materials.append(line)
    
nrot=((0, math.pi/2, 0))
bpy.context.scene.objects.active.rotation_euler=nrot

bpy.ops.mesh.primitive_circle_add(
    vertices=128, #32
    radius= R,
    location=(0,0,0))
bpy.context.object.data.materials.append(line)
    
    
#---Initialization of Mother-Ship--------------------------------

bpy.ops.object.select_all(action='DESELECT')
group_name = GN.pop()
group = bpy.data.groups.new(group_name)

for x in range(0, 5):
    bpy.ops.mesh.primitive_cube_add(
        rotation=(math.pi/10, 0.0, 0.0),
        location=(0,x*4,0))
    bpy.context.active_object.scale=(1,1,.01)
    bpy.context.object.data.materials.append(pannel)
    bpy.ops.object.group_link(group=group_name)
    bpy.ops.mesh.primitive_cube_add(
        rotation=(0-math.pi/10, 0.0, 0.0),
        location=(0,x*4+2,0))
    bpy.context.active_object.scale=(1,1,.01)
    bpy.context.object.data.materials.append(pannel)
    bpy.ops.object.group_link(group=group_name)
    
bpy.ops.mesh.primitive_cube_add(
    rotation=(0, 0.0, 0.0),
    location=(0,9,0))
bpy.context.object.data.materials.append(green)
bpy.context.active_object.scale=(1.1,1,1)
bpy.ops.object.group_link(group=group_name)
    
bpy.ops.mesh.primitive_cylinder_add(
    rotation=(0, 0.0, 0.0),
    location=(0,9,0-0.1))
bpy.context.object.data.materials.append(grey)
bpy.ops.object.group_link(group=group_name)

bpy.ops.object.select_same_group(group=group_name)
bpy.ops.object.join()


bpy.context.active_object.scale=(0.2,0.2,0.2)

nrot=(-(0.239)*math.pi, 0.0, -(0.313)*math.pi)
bpy.context.scene.objects.active.rotation_euler=nrot

bpy.context.active_object.location=[Dst,Dst-R/2.3,Dst+R/2.3] 

#----------------------------------------------------------------


#---Ray creation-------------------------------------------------

Lnth=math.sqrt(Dst*Dst*3)+R
bpy.ops.mesh.primitive_cylinder_add(
    vertices=32, 
    radius=s*2, 
    depth=Lnth)
bpy.context.object.data.materials.append(laser)
nrot=(-(0.239)*math.pi, 0.0, 0-(0.313)*math.pi)
bpy.context.scene.objects.active.rotation_euler=nrot
p=[(Dst-R/2.35)/2,(Dst-R/2.35)/2,(Dst-R/2.35)/2]                   #first position
bpy.context.active_object.location=p    #Start Pos.
ray=bpy.context.active_object


bpy.ops.mesh.primitive_cone_add(
    vertices=32, 
    radius1=s*2, 
    radius2=0, 
    depth=R,
    location=(0-R/5,0-R/12,0-R/2.1))
bpy.context.object.data.materials.append(laser)
nrot=(-(0.20)*math.pi, 0.0, -(.6)*math.pi)
bpy.context.scene.objects.active.rotation_euler=nrot
