#https://www.ensta-bretagne.fr/jaulin/robmooc.html
from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

        
def h(x,y):
    return 2*exp(-((x+2)**2+(y+2)**2)/10) + 2*exp(-((x-2)**2+(y-2)**2)/10) - 10


def draw_mesh():
    Mx=arange(-L,L,1.5)
    X,Y = meshgrid(Mx,Mx)
    H = h(X,Y)
    ax.plot_surface(X,Y,H)
    #ax.contour(X,Y,H)
    return()
    
def draw(x):
    x = x.flatten()    
    ψ=x[3]
    draw_auv3D(ax,x[0:3],0,0,ψ,'blue',0.1)
    draw_auv3D(ax,array([[x[0],x[1],h(x[0],x[1])]]),0,0,ψ,'black',0.1)
    return()

ax = Axes3D(figure())
x    = array([[2,-1,-1,0]]).T #x,y,z,ψ
L=10 #size of the world
draw_mesh()
draw(x)
pause(2)     
