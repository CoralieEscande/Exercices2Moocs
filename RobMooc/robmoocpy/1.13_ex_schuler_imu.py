from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

def f(x):
    x=x.flatten()
    return (array([[1],[0],[2],[0] ]))

        
r=10
g = 9.81
dt=0.005;
x=array([[r],[0],[0],[0]])


ech=5
ax=init_figure(r-ech,r+ech,-ech,ech)
clear(ax)
draw_disk(array([[0],[0]]),r,ax,"grey")
for t in arange(0,1,dt) :
    x=x+dt*(0.25*f(x)+0.75*(f(x+dt*(2/3)*f(x)))); # Runge Kutta
    draw_tank(array([x[0],x[2],0]),'blue',0.01,1)    
pause(1)    