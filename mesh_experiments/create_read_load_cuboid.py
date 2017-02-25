
from openmesh import *
import pybullet as pb
import sys

# sys.path.append('./markup110')
# import markup


def generate_point_cloud():
    pass


def create_mesh():
    mesh = TriMesh()

    vh0 = mesh.add_vertex(TriMesh.Point(0, 1, 0))
    vh1 = mesh.add_vertex(TriMesh.Point(1, 0, 0))
    vh2 = mesh.add_vertex(TriMesh.Point(2, 1, 0))
    vh3 = mesh.add_vertex(TriMesh.Point(0,-1, 0))
    vh4 = mesh.add_vertex(TriMesh.Point(2,-1, 0))

    fh0 = mesh.add_face(vh0, vh1, vh2)
    fh1 = mesh.add_face(vh1, vh3, vh4)
    fh2 = mesh.add_face(vh0, vh3, vh1)
    vh_list = [vh2, vh1, vh4]
    fh3 = mesh.add_face(vh_list)

    write_mesh(mesh, "cube.obj")


def main():
    phys_id = pb.connect(pb.SHARED_MEMORY)
    if (phys_id<0):
        phys_id = pb.connect(pb.GUI)
    
    pb.resetSimulation()
    
    pb.setTimeStep(0.01)

    world = pb.loadURDF('myworld.urdf')
    
    mycube = pb.loadURDF('pcd_stl.urdf')
    
    pb.setGravity(0., 0.,-10.)

    pb.setRealTimeSimulation(0)

    while True:
        pb.stepSimulation()


if __name__ == '__main__':
    # create_mesh()
    main()