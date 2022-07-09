from autolib import *  # available at https://www.ensta-bretagne.fr/jaulin/autolib.py

def f(x,u):
    s,θ,ds,dθ=list(x[0:4,0])
    dds=(mr*sin(θ)*(g*cos(θ)- l*dθ**2) + u)/(mc+mr*sin(θ)**2)
    ddθ= (sin(θ)*((mr+mc)*g - mr*l*dθ**2*cos(θ)) + cos(θ)*u)/ (l*(mc+mr*sin(θ)**2))
    return(array([[ds],[dθ],[dds],[ddθ]]))

mc,l,g,mr=5,1,9.81,1
x = array([[0,2,0,0]]).T
xhat = array([[0,0,0,0]]).T                 
dt = 0.01
ax=init_figure(-3,3,-3,3)
for t in arange(0,20,dt) :
    clear(ax)
    u=0
    w=1
    plot(w,0.5,'o')
    draw_invpend(ax,x)
    x = x + dt*f(x,u)  
pause(1)    
