from autolib import *


def draw_snake(x,u):
   mx,my,θ,v,δ=list(x[0:5,0])
   u1,u2=list(u[0:2,0])
   M0=array([[ 0  ,-0.3, 0.3, 0  ,0  ,-0.3,0.3,0  ,0,1], 
             [-0.4,-0.4,-0.4,-0.4,0.4, 0.4,0.4,0.4,0,0]])  
   M0=add1(M0)          
   W=array([[-0.4,0.4],[0,0],[1,1]])
   R1=tran2H(mx,my)@rot2H(θ)
   M1=R1@M0
   β=arctan(u1)
   skate=R1@tran2H(1,0)@rot2H(β)@W
   M2=R1@rot2H(δ)@tran2H(-1,0)@M0
   plot2D(M1,'blue')
   plot2D(skate,'magenta')
   plot2D(M2,'black')

          
s=5
ax = init_figure(-s,s,-s,s)
x=array([[0],[0],[2],[1],[0]]) #x,y,θ,v,δ
u=array([[1],[0]])
draw_snake(x,u) 


pause(1)    

  
  
  