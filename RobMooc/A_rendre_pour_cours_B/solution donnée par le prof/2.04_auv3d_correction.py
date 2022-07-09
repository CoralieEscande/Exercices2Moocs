from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

              
def draw(x,w):
    clean3D(ax,-30,30,-30,30,0,60)
    draw_axis3D(ax,0,0,0,eye(3,3),10)
    draw_robot3D(ax,x[0:3],eulermat(*x[4:7,0]),'blue')
    ax.scatter(*w[0:3,0],color='magenta')
       
def f(x,u):
    x,u=x.flatten(),u.flatten()
    v,φ,θ,ψ=x[3],x[4],x[5],x[6];
    cφ,sφ,cθ,sθ,cψ,sψ= cos(φ),sin(φ),cos(θ),sin(θ),cos(ψ),sin(ψ)
    return array([ [v*cθ*cψ],[v*cθ*sψ],[-v*sθ],[u[0]] ,
                    [-0.1*sφ*cθ + tan(θ)*v*(sφ*u[1]+cφ*u[2])] ,
                     [cφ*v*u[1] - sφ*v*u[2]] ,
                     [(sφ/cθ)*v*u[1] + (cφ/cθ)*v*u[2]]])
    
def control(x,w,dw,ddw):
    p = x[0:3,:]
    print(p)
    x=x.flatten()
    v,φ,θ,ψ=x[3],x[4],x[5],x[6];
    cψ,sψ,cθ,sθ,cφ,sφ = cos(ψ),sin(ψ),cos(θ),sin(θ),cos(φ),sin(φ)
    A1 = array([[cθ*cψ,-v*cθ*sψ,-v*sθ*cψ],[cθ*sψ,v*cθ*cψ,-v*sθ*sψ],[-sθ,0,-v*cθ]])
    A2 = array([[1, 0, 0],[0,v*sφ/cθ,v*cφ/cθ],[0,v*cφ,-v*sφ]])
    dp = array([[v*cθ*cψ],[v*cθ*sψ],[-v*sθ]])
    u = inv(A1 @ A2) @ (0.04*(w-p) + 0.4*(dw-dp) + ddw)
    return u
        
def setpoint(t):
    f1,f2,f3,R = 0.01,0.06,0.03,20
    s1,s2,s3,c1,c2,c3=sin(f1*t),sin(f2*t),sin(f3*t),cos(f1*t),cos(f2*t),cos(f3*t)
    w = R*array([[s1+s2],[c1+c2],[s3]])
    dw = R*array([[f1*c1+f2*c2],[-f1*s1-f2*s2],[f3*c3]])
    ddw = R*array([[-f1**2*s1-f2**2*s2],[-f1**2*c1-f2**2*c2],[-f3**2*s3]])
    return w,dw,ddw

ax = Axes3D(figure())    
x = array([[0,0,1,0.1,0,0,0]]).T
dt = 0.1
for t in arange(0,50,dt):
    w,dw,ddw=setpoint(t)
    u = control(x,w,dw,ddw)
    x = x + dt * f(x,u)
    draw(x,w)
    pause(0.001)


    
