import numpy as np
from PIL import Image

global small
small = 1000000000
global big
big = -1000000000
#f = open("C:/Data/RdF_HEIGHT.csv", "r")
f = open("C:/Data/RdF_SLOPE.csv", "r")

while f:
    line = f.readline()
    if line == "":
        break
    hValues = np.array(line.split(","))
    res = hValues.astype(np.float)
    print(res)

    if min(res) < small:
        small = min(res)
    if max(res) > big:
        big = max(res)

f.seek(0)

img = Image.new('RGB', (1277, 1277))
pixels_new = img.load()
i = 0
while f:

    line = f.readline()
    if line == "":
        break
    hValues = np.array(line.split(","))
    res = hValues.astype(np.float)
    
    j = 0
    for n in res:
        #newVal = int((n-small)/(big-small) * 256) #Reversed colors
        newVal = int((big-n+small)/(big-small) * 256)
        pixels_new[j, i] = (newVal, newVal, newVal, 255)
        j = j+1
    i = i+1
img.save("heightmap.jpg", "JPEG")