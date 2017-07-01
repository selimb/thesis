from utils import *

def interp(a, b, ratio):
    l = len(a)
    ret = [(b[i] - a[i])*ratio + a[i] for i in range(l)]
    return ret

def doit(vertices):
    N = len(vertices)
    locs = ['below', 'below', 'above', 'above']

    for i, (vtx, loc) in enumerate(zip(vertices, locs)):
        print draw_fp(vtx, loc=loc, text=str(i+1), radius='0.01')

    center = centroid(vertices)
    edges = [(vertices[i],vertices[ (i+1)%N]) for i in range(N)]
    for edge in edges:
        ec = centroid(edge)
        line = [ec, center]
        print draw(line, opt='dashed')
        print draw_ip(centroid(line), size='')

    print draw(vertices, cycle=True)
    points = [
        interp(vertices[0], vertices[1], 0.2),
        vertices[0],
        interp(vertices[0], vertices[N-1], 0.2)
    ]
    points = map(fmt_vtx, points)
    p0, p1, p2 = points
    print '\\draw [thick, <->] %s node [below right] {$s$} -- %s -- %s node [left] {$t$};' % (p0, p1, p2)

vertices = [
    (0.0,0.0),
    (1.0,0.0),
    (1.0,1.0),
    (0.0,1.0)
]
doit(vertices)

print '\\draw [very thick, ->] (1.3, 0.5) -- (1.7, 0.5);'

vertices = [
    (2.0,0.0),
    (2.8,0.0),
    (2.9,1.1),
    (2.05,1.0)
]
doit(vertices)

