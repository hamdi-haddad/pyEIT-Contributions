
from pyeit.mesh.shape import circle,ellipse,rectangle0,rectangle,box_circle,thorax,L_shaped

#....#

# Mesh shape is specified with fd parameter in the instantiation, e.g : fd=thorax , Default :fd=circle
mesh_obj, el_pos = wrapper.create(16, h0=0.1,fd=thorax)

#....#