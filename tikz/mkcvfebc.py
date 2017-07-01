from utils import *

print draw([(-1.0,0.0),(1.0,0.0)], opt='thin')

VERTICES = [
    (-0.7,0.0),
    (0.0,0.0),
    (0.8,0.0),
    (-0.4,0.5),
    (0.25,0.4),
]

edge_conn = [
    (0,1),
    (0,3),
    (1,2),
    (1,3),
    (1,4),
    (2,4),
    (3,4)
]

face_conn = [
    (0,1,3),
    (1,3,4),
    (1,2,4)
]

for i, vtx in enumerate(VERTICES):
    radius = '0.01'
    if i == 1:
        print draw_fp(vtx, loc='below', text='$P$', radius=radius)
    else:
        print draw_fp(vtx, radius=radius)

for edge in edge_conn:
    points = [VERTICES[n] for n in edge]
    print draw(points)

int_surface = 'E0 F0 E3 F1 E4 F2 E2'
path = []
for e in int_surface.split():
    typ, num = e[0], int(e[1])
    if typ == 'E':
        ids = edge_conn[num]
    elif typ == 'F':
        ids = face_conn[num]
    pts = [VERTICES[n] for n in ids]
    path.append(centroid(pts))

print draw(path, cycle=True, opt='fill=gray,opacity=0.5,draw=none')
print draw(path, opt='dashed,thick')

for edge in [edge_conn[0], edge_conn[2]]:
    ec = centroid([VERTICES[n] for n in edge])
    ip = centroid([ec, VERTICES[1]])
    print draw_ip(ip)

