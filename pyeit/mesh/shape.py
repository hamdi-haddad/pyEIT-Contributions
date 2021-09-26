import numpy as np

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


#....#

def thorax(pts):
    
    '''
     p : Nx2 ndarray

    returns boolean ndarray specifiying whether the point is inside thorax or not 
    e.g :
    array([[False, False],
       [ True,  True],
       [ True,  True]])

    '''
    # Thorax contour points coordinates are taken from a thorax simulation based on a CT thorax image from EIDORS library 
    thrx = Polygon([(0.0487,0.6543),(0.1564,0.6571),(0.2636,0.6697),(0.3714,0.6755),
                (0.479,0.6686),(0.5814,0.6353),(0.6757,0.5831),(0.7582,0.5137),
                (0.8298,0.433),(0.8894,0.3431),(0.9347,0.2452) ,(0.9698,0.1431),
                (0.9938,0.0379),(1.0028,-0.0696),(0.9914,-0.1767),(0.9637,-0.281),
                (0.9156,-0.3771),(0.8359,-0.449),(0.7402,-0.499),(0.6432,-0.5463),
                (0.5419,-0.5833),(0.4371,-0.6094),(0.3308,-0.6279),(0.2243,-0.6456),
                (0.1168,-0.6508),(0.0096,-0.6387),(-0.098,-0.6463),(-0.2058,-0.6433),
                (-0.313,-0.6312),(-0.4181,-0.6074),(-0.5164,-0.5629),(-0.6166,-0.5232),
                (-0.7207,-0.4946),(-0.813,-0.4398) ,(-0.8869,-0.3614),(-0.933,-0.2647),
                (-0.9451,-0.1576),(-0.9425,-0.0498),(-0.9147,0.0543),(-0.8863,0.1585),
                (-0.8517,0.2606),(-0.8022,0.3565),(-0.7413,0.4455),(-0.6664,0.5231),
                (-0.5791,0.5864),(-0.4838,0.6369),(-0.3804,0.667),(-0.2732,0.6799),
                (-0.1653,0.6819),(-0.0581,0.6699)])

    pts_ = [ Point(p[0],p[1]) for p in pts ]
    
    ba = [ [thrx.contains(pt),thrx.contains(pt)] for pt in pts_]   # ba : boolean "array" , will be then converted to an array
                                                                                 # initialized as list because it's smoother in initialization 
                                                                                 # compared to an array (in first append : axis=1,>=second :axis=0)
    ba = np.array(ba); 

    return ba


# L_shaped mesh function  ( already exists but it's now defined as a normal shape function )
def L_shaped(pts):
            ''' 
            dist_diff and rectangle functions are already defined in shape.py file in pyEIT library 
            '''  
            return dist_diff(
            rectangle(pts, p1=[-1, -1], p2=[1, 1]),
            rectangle(pts, p1=[0, 0], p2=[1, 1]),
              )