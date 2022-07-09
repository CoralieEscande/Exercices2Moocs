from autolib import *  # https://www.ensta-bretagne.fr/jaulin/autolib.py


def u(t): return array([[cos(t)],[sin(t)]]) 
       
def f(x,t):
    x1,x2,x3,x4,x5=list(x[0:5,0])
    u1,u2=list(u(t)[0:2,0])
    return array([[x4*cos(x3)],[x4*sin(x3)],[x5],[u1],[u2]])
    
def clock_Euler(x,t,dt): return x+dt*f(x,t) 

    
def simu(x0,dt,k0,s):
    k=0
    xe=x0
    for t in arange(0,tmax,dt): 
        xe=clock_Euler(xe,t,dt)
        if k%k0==0:
            draw_tank(xe,"red",s)
            pause(0.001)              
        k=k+1
        


ax=init_figure(-13,17,-4,7)
x0=array([[0],[0],[0],[5],[-1/2]]) #x,y,θ,v,w
tmax=12
dt=0.05
simu(x0,dt,5,0.2)

    
pause(2)
