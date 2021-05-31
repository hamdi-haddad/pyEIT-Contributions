from pyeit.mesh.shape import ball
#....#

# tetrahedron meshing in a 3D bbox
bbox = [[-1.2, -1.2, -1.2], [1.2, 1.2, 1.2]]
# 3D Mesh shape is specified with fd parameter in the instantiation, e.g : fd=ball , Default in 3D :fd=ball
ms, el_pos = mesh.create(h0=0.15, bbox=bbox,fd=ball)

#....#