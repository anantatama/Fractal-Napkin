import random
from collections import deque
from PIL import Image
imgx = 300
imgy = 300
mat=[[0.0,0.0,0.0,0.16,0.0,0.0,0.01],
     [0.85,0.04,-0.04,0.85,0.0,1.6,0.85],
     [0.2,-0.26,0.23,0.22,0.0,1.6,0.07],
     [-0.15,0.28,0.26,0.24,0.0,0.44,0.07]]

m = len(mat) #4

#Untuk mencari xa, ya, xb, yb
x = mat[0][4]
y = mat[0][5] 
xa = x
xb = x
ya = y
yb = y
for k in range(imgx * imgy):
    p = random.random()
    psum = 0.0
    for i in range(m):
        psum += mat[i][6]
        if p <= psum:
            break
    x0 = x * mat[i][0] + y * mat[i][1] + mat[i][4] 
    y  = x * mat[i][2] + y * mat[i][3] + mat[i][5] 
    x = x0 
    if x < xa:
        xa = x
    if x > xb:
        xb = x
    if y < ya:
        ya = y
    if y > yb:
        yb = y

imgy = int(imgy * (yb - ya) / (xb - xa))
image = Image.new("RGB", (imgx, imgy)) #Dicoba pakai L tapi hasilnya malah putih semua, sehingga pakainya RGB

maxIt = 16
for ky in range(imgy):
    for kx in range(imgx):
        x = float(kx) / (imgx - 1) * (xb - xa) + xa
        y = float(ky) / (imgy - 1) * (yb - ya) + ya
        queue = deque([])
        queue.append((x, y, 0))
        while len(queue) > 0: # iterasi titik sampai habis
            (x, y, i) = queue.popleft()
            for j in range(m):
                d = mat[j][0] * mat[j][3] - mat[j][2] * mat[j][1]
                if d != 0.0:
                    xnew = ((x - mat[j][4]) * mat[j][3] - (y - mat[j][5]) * mat[j][1]) / d
                    ynew = ((y - mat[j][5]) * mat[j][0] - (x - mat[j][4]) * mat[j][2]) / d
                    if xnew >= xa and xnew <= xb and ynew >= ya and ynew <= yb:
                        if i + 1 == maxIt: break
                        queue.append((xnew, ynew, i + 1))

        image.putpixel((kx, ky), (i % 8 * 32, i % 16 * 16, i % 32 * 8))

final = image.rotate(180) #Hasil gambar kebalik, belum ketemu titik terang. Sementara dirotate dulu
final.save("IFSfractalUsingIterationMethod.png", "PNG")