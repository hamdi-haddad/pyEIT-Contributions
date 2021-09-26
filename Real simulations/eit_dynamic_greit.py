# coding: utf-8
""" demo using GREIT based on real lung voltage measurements data """
# Copyright (c) Benyuan Liu. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
from __future__ import division, absolute_import, print_function

import numpy as np
import matplotlib.pyplot as plt

import pyeit.mesh as mesh
from pyeit.eit.fem import Forward
from pyeit.eit.utils import eit_scan_lines
from pyeit.mesh.shape import circle,ellipse,rectangle0,rectangle,box_circle,thorax,L_shaped
import pyeit.eit.greit as greit

#import lung data ( real voltage measurements )
import lungData as ld


""" 0. construct mesh """
# Mesh shape is specified with fd parameter in the instantiation, e.g : fd=thorax , Default :fd=circle
mesh_obj, el_pos = mesh.create(16, h0=0.05,fd=thorax)

# extract node, element, alpha
pts = mesh_obj["node"]
tri = mesh_obj["element"]


""" 1. FEM forward simulations """
# setup EIT scan conditions
el_dist, step = 1, 1
ex_mat = eit_scan_lines(16, el_dist)

""" 2. Construct using GREIT """
eit = greit.GREIT(mesh_obj, el_pos, ex_mat=ex_mat, step=step, parser="std")
eit.setup(p=0.50, lamb=0.001)
#ld.r_v19 are real thorax voltages measured at the middle of breathing cycle ( see lungData.py )
#ld.w_v are real thorax voltages measured at the beginning of breathing cycle ( see lungData.py )
ds = eit.solve(np.array(ld.r_v19), np.array(ld.w_v))
x, y, ds = eit.mask_value(ds, mask_value=np.NAN)

# plot
"""
imshow will automatically set NaN (bad values) to 'w',
if you want to manually do so

import matplotlib.cm as cm
cmap = cm.gray
cmap.set_bad('w', 1.)
plt.imshow(np.real(ds), interpolation='nearest', cmap=cmap)
"""
#ax = axes[1]
fig, ax = plt.subplots()
im = ax.imshow(np.real(ds), interpolation="none", cmap=plt.cm.viridis)
ax.axis("equal")
ax.set_title("Reconstructed conductivities")

fig.colorbar(im, ax=ax)
fig.savefig('demo_greit.png', dpi=96)
plt.figure(1)
#plt.show()
#------------------- Deep Learning Layer ------------------#

from UNET_Segmentor import UNET_Segmentor

UNET_Segmentor().predict()