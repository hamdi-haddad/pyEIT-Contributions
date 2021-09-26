# coding: utf-8
""" demo code for back-projection based on real lung voltage measurements data """
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
from __future__ import division, absolute_import, print_function

import numpy as np
import matplotlib.pyplot as plt

import pyeit.mesh as mesh
from pyeit.eit.fem import Forward
from pyeit.eit.utils import eit_scan_lines
from pyeit.mesh.shape import circle,ellipse,rectangle0,rectangle,box_circle,thorax,L_shaped
import pyeit.eit.bp as bp

#import lung data ( real voltage measurements )
import lungData as ld


""" 0. build mesh """
# Mesh shape is specified with fd parameter in the instantiation, e.g : fd=thorax , Default :fd=circle
mesh_obj, el_pos = mesh.create(16, h0=0.08,fd=thorax)

# extract node, element, alpha
pts = mesh_obj["node"]
tri = mesh_obj["element"]

""" 1. FEM forward simulations """
# setup EIT scan conditions
# adjacent stimulation (el_dist=1), adjacent measures (step=1)
el_dist, step = 1, 1
ex_mat = eit_scan_lines(16, el_dist)

"""
2. naive inverse solver using back-projection
"""
eit = bp.BP(mesh_obj, el_pos, ex_mat=ex_mat, step=1, parser="std")
eit.setup(weight="none")
#ld.r_v19 are real thorax voltages measured at the middle of breathing cycle ( see lungData.py )
#ld.w_v are real thorax voltages measured at the beginning of breathing cycle ( see lungData.py )
ds = 192.0 * eit.solve(np.array(ld.r_v19), np.array(ld.w_v), normalize=False)

# plot
fig, ax = plt.subplots()

im = ax.tripcolor(pts[:, 0], pts[:, 1], tri, ds, cmap=plt.cm.viridis)
ax.set_title(r"Reconstituted $\Delta$ Conductivities")
ax.axis("equal")
fig.colorbar(im, ax=ax)
""" for production figures, use dpi=300 or render pdf """

fig.savefig('demo_bp.png', dpi=96)
plt.title('Reconstructed Image ( Back-Projection )')
plt.figure(1)
#plt.show()

#------------------- Deep Learning Layer ------------------#

from UNET_Segmentor import UNET_Segmentor

UNET_Segmentor().predict()