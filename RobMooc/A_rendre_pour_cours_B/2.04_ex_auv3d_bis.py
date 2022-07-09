from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

fig = figure()
ax = Axes3D(fig)

def draw(x,w):
    x = x.flatten()
    ψx,θx,φx = x[4],x[5],x[6];
    w = w.flatten()

    ax.clear()
    ax.set_xlim3d(-30,30)
    ax.set_ylim3d(-30,30)
    ax.set_zlim3d(-30,30)
    draw_axis3D(ax,0,0,0,eye(3,3),10)

    draw_auv3D(ax,x[0],x[1],x[2],φx,θx,ψx,'blue')

    #draw_auv3D(ax,w[0],w[1],w[2],ψx,θx,φx,'red')
    ax.scatter(w[0],w[1],w[2],color='red')
    
    ax.scatter(0,0,0,color='magenta')
           

def f(x,u):
    x,u = x.flatten(),u.flatten()
    v,ψ,θ,φ = x[3],x[4],x[5],x[6];
    cφ,sφ,cθ,sθ,cψ,sψ = cos(φ),sin(φ),cos(θ),sin(θ),cos(ψ),sin(ψ)
    return array([[v*cθ*cψ],
                  [v*cθ*sψ],
                  [-v*sθ],
                  [u[0]],
                  [(sφ/cθ)*v*u[1] + (cφ/cθ)*v*u[2]],
                  [cφ*v*u[1] - sφ*v*u[2]],
                  [-0.1*sφ*cθ + tan(θ)*v*(sφ*u[1]+cφ*u[2])]])

def control(x, w, dw, ddw) :
    p = x[0:3,:]
    x = x.flatten()
    v,ψ,θ,φ = x[3],x[4],x[5],x[6];
    cφ,sφ,cθ,sθ,cψ,sψ = cos(φ),sin(φ),cos(θ),sin(θ),cos(ψ),sin(ψ)
    A1 = array([[cθ*cψ, -v*cθ*sψ, -v*sθ*cψ],
                [cθ*sψ, v*cθ*cψ, -v*sθ*sψ],
                [-sθ,    0,       -v*cθ]])
    #A2 = array([[1,  0,     0],
     #           [0, -sφ/cθ, cφ/cθ],
      #          [0,  cφ,    -sφ]])
    
    A2 = array([[1,  0,       0],
                [0,  v*sφ/cθ, v*cφ/cθ],
                [0,  v*cφ,    -v*sφ]])
    A = A1 @ A2
    dp = v * array([[cθ*cψ],
                    [cθ*sψ],
                    [-sθ]])
    print(w)
    u = inv(A) @ (0.04*(w-p) + 0.4*(dw-dp) + ddw)
    return u


              
x = array([[0,0,0,15,0,0,0]]).T
#x = array([[0,0,1,0.1,0,0,0]]).T
#u = array([[0,0,0.1]]).T
#dt = 0.05
#dt = 0.1
dt = 0.5
R = 20
f1 = 0.01
f2 = 6 * f1
f3 = 3 * f1
for t in arange(0,200,dt):
    w = array([[R*sin(f1*t) + R*sin(f2*t)],
               [R*cos(f1*t) + R*cos(f2*t)],
               [R*sin(f3*t)]])
    dw = R * array([[f1*cos(f1*t) + f2*cos(f2*t)],
                    [-f1*sin(f1*t) - f2*sin(f2*t)],
                    [f3*cos(f3*t)]])
    ddw = R * array([[-f1**2*sin(f1*t) - f2**2*sin(f2*t)],
                     [-f1**2*cos(f1*t) - f2**2*cos(f2*t)],
                     [-f3**2*sin(f3*t)]])
    u = control(x, w, dw, ddw)
    xdot = f(x,u)
    x = x + dt * xdot
    draw(x, w)
    pause(0.001)
