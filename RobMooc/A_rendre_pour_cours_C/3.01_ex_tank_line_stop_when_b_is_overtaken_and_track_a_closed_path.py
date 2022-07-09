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
    #print(X)
    u = control_robot(X, point1, point2)
    #print(u)
    X = X + dt*fct(X,u)
    #print(X)
    return X

def switch_segment(j):
    #print(j)
    aj, bj = zeros([2,size(j)]), zeros([2,size(j)])
    #print(aj, bj)
    for i in arange(0,size(j),1):
        #print(i)
        if j[i] == 1 :
            aj[:,i], bj[:,i] = a.T, b.T
        elif j[i] == 2 :
            aj[:,i], bj[:,i] = b.T, c.T
        elif j[i] == 3 :
            aj[:,i], bj[:,i] = c.T, d.T
        elif j[i] == 4 :
            aj[:,i], bj[:,i] = d.T, a.T    
    return (aj, bj)

ax=init_figure(-40,40,-40,40)
#a,b = array([[-30],[-4]]), array([[30],[6]])
a,b = array([[-30],[-30]]), array([[-20],[20]])
c,d = array([[20],[35]]), array([[35],[-15]])
#closed_path = hstack((a,b,c,d))
#j_max = 4
j = array([[1],[2],[3],[4]])

# état : x, y, theta
X=array([[-20],[-10],[4]])

#u=1
dt= 0.8

m = X[0:2]
aj = a
bj = b

for t in arange(0,250,dt):
    clear(ax)
    draw_tank(X,'darkblue')
    #plot2D(hstack((a,b)),'red')
    #plot2D(a,'ro')
    #plot2D(b,'ro')
    plot2D(hstack((a,b)),'cyan')
    plot2D(hstack((b,c)),'magenta')
    plot2D(hstack((c,d)),'green')
    plot2D(hstack((d,a)),'black')
    plot2D(a,'ro')
    plot2D(b,'ro')
    plot2D(c,'ro')
    plot2D(d,'ro')

    p1, p2 = switch_segment(j)
    #print('segment_switched')
    i = 0
    aj = p1[:,i].reshape(-1,1)
    #print(aj)
    bj = p2[:,i].reshape(-1,1)
    #print(bj)

    if transpose(bj-aj)@(bj-m) >= 0 :
        X = follow_segment(X, aj, bj)
        m = X[0:2]
    else :
        if j[i]<=0 or j[i]>4 :
            print('error with j value')
        elif j[i] == 4 :
            j[i] = 1
        else :
            j[i] = j[i] + 1
        print(j[i])
