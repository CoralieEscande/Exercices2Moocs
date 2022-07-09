#! /usr/bin/env python3
# coding: utf-8
from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

def draw_pools(x,u):
    x=x.flatten()
    u=u.flatten()
    plot([0,0],[10,1],'black',linewidth=2)    
    plot([-7,23],[0,0],'black',linewidth=5)    
    plot([16,16],[1,10],'black',linewidth=2)    
    plot([4,4,6,6],[10,1,1,10],'black',linewidth=2)    
    plot([10,10,12,12],[10,1,1,10],'black',linewidth=2)    
    P=array([[0,x[0]],[0,1],[-6,0],[22,0],[16,1],[16,x[2]],[12,x[2]],[12,1]
            ,[10,1],[10,x[1]],[6,x[1]],[6,1],[4,1],[4,x[0]]])
    draw_polygon(P,ax,'blue')       
    P=array([[1,10],[1,x[0]],[1+0.1*u[0],x[0]],[1+0.1*u[0],10]])            
    draw_polygon(P,ax,'blue')
    P=array([[13,10],[13,x[2]],[13+0.1*u[1],x[2]],[13+0.1*u[1],10]])            
    draw_polygon(P,ax,'blue')

def q(h):
    a = 0.4
    g = 9.81
    q = a * sign(h) * sqrt(2 * g * abs(h))
    return(q)

def f(x,u):
    x=x.flatten()
    u=u.flatten()
    xdot = array([[-q(x[0]) - q(x[0]-x[1]) + u[0]],
                  [q(x[0]-x[1]) - q(x[1]-x[2])],
                  [-q(x[2]) + q(x[1]-x[2]) + u[1] + 1 ]])
    return(xdot)

def main():
    x = array([[2],[2],[2]])
    z = array([[0],[0]])
    for t in arange(0,10,dt) :
        y = array([[x[0,0]],[x[2,0]]])
        v = z + 2*(w-y) + dw
        b = array([[-q(x[0,0]) - q(x[0,0]-x[1,0])],
                   [-q(x[2,0]) + q(x[1,0]-x[2,0])]])
        u = v - b
        #import pdb; pdb.set_trace()
        clear(ax)
        draw_pools(x,u)
        z = z + (w - y)*dt
        x = x + dt*f(x,u)
    print(y)
        
if __name__ == "__main__":
    """Définition des constantes"""
    dt = 0.05
    #u = array([[10],[1]])
    w = array([[7],[3]])
    dw = array([[0],[0]])
    
    ax = init_figure(-10,25,-2,12)
    
    """ Simulation """
    main()
