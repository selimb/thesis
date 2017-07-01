from math import cos, sin, pi, sqrt
from itertools import izip, tee

lengths = [
    0.9,
    1.0,
    1.1,
    0.8
]
angles = [
    5.0,
    80.0,
    175.0,
    225.0
]
og = (0.0,0.0)
fp_fmt = '\draw [fill] {loc} circle [radius=0.02] node [{opt}] {{{text}}};'

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

def normal(line):
    dx, dy = [line[1][i] - line[0][i] for i in range(2)]
    norm = sqrt(dx**2 + dy**2)
    n = (dy/norm, -dx/norm)
    return n

def deg2rad(deg):
    return deg*pi/180

def fmt_vtx(vtx):
    return '(%.2f,%.2f)' % (vtx[0], vtx[1])

def draw(points, cycle=False, opt=''):
    path = [fmt_vtx(p) for p in points]
    if cycle:
        path = path + ['cycle']
    return '\\draw[%s] ' % opt + ' -- '.join(path) + ';'

def draw_ip(p):
    return '\\node at %s {\\large $\\times$};' % fmt_vtx(p)

def draw_fp(p, loc='', text=''):
    return fp_fmt.format(loc=p, opt=loc, text=text)

def draw_normal(loc, vec, scale=0.08):
    a = loc
    b = [loc[i] + scale*vec[i] for i in range(2)]
    return '\\draw[->,thick] %s -- %s;' % (fmt_vtx(a), fmt_vtx(b))

def centroid(vertices):
    x = []
    y = []
    l = len(vertices)
    for v in vertices:
        x.append(v[0])
        y.append(v[1])

    xavg = sum(x)/l
    yavg = sum(y)/l
    return (xavg, yavg)

VERTICES = [og]
cur = og
for l, a in zip(lengths, angles):
    rad = deg2rad(a)
    new = (cur[0] + l*cos(rad), cur[1] + l*sin(rad))
    VERTICES.append(new)
    cur = new

CENTER = (0.3, 0.6)
parts = []
for v in VERTICES:
    parts.append(v)
print draw(parts, True)

for v in VERTICES:
    print draw_fp(v)

print draw_fp(CENTER, loc='above=3pt,xshift=3pt', text='\\Large $P$')

for v in VERTICES:
    parts = [CENTER, v]
    print draw(parts)

ELEMENTS = []
for i in range(len(VERTICES) - 1):
    e = [VERTICES[i], VERTICES[i+1]]
    ELEMENTS.append(e)

ELEMENTS.append([VERTICES[-1], VERTICES[0]])
num_elements = len(ELEMENTS)

int_surface = []
for e in ELEMENTS:
    p = centroid([e[0], CENTER])
    int_surface.append(p)
    elem_center = centroid(e + [CENTER])
    int_surface.append(elem_center)

    print draw([elem_center, centroid(e)], opt='dashed,thick')

int_surface.append(int_surface[0])
print draw(int_surface, opt='fill=gray,fill opacity=0.5,dashed,thick')

for surf in pairwise(int_surface):
    ip = centroid(surf)
    print draw_ip(ip)
    n = normal(surf)
    # print draw_normal(ip, n)

