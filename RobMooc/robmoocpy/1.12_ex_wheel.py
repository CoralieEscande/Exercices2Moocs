from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

def draw(x):
    ax.clear()
    ax.set_xlim3d(-ech,ech)
    ax.set_ylim3d(-ech,ech)
    ax.set_zlim3d(0,2*ech)    
    x=x.flatten()    
    draw_wheel3D(ax,*x[0:6])
    φ,θ,ψ=x[3:6]
    E=eulermat(φ,θ,ψ)
    p=x[0:3].reshape(3,1) #center of the wheel
    wr=(x[9:12]).reshape(3,1)   
    w=E@wr
    draw_axis3D(ax,0,0,0,eye(3,3))
    draw_axis3D(ax,*p,E)

         
        
def f(x):
    x=x.flatten()
    return array([[0.1],[0.1],[0.2],[2],[0.1],[0.1],[0.0],[0],[0],[0],[0],[0]])
         
    
    

fig = figure()
ax = Axes3D(fig)
dt = 0.05  
ech=2
m,ρ=1,1

x=array([[0],[0],[2],[0],[0],[0],[5],[0],[0],[5],[1],[0]])  #x,y,z,   φ,θ,ψ   vr  wr     
for t in arange(0,10,dt):
    x=x+dt*f(x)
    draw(x)
    pause(0.001)
pause(1)    

