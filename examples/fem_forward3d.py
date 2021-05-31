
from pyeit.mesh.shape import ball

#....#

# 3D Mesh shape is specified with fd parameter in the instantiation, e.g : fd=ball , Default in 3D :fd=ball
mesh_obj, el_pos = mesh.create(h0=0.15, bbox=bbox,fd=ball)

#....#