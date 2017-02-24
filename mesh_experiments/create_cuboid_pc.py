import random
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_point_cloud(l,b,h, num_points=1000, rand=False):
    point_cloud = []
    points_l = np.linspace(0,l,num_points)
    points_b = np.linspace(0,b,num_points)
    points_h = np.linspace(0,h,num_points)

    for i in range(num_points):

        if not rand:
            for j in range(num_points):
                for k in range(num_points):
                    point_cloud.append(np.array([points_l[i], points_b[j], points_h[k]]))
        else:

            point_cloud.append(np.array([random.uniform(0,l),random.uniform(0,b),random.uniform(0,h)]))

    return np.asarray(point_cloud)


def create_mesh_from_point_cloud(point_cloud):

    tri =  Delaunay(point_cloud)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(point_cloud[:,0], point_cloud[:,1], point_cloud[:,2], 
                    triangles=tri.simplices, cmap=plt.cm.Spectral)
    plt.show()


def main():

    length = 1
    breadth = 1
    height =  1
    point_cloud =  generate_point_cloud(length,breadth, height, 10, True)
    create_mesh_from_point_cloud(point_cloud)



if __name__ == '__main__':
    main()





