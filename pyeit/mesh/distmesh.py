# coding: utf-8
# pylint: disable=invalid-name, no-member, no-name-in-module
# pylint: disable=too-many-arguments, too-many-locals
# pylint: disable=too-many-instance-attributes
""" implement 2D/3D distmesh """
# Copyright (c) Benyuan Liu. All rights reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
from __future__ import division, absolute_import, print_function

from itertools import combinations
import numpy as np
from numpy import sqrt
from scipy.spatial import Delaunay
from scipy.sparse import csr_matrix

from .utils import dist, edge_project

from .shape import thorax

class DISTMESH:
    """ class for distmesh """

    def __init__(
        self,
        fd,
        fh,
        h0=0.1,
        p_fix=None,
        bbox=None,
        density_ctrl_freq=30,
        deltat=0.1,
        dptol=0.001,
        ttol=0.1,
        Fscale=1.2,
        verbose=False,
    ):

        '''
        keep points that are inside the thorax shape using a function that returns a matrix containing
        True if the corresponing point is inside the shape, False if not . 
        p : are points coordinates NX2 matrix 
        '''

        if (fd==thorax):
            p = p[fd(p)]
        else:
            # keep points inside (minus distance) with a small gap (geps)
            p = p[fd(p) < self.geps]  # pylint: disable=E1136

        #....#


        # convert boolean array to 2D to be compatible with Delaunay pts paramater (must be 2D)  
        if (fd==thorax):
            p = np.reshape(p, (-1, 2))  


        #....#


    def triangulate(self):
   
        #....#

        # triangles where the points are arranged counterclockwise
        if (self.fd!=thorax):
             tri = Delaunay(self.p).simplices
        else :
             #QJ parameter is added in case of thorax shape so tuples don't exceed boundary 
             tri = Delaunay(self.p,qhull_options="QJ").simplices

        #....#

        if (self.fd!=thorax):  
            # keeps only interior points
            t = tri[self.fd(pmid) < -self.geps]
        else : 
            #adapting returned triangles matrix with the thorax integrated fd
            tri_pmid = [ p[0] for p in self.fd(pmid) ]
            tri_pmid = np.array(tri_pmid)
            t = tri[ tri_pmid ]

        #....#

#....#

def build(
    fd, fh, pfix=None, bbox=None, h0=0.1, densityctrlfreq=10, maxiter=500, verbose=False
):
        #....#

    for i in range(maxiter):

        #....#

        #So far, thorax mesh is created without mesh iteration ( to be improved )
        if ( fd!=thorax): 
            # update p
            converge = dm.move_p(Ftot)

            # the stopping ctriterion (movements interior are small)
            if converge:
                break
        else:            
            break

        #....#