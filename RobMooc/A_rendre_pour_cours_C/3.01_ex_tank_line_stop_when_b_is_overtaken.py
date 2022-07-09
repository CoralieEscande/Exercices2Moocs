from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
from numpy import *

def fct(X,u):
    θ=X[2,0]
    return array([[cos(θ)], [sin(θ)],[u]])

def control_robot(X, point1, point2) :
    phi = arctan2(point2[1,0]-point1[1,0], point2[0,0]-point1[0,0])
    m_r = X[0:2]
    #distance à la ligne : e
    dist_e = det(hstack((point2-point1, m_r-point1))) / norm(point2-point1) 
    thetabar = phi - arctan(dist_e)
    u = arctan(tan((thetabar - X[2,0]) / 2))
    return u

def follow_segment(X, point1, point2) :
    #draw_tank_following_segment(X)
    #print(X)
    u = control_robot(X, point1, point2)
    #print(u)
    X = X + dt*fct(X,u)
    #print(X)
    return X

X=array([[-20],[-10],[4]])
u=1
dt= 0.4
a,b = array([[-30],[-4]]), array([[30],[6]])
ax=init_figure(-40,40,-40,40)

m = X[0:2]
aj = a
bj = b

for t in arange(0,100,dt):
    clear(ax)
    draw_tank(X,'darkblue')
    plot2D(hstack((a,b)),'red')
    plot2D(a,'ro')
    plot2D(b,'ro')  

    if transpose(bj-aj)@(bj-m) >= 0 :
        X = follow_segment(X, aj, bj)
        m = X[0:2]
