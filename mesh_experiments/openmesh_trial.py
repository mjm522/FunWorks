from openmesh import *

mesh = TriMesh()

vh0 = mesh.add_vertex(TriMesh.Point(0, 1, 0))
vh1 = mesh.add_vertex(TriMesh.Point(1, 0, 0))
vh2 = mesh.add_vertex(TriMesh.Point(2, 1, 0))
vh3 = mesh.add_vertex(TriMesh.Point(0,-1, 0))
vh4 = mesh.add_vertex(TriMesh.Point(2,-1, 0))

fh0 = mesh.add_face(vh0, vh1, vh2)
fh1 = mesh.add_face(vh1, vh3, vh4)
fh2 = mesh.add_face(vh0, vh3, vh1)

# vh_list = [vh2, vh1, vh4]
# fh3 = mesh.add_face(vh_list)

for vh in mesh.vertices():
    print vh.idx()

# iterate over all halfedges
for heh in mesh.halfedges():
    print heh.idx()
# iterate over all edges
for eh in mesh.edges():
    print eh.idx()
# iterate over all faces
for fh in mesh.faces():
    print fh.idx()

for vh in mesh.vv(vh1):
    print vh.idx()

# iterate over all incoming halfedges
for heh in mesh.vih(vh1):
    print heh.idx()
# iterate over all outgoing halfedges
for heh in mesh.voh(vh1):
    print heh.idx()
# iterate over all adjacent edges
for eh in mesh.ve(vh1):
    print eh.idx()
# iterate over all adjacent faces
for fh in mesh.vf(vh1):
    print fh.idx()


# iterate over the face's vertices
for vh in mesh.fv(fh0):
    print vh.idx()
# iterate over the face's halfedges
for heh in mesh.fh(fh0):
    print heh.idx()
# iterate over the face's edges
for eh in mesh.fe(fh0):
    print eh.idx()
# iterate over all edge-neighboring faces
for fh in mesh.ff(fh0):
    print fh.idx()


write_mesh(mesh, "cube.obj")


new_mesh = TriMesh()
new_mesh.request_halfedge_normals()
new_mesh.request_vertex_normals()
options = Options()
options += Options.VertexNormal
result = read_mesh(new_mesh, "cube.obj", options)
if result:
        print "everything worked"
else:
        print "something went wrong"