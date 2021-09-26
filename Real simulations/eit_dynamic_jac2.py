# coding: utf-8
""" demo on dynamic eit using JAC method based on real lung voltage measurements data"""
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
from __future__ import division, absolute_import, print_function

import numpy as np
import matplotlib.pyplot as plt

import pyeit.mesh as mesh
from pyeit.eit.fem import Forward
from pyeit.eit.utils import eit_scan_lines

from pyeit.mesh.shape import circle,ellipse,rectangle0,rectangle,box_circle,thorax,L_shaped
import pyeit.eit.jac as jac
from pyeit.eit.interp2d import sim2pts

#import lung data ( real voltage measurements )
import lungData as ld

""" 0. construct mesh """
# Mesh shape is specified with fd parameter in the instantiation, e.g : fd=thorax , Default :fd=circle
mesh_obj, el_pos = mesh.create(16, h0=0.05,fd=thorax)
# mesh_obj, el_pos = mesh.layer_circle()

# extract node, element, alpha
pts = mesh_obj["node"]
tri = mesh_obj["element"]
x, y = pts[:, 0], pts[:, 1]

""" 1. FEM simulation """
el_dist, step = 1, 1
ex_mat = eit_scan_lines(16, el_dist)

""" 3. JAC solver """
# Note: if the jac and the real-problem are generated using the same mesh,
# then, data normalization in solve are not needed.
# However, when you generate jac from a known mesh, but in real-problem
# (mostly) the shape and the electrode positions are not exactly the same
# as in mesh generating the jac, then data must be normalized.
eit = jac.JAC(
    mesh_obj,
    el_pos,
    ex_mat=ex_mat,
    step=step,
    perm=1.0,
    parser="std",
)
eit.setup(p=0.5, lamb=0.01, method="kotre")

#ld.r_v19 are real thorax voltages measured at the middle of breathing cycle ( see lungData.py )
#ld.w_v are real thorax voltages measured at the beginning of breathing cycle ( see lungData.py )

#ld.r_v11,ld.r_v12,ld.r_v13,ld.r_v14,ld.r_v15,ld.r_v16,ld,ld.r_v17,ld.r_v18,
#l = [ld.r_v19,ld.r_v20,ld.r_v21,ld.r_v22,ld.r_v23,ld.r_v24,ld.r_v25,
#ld.r_v26,ld.r_v27,ld.r_v28,ld.r_v29,ld.r_v30,ld.r_v31,ld.r_v32,ld.r_v33,ld.r_v34]


ds = eit.solve(np.array(ld.r_v19), np.array(ld.w_v), normalize=False)
ds_n = sim2pts(pts, tri, np.real(ds))

# plot ground truth

fig, ax = plt.subplots()
fig.set_size_inches(6, 4)


# plot EIT reconstruction


im = ax.tripcolor(x, y, tri, ds_n, shading="flat")

ax.set_aspect("equal")


#Draw electrodes 
ax.plot(pts[:, 0][el_pos], pts[:, 1][el_pos], "ro")
for i, e in enumerate(el_pos):
    ax.text( pts[:, 0][e],  pts[:, 1][e], str(i + 1), size=12)


fig.colorbar(im, ax=ax)
plt.savefig('demo_jac.png', dpi=96)
plt.title('Reconstructed Image')   # ( Dynamic Jac 2 )
plt.figure(1)
#plt.show()



#------------------- Deep Learning Layer ------------------#

#####################################################################

from UNET_Segmentor import UNET_Segmentor

UNET_Segmentor().predict()