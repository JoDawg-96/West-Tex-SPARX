import numpy as np
from stl import mesh
from stl.base import AREA_SIZE_THRESHOLD

global d
d = 1277
global small
small = 1000000000
global big
big = -1000000000
f = open("C:/Data/RDF_HEIGHT.csv", "r")

while f:
    line = f.readline()
    if line == "":
        break
    hValues = np.array(line.split(","))
    res = hValues.astype(np.float)

    if min(res) < small:
        small = min(res)
    if max(res) > big:
        big = max(res)

v = []
f.seek(0)

i = 0
while f:

    line = f.readline()
    if line == "":
        break
    hValues = np.array(line.split(","))
    res = hValues.astype(np.float)
    
    j = 0
    for n in res:
        v.append([i,j,n/40])
        j = j+1
    i = i+1
v.append([0,0,-d])
f.close()
#print(v[len(v)-1])

p = []
for i in range(len(v)-d-1):
    if (i+1)%d == 0:
        p.append([i,i+d,d*d])
    else:
        p.append([i,i+1,i+d])
        p.append([i+d,i+1,i+d+1])

vertices = np.array(v)
faces = np.array(p)

# Create the mesh
cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        cube.vectors[i][j] = vertices[f[j],:]

# Write the mesh to file "cube.stl"
cube.save('C:/Data/cube.stl')