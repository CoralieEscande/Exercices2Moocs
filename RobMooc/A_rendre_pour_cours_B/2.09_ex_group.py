from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
from numpy import *


def f(x,u):
    x,u=x.flatten(),u.flatten()
    # state : x = (x, y, theta, v)
    xdot = array([[x[3]*cos(x[2])],[x[3]*sin(x[2])],[u[0]],[u[1]]])
    return(xdot)

def control(x,w,dw,ddw):
    #u=array([[0],[0]]) #TO DO
    x = x.flatten()
    p = array([[x[0]], [x[1]]]) #position : (x,y)
    v = array([[x[3]*cos(x[2])], [x[3]*sin(x[2])]]) #vitesse : (xdot,ydot)
    A = array([[-x[3]*sin(x[2]), cos(x[2])],
               [ x[3]*cos(x[2]), sin(x[2])]])
    commande_PD = w - p + 2*(dw - v) + ddw
    u = inv(A)@commande_PD
    return u    
    

ax=init_figure(-50,50,-50,50)
#ax=init_figure(-2,2,-2,2)
m   = 20
X   = 10*randn(4,m)
a,dt = 0.1,0.5

for t in arange(0,50,dt):
    clear(ax)
    for i in range(m):        
        #w = zeros((2,1)) #TO DO
        #dw = zeros((2,1))  #TO DO
        #ddw = zeros((2,1))#TO DO
        
        delta = (2*i*pi)/m
        theta = a*t
        
        c = array([[cos(theta +delta)],
                   [sin(theta +delta)]])
        dc = a * array([[-sin(theta +delta)],
                        [ cos(theta +delta)]])
        ddc = -a**2 * c

        R = array([[cos(theta), -sin(theta)],
                   [sin(theta),  cos(theta)]])
        dR = a * array([[-sin(theta), -cos(theta)],
                        [ cos(theta), -sin(theta)]])
        ddR = -a**2 * R

        D = array([[20+15*sin(theta), 0],
                   [0,               20]])
        dD = array([[15*a*cos(theta), 0],
                    [0,               0]])
        ddD = array([[-15*a**2*sin(theta), 0],
                     [0,                   0]])

        w = R@D@c
        dw = R@D@dc + R@dD@c + dR@D@c
        ddw = R@D@ddc + R@ddD@c + ddR@D@c + 2 *(dR@D@dc + R@dD@dc + dR@dD@c)
        
        x=X[:,i].reshape(4,1)
        #u = control(x,c,dc,ddc)
        u = control(x,w,dw,ddw)
        x=X[:,i].reshape(4,1)
        #draw_tank(x,'b',0.05,1)
        draw_tank(x,'b',1,1)
        x=x+f(x,u)*dt        
        X[:,i]  = x.flatten()
        #plot([c[0][0]],[c[1][0]],'r+')
        plot([w[0][0]],[w[1][0]],'r+')


