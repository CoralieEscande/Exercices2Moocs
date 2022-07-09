from autolib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

def clock(x):
    x1,x2,ψ=x.flatten()
    u=0.3
    clear(ax); 
    draw_tank(x,'blue',0.1,2)
    x=x+dt*array([[cos(ψ)], [sin(ψ)],[u]])
    return x
    

x=array([[-3],[1],[-1]])
ax=init_figure(-4,4,-1,7)
dt=0.1

while (True):   
    x=clock(x)



    
    


