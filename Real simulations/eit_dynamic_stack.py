# coding: utf-8
""" demo using stacked ex_mat based on real lung voltage measurements data """
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
from __future__ import division, absolute_import, print_function

import numpy as np
import matplotlib.pyplot as plt

# pyEIT 2D algorithm modules
import pyeit.mesh as mesh
from pyeit.eit.fem import Forward
from pyeit.eit.utils import eit_scan_lines

from pyeit.mesh.shape import circle,ellipse,rectangle0,rectangle,box_circle,thorax,L_shaped
import pyeit.eit.jac as jac

#import lung data ( real voltage measurements )
import lungData as ld

""" 1. setup """
# Mesh shape is specified with fd parameter in the instantiation, e.g : fd=thorax , Default :fd=circle
mesh_obj, el_pos = mesh.create(16,h0=0.05,fd=thorax)


# extract node, element, alpha
pts = mesh_obj["node"]
tri = mesh_obj["element"]


""" 2. calculate simulated data using stack ex_mat """
#el_dist is different from the simulation example(the same algorithm at examples folder)
#The adjacent injection pattern is used in the real measurement  
el_dist, step = 1, 1
n_el = len(el_pos)
ex_mat = eit_scan_lines(n_el, el_dist)


""" 3. solving using dynamic EIT """
# number of stimulation lines/patterns
#Ex_mat used is different from the simulation example(the same algorithm at examples folder) : the electrode combination must coincide with the real
#meseaurement electrodes combination used in that example (208=16*13) because it's the adjacent current injection
#pattern which is used in the real measurements

eit = jac.JAC(mesh_obj, el_pos, ex_mat=ex_mat, step=step, parser="std")
eit.setup(p=0.40, lamb=1e-3, method="kotre")
#ld.r_v19 are real thorax voltages measured at the middle of breathing cycle ( see lungData.py )
#ld.w_v are real thorax voltages measured at the beginning of breathing cycle ( see lungData.py )
ds = eit.solve(np.array(ld.r_v19), np.array(ld.w_v), normalize=False)

""" 4. plot """
fig, ax = plt.subplots(figsize=(6, 4))
im = ax.tripcolor(
    pts[:, 0],
    pts[:, 1],
    tri,
    np.real(ds),
    shading="flat",
    alpha=0.90,
    cmap=plt.cm.viridis,
)

#Draw electrodes 
ax.plot(pts[:, 0][el_pos], pts[:, 1][el_pos], "ro")
for i, e in enumerate(el_pos):
    ax.text( pts[:, 0][e],  pts[:, 1][e], str(i + 1), size=12)

fig.colorbar(im)
ax.set_aspect("equal")
ax.set_title(r"$\Delta$ Permittivity Reconstructed")

plt.savefig('Dynamic_stack.png')
#plt.show()
plt.title('Reconstructed image (Dynamic stack)')
plt.figure(1)

#------------------- Deep Learning Layer ------------------#

#####################################################################

from UNET_Segmentor import UNET_Segmentor

UNET_Segmentor().predict()