from autolib import *

def g(x):
    mx,my,θ,v,δ=list(x[0:5,0])
    u=[sin(θ),-cos(θ)]
    m=[mx,my];  d=inf
    for i in range(len(P)-1):
        a,b=P[i],P[i+1]
        α=det([a-m,b-a])/det([u,b-a])
        if (det([a-m,u])*det([b-m,u])<=0 and α>=0): d=min(α,d)
    return array([[d],[v],[δ]])
   
    
def draw_laser(x,d):
    mx,my,θ,v,δ=list(x[0:5,0])
    plot([mx,mx+sin(θ)*d],[my,my-cos(θ)*d],"red")

r0,v0,dt=5,7,0.05
ax=init_figure(-25,55,-30,40)
P=array([[-10,-5],[-10,5],[0,15],[10,20],[20,20],[32,15],[35,10],[30,0],[20,-3],[0,-6],[-10,-5]]) 
x=array([[-15],[0],[pi/2],[7],[0.1]])
draw_polygon(ax,P,"green")
y=g(x)
draw_car(x,"darkblue",0.7,1)
draw_laser(x,y[0,0])
pause(1)