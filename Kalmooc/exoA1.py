"""
créé le 29 juin 2022
par Coralie Escande

Kalmooc leçon A - exercice 1 : représentation d'une fonction quadratique
"""

from mpl_toolkits import mplot3d 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#maillage
Mx = np.arange(-1,1,0.1)
My = Mx
[X, Y] = np.meshgrid(Mx, My)
#affichage du maillage
fig, ax = plt.subplots()
ax.scatter(X, Y, color="green")
ax.set_title('Regular Grid, created by Meshgrid')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()

# Gradient
GX = Y
GY = X
#affichage du champ de gradients
plt.quiver(Mx, My, GX, GY)
plt.show()

#Calcul de la fonction f
Z = X*Y #multiplication élément par élément

#affichage de la surface et du contour de la fonction f
fig = plt.figure() 
#ax = plt.axes(projection='3d')
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, cmap="autumn_r", lw=0.5, rstride=1, cstride=1, alpha=0.5)
ax.contour3D(X, Y, Z, 50, cmap=cm.cool) 
ax.set_xlabel('x') 
ax.set_ylabel('y') 
ax.set_zlabel('z') 
ax.set_title('contour de la fonction f') 
plt.show()
