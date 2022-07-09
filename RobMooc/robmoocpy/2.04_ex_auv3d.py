from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
fig = figure()
ax = Axes3D(fig)

def draw(x):
    x = x.flatten()    
    ax.clear()
    ax.set_xlim3d(-20,20)
    ax.set_ylim3d(-20,20)
    ax.set_zlim3d(0,40)
    draw_axis3D(ax,0,0,0,eye(3,3),10)

    draw_auv3D(ax,x[0],x[1],x[2],x[4],x[5],x[6],'blue') 
    ax.scatter(0,0,0,color='magenta')
           

def f(x,u):
    x,u=x.flatten(),u.flatten()
    v,φ,θ,ψ=x[3],x[4],x[5],x[6];
    cφ,sφ,cθ,sθ,cψ,sψ= cos(φ),sin(φ),cos(θ),sin(θ),cos(ψ),sin(ψ)
    return array([ [v*cθ*cψ],[v*cθ*sψ],[-v*sθ],[u[0]] ,
                    [-0.1*sφ*cθ + tan(θ)*v*(sφ*u[1]+cφ*u[2])] ,
                     [cφ*v*u[1] - sφ*v*u[2]] ,
                     [(sφ/cθ)*v*u[1] + (cφ/cθ)*v*u[2]]])
              
x = array([[0,0,10,15,0,1,0]]).T
u = array([[0,0,0.1]]).T
dt = 0.05
for t in arange(0,2,dt):
    xdot=f(x,u)
    x = x + dt * xdot
    draw(x)
    pause(0.001)