import numpy as np
import trimesh


# attach to trimesh logs
trimesh.util.attach_to_log()

# load a file by name or from a buffer
mesh = trimesh.load_mesh('mesh.STL')


# mesh.fill_holes()


meshes = mesh.split(only_watertight=False)

# the convex hull of every component
meshes_convex = [i.convex_hull for i in meshes]

# combine all components into one mesh
convex_combined = np.sum(meshes_convex)

convex_combined.show()

convex_combined.export('mesh_hull.STL', 'stl')

# is the current mesh watertight?
print mesh.is_watertight

# what's the euler number for the mesh?
print mesh.euler_number


# the convex hull is another Trimesh object that is available as a property
# lets compare the volume of our mesh with the volume of its convex hull
print np.divide(mesh.volume, mesh.convex_hull.volume)


# since the mesh is watertight, it means there is a
# volumetric center of mass which we can set as the origin for our mesh
mesh.vertices -= mesh.center_mass


# what's the moment of inertia for the mesh?
print mesh.moment_inertia

# if there are multiple bodies in the mesh we can split the mesh by
# connected components of face adjacency
# since this example mesh is a single watertight body we get a list of one mesh
mesh.split()

# find groups of coplanar adjacent faces
facets, facets_area = mesh.facets(return_area=True)

# set each facet to a random color
# colors are 8 bit RGBA by default (n,4) np.uint8
for facet in facets:
    mesh.visual.face_colors[facet] = trimesh.visual.random_color()


mesh.export('tri_meshed_test_pcd_mug.STL', 'stl')

# preview mesh in an opengl window if you installed pyglet with pip
mesh.show()


# transform method can be passed a (4,4) matrix and will cleanly apply the transform
mesh.apply_transform(trimesh.transformations.random_rotation_matrix())

# an axis aligned bounding box is available
print mesh.bounding_box.primitive.extents

# a minimum volume oriented bounding box is available
print mesh.bounding_box_oriented.primitive.transform


# show the mesh overlayed with its oriented bounding box
# the bounding box is a trimesh.primitives.Box object, which subclasses
# Trimesh and lazily evaluates to fill in vertices and faces when requested
# (press w in viewer to see triangles)
(mesh + mesh.bounding_box_oriented).show()

# bounding spheres and bounding cylinders of meshes are also
# available, and will be the minimum volume version of each
# except in certain degenerate cases, where they will be no worse
# than a least squares fit version of the primitive.
print(mesh.bounding_box_oriented.volume, 
      mesh.bounding_cylinder.volume,
      mesh.bounding_sphere.volume)

