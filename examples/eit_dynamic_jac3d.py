# import mesh shape from shape.py file 
from pyeit.mesh.shape import ball
#....#
#3D Mesh shape is specified with fd parameter in the instantiation, e.g : fd=ball , Default in 3D :fd=ball
mesh_obj, el_pos = mesh.create(16, h0=0.1,fd=ball)

#....## 