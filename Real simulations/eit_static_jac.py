# coding: utf-8
""" Demo on static solving using JAC based on real lung voltage measurements data """
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
from __future__ import division, absolute_import, print_function

import numpy as np
import matplotlib.pyplot as plt

# pyEIT 2D algorithms modules
from pyeit.mesh import create, set_perm
from pyeit.eit.fem import Forward
from pyeit.eit.utils import eit_scan_lines
from pyeit.mesh.shape import circle,ellipse,rectangle0,rectangle,box_circle,thorax,L_shaped
import pyeit.eit.jac as jac
from pyeit.eit.interp2d import sim2pts

#import lung data ( real voltage measurements )
import lungData as ld


""" 1. setup """
n_el = 16
# Mesh shape is specified with fd parameter in the instantiation, e.g : fd=thorax , Default :fd=circle
mesh_obj, el_pos = create(n_el, h0=0.05,fd=thorax) #fd=thorax

# extract node, element, perm
pts = mesh_obj["node"]
tri = mesh_obj["element"]


el_dist, step = 1, 1
ex_mat = eit_scan_lines(n_el, el_dist)


""" 2. solve_eit using gaussian-newton (with regularization) """
# number of stimulation lines/patterns
eit = jac.JAC(mesh_obj, el_pos, ex_mat, step, perm=1.0, parser="std")
eit.setup(p=0.25, lamb=1.0, method="lm")
# lamb = lamb * lamb_decay

#ld.r_v19 are real thorax voltages measured at the middle of breathing cycle ( see lungData.py )
ds = eit.gn(ld.r_v19,p=0.01, lamb=0.001, method='kotre', maxiter=20, verbose=True)

fig,ax = plt.subplots()

# plot
ax = ax
im = ax.tripcolor(
    pts[:, 0],
    pts[:, 1],
    tri,
    np.real(ds),
    shading="flat",
    alpha=1.0,
    cmap=plt.cm.viridis,
)

#Draw electrodes 
ax.plot(pts[:, 0][el_pos], pts[:, 1][el_pos], "ro")
for i, e in enumerate(el_pos):
    ax.text( pts[:, 0][e],  pts[:, 1][e], str(i + 1), size=12)


ax.axis("equal")
ax.set_title("Conductivities Reconstructed")

fig.colorbar(im, ax=ax)
fig.savefig('demo_static.png', dpi=96)
plt.figure(1)
#plt.show()


#------------------- Deep Learning Layer ------------------#

#####################################################################

from UNET_Segmentor import UNET_Segmentor

UNET_Segmentor().predict()
