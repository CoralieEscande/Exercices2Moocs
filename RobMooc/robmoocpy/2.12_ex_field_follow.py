from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

def draw(x):
    clear(ax)
    draw_tank(x,'darkblue',0.3)
    a,b = array([[-30],[0]]), array([[30],[0]])
    draw_segment(a,b,'red',2)
    
def f(x,u):
    θ=x[2,0]
    return array([[cos(θ)], [sin(θ)],[u]])
           

x=array([[-2],[-2],[3]])
dt= 0.05
ax=init_figure(-5,5,-5,5)
for t in arange(0,8,dt):
    draw(x)
    u=0
    x=x+dt*f(x,u)
pause(10)    
