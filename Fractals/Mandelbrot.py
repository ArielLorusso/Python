import matplotlib.pylab as plt
import math 

window_size = 600
zoom = 1
center = window_size/2
atoms=[]
mat = []

for y in range(window_size):
    mat.append([])
    for x in range(window_size):
        mat[y].append(0)
       
        dx = (x-center )/(zoom*center)
        dy = (y-center )/(zoom*center)
        a = dx
        b = dy
        
        for t in range(30):
            d = (a*a)-(b*b)+dx
            b = 2*(a*b)+dy
            a = d
            H = d > 200
            if(H==True):
                mat[y][x] = t
plt.imshow(mat)
plt.show()