import numpy as np
from .shape import fix_points_fd, fix_points_ball

#import different shapes to create your convenient mesh (thorax and L_shaped mesh : added , ball(3D) : debugged)
from .shape import circle, area_uniform, ball, thorax,L_shaped

#fd: parameter that defines the mesh type, is set to None in default case, to generate the appropriate condition (which depends on bbox dimension ( see underneath ))  
def create(n_el=16, fd=None, fh=area_uniform, h0=0.1, p_fix=None, bbox=None):
      
    #....#

    # test conditions if fd or/and bbox are none
    if bbox is None:
        if fd!=ball:
             bbox = np.array([[-1, -1], [1, 1]])
        else : 
             bbox = [[-1.2, -1.2, -1.2], [1.2, 1.2, 1.2]]

    bbox = np.array(bbox)  # list is converted to Numpy array so we can use it then (calling shape method..)
    n_dim = bbox.shape[1]  # bring dimension of bbox 

    # test on fd to set mesh type 
    if fd is None:
        if n_dim==2:
             fd=circle
        elif n_dim==3:
             fd=ball

     #....#

    if p_fix is None:                 
        if n_dim == 2:
           
            if fd==thorax:
                # Set thorax electrode positions ( electrode points coordinates ): you can change the disposition depending on the electrodes disposition of the forward problem mesh 
                p_fix= [(0.1564, 0.6571), (0.5814, 0.6353), (0.8298, 0.433), (0.9698, 0.1431), (0.9914, -0.1767), (0.8359, -0.449), (0.5419, -0.5833), (0.2243, -0.6456), (-0.098, -0.6463), (-0.4181, -0.6074), (-0.7207, -0.4946), (-0.933, -0.2647), (-0.9147, 0.0543), (-0.8022, 0.3565), (-0.5791, 0.5864), (-0.1653, 0.6819)]
                p_fix = np.array(p_fix)
                #smaller mesh size in thorax gives better results 
                h0=0.05  
    
            elif fd==L_shaped:
                # Set fixed points of L_shaped mesh 
                p_fix = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [0, 0]] #values brought from distmesh2D L shaped mesh example
                p_fix = np.array(p_fix)
                h0=0.15
        
            else:
                p_fix = fix_points_fd(fd, n_el=n_el)
            
        elif n_dim == 3:
            p_fix = fix_points_ball(n_el=n_el)
