from pyeit.mesh.shape import circle,ellipse,rectangle0,rectangle,box_circle,thorax,L_shaped

#....#

""" 0. construct mesh structure """
# Mesh shape is specified with fd parameter in the instantiation, Default :fd=circle
mesh_obj, el_pos = mesh.create(16, h0=0.08)

#....#