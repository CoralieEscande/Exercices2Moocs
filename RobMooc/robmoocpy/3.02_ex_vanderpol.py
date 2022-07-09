from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
def f(x,u):
    x,u  = x.flatten(), u.flatten()
    xdot = array([[x[3]*cos(x[4])*cos(x[2])],
                  [x[3]*cos(x[4])*sin(x[2])],
                  [   x[3]*sin(x[4])/3     ],
                  [          u[0]          ],
                  [          u[1]          ]])
    return(xdot)


def draw_field(xmin,xmax,ymin,ymax):
    Mx    = arange(xmin,xmax,2)
    My    = arange(ymin,ymax,2)
    X1,X2 = meshgrid(Mx,My)
    VX    = X2
    VY    = -(0.01*(X1**2)-1)*X2-X1
    VX    = VX/sqrt(VX**2+VY**2)
    VY    = VY/sqrt(VX**2+VY**2)
    quiver(Mx,My,VX,VY)
    return()


x    = array([[0,5,pi/2,30,0.6]]).T
dt   = 0.01
ax=init_figure(-40,40,-40,40)
for t in arange(0,1,dt):
    clear(ax)
    u    = array([[0],[0]])
    x    = x +dt*f(x,u)
    draw_field(-40,40,-40,40)
    draw_car(x)
pause(1)    


