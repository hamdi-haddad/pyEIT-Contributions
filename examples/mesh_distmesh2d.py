# import mesh shape from shape.py file 
from pyeit.mesh.shape import circle,ellipse,rectangle0,rectangle,box_circle,thorax,area_uniform

#....#


def example6():
    """ Thorax mesh """

    # build fix points, may be used as the position for electrodes
    num = 16

    el_pos = np.arange(num)
    p_fix= [(0.1564, 0.6571), (0.5814, 0.6353), (0.8298, 0.433), (0.9698, 0.1431), (0.9914, -0.1767), (0.8359, -0.449), (0.5419, -0.5833), (0.2243, -0.6456), (-0.098, -0.6463), (-0.4181, -0.6074), (-0.7207, -0.4946), (-0.933, -0.2647), (-0.9147, 0.0543), (-0.8022, 0.3565), (-0.5791, 0.5864), (-0.1653, 0.6819)]
    # build triangles
    p, t = distmesh.build(thorax, fh=area_uniform ,pfix=p_fix, h0=0.05)
    # plot
    fig, ax = plt.subplots()
    ax.triplot(p[:, 0], p[:, 1], t)
    ax.plot(p[el_pos, 0], p[el_pos, 1], "ro")
    ax.set_aspect("equal")
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.1, 1.1])
    ax.set_title("Thorax mesh")
    plt.show()

if __name__ == "__main__":
    example6()