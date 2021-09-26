#!/usr/bin/env python



# coding: utf-8
""" Demo on dynamic solving using JAC based on real lung voltage measurements data """
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
from __future__ import division, absolute_import, print_function

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import data

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
mesh_obj, el_pos = create(n_el, h0=0.05,fd=thorax) 

'''
# test function for altering the permittivity in mesh
anomaly = [
    {"x": 0.4, "y": 0.4, "d": 0.2, "perm": 10},
    {"x": -0.4, "y": -0.4, "d": 0.2, "perm": 0.1},
]
# background changed to values other than 1.0 requires more iterations
mesh_new = set_perm(mesh_obj, anomaly=anomaly, background=2.0)
'''
# extract node, element, perm
pts = mesh_obj["node"]
tri = mesh_obj["element"]
#perm = mesh_new["perm"]
'''
# show
fig, axes = plt.subplots(1, 2, constrained_layout=True)
fig.set_size_inches(6, 4)

ax = axes[0]
im = ax.tripcolor(
    pts[:, 0], pts[:, 1], tri, np.real(perm), shading="flat", cmap=plt.cm.viridis
)
ax.axis("equal")
ax.set_title(r"$\Delta$ Conductivities")
'''

""" 2. calculate simulated data """
el_dist, step = 1, 1
ex_mat = eit_scan_lines(n_el, el_dist)

fwd = Forward(mesh_obj, el_pos)

""" 3. solve_eit using gaussian-newton (with regularization) """
# number of stimulation lines/patterns
eit = jac.JAC(mesh_obj, el_pos, ex_mat, step, perm=1.0, parser="std")
#p and lamb :regulatization parameters, method : regularization method
eit.setup(p=0.25, lamb=1.0, method="lm")
# lamb = lamb * lamb_decay

#ld.w_v are real thorax voltages measured at the beginning of breathing cycle ( see lungData.py )
ds1 = eit.gn(ld.w_v, p=0.01, lamb=0.001, method='kotre', maxiter=2, verbose=True)
#ld.r_v19 are real thorax voltages measured at the middle of breathing cycle ( see lungData.py )
ds2 = eit.gn(ld.r_v11, p=0.01, lamb=0.001, method='kotre', maxiter=2, verbose=True)
ds3 = ds2-ds1

ds_n = sim2pts(pts, tri, np.real(ds3)) 

max_perm = max(ds_n)
min_perm = min(ds_n)
ds = [(i - min_perm) / (max_perm - min_perm) for i in ds_n]


# plot

fig, ax = plt.subplots()
fig.set_size_inches(6, 4)

#ax = axes[1]

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

#fig.colorbar(im, ax=axes.ravel().tolist())
fig.colorbar(im, ax=ax)

# fig.savefig('../doc/images/demo_static.png', dpi=96)
plt.figure(1)
plt.savefig('demo_jac.png', dpi=96)
plt.title('Reconstructed Image')   # ( Dynamic Jac 2 )
#plt.show()


#------------------- Deep Learning Layer ------------------#

#####################################################################

from UNET_Segmentor import UNET_Segmentor

UNET_Segmentor().predict()


