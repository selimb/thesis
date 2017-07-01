tikz = '''
  \draw (-0.05,-0.02) -- (0.0,0.0) -- (0.7, 0.03) -- (1.5, 0.0) -- (2.2, 0.0) -- (2.25, -0.02);
  \draw (0.05,0.6) -- (0.1, 0.7) -- (0.68, 0.72) -- (1.53, 0.62) -- (2.15, 0.60) -- (2.2, 0.61);
  \draw (0.0, 1.2) -- (0.05, 1.21) -- (0.83, 1.28) -- (1.58, 1.2) -- (2.2, 1.18) -- (2.25, 1.19);
  \draw (0.03, 1.7) -- (0.08, 1.70) -- (0.77, 1.65) -- (1.5, 1.67) -- (2.12, 1.7) -- (2.17, 1.72);'''

ni = nj = 4
coords = [[(None, None) for i in range(ni)] for j in range(nj)]
lines = tikz.split('\n')

j = 0
for line in lines[1:]:
    i = 0
    points = line.split('--', 1)[1].split('--')[:-1]
    for p in points:
        c = eval(p)
        coords[j][i] = c
        i += 1

    j += 1

print(coords)

def loc(p, v):
    if p == 0:
        return '%s    ' % v
    elif p == 1:
        return '%s+1' % v
    elif p == -1:
        return '%s-1' % v
    else:
        print('DA FUCK')
for i in range(ni - 1):
    for j in range(nj - 1):
        x = []
        y = []
        for l in (0, 1):
            for m in (0, 1):
                c = coords[j+l][i+m]
                x.append(c[0])
                y.append(c[1])
                points.append(coords[j+l][i+m])

        xavg = sum(x)/len(x)
        yavg = sum(y)/len(y)
        ip = i - 1
        jp = j - 1
        ii = loc(ip, 'i')
        jj = loc(jp, 'j')
        print('\draw[fill] (%.3f, %.3f) circle [radius=0.02] node [above] {%s, %s};' % (xavg, yavg, ii, jj))
