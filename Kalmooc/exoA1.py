"""
créé le 29 juin 2022
par Coralie Escande

Kalmooc leçon A - exercice 1 : représentation d'une fonction quadratique
"""

from mpl_toolkits import mplot3d 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def maillage():
    # création du maillage
    Mx = np.arange(-1,1,0.1)
    My = Mx
    #print(Mx)
    [X, Y] = np.meshgrid(Mx, My)
    #print(X)
    #print (Y)
    # affichage du maillage
    fig, ax = plt.subplots()
    ax.scatter(X, Y, color="green")
    ax.set_title('Regular Grid, created by Meshgrid')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.show()
    return(X,Y,Mx,My)

def gradient_f(X,Y):
    # Gradient de la fonction f
    GX = Y
    GY = X
    return(GX,GY)

def gradient_g(x,y):
    # Gradient de la fonction g
    GX = 4*x + y - 1
    GY = x + 8*y + 1
    return(GX,GY)

def show_gradient(GX,GY, Mx, My, X, Y):
    #affichage du champ de gradients
    plt.quiver(Mx, My, GX, GY)
    plt.show()
    plt.quiver(X, Y, GX, GY)
    plt.show()

def fct_f(X,Y):
    #Calcul de la fonction f
    Z = X*Y #multiplication élément par élément
    return Z

def fct_g(X,Y):
    #Calcul de la fonction g
    Z = 2*X**2 + x*y + 4*y**2 + y - x + 3
    return Z

def surface_and_contour(X,Y,Z):
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

(X,Y,Mx,My) = maillage()
(GX,GY) = gradient_f(X,Y)
show_gradient(GX,GY, Mx, My, X, Y)
Z = fct_f(X,Y)
surface_and_contour(X,Y,Z)
