from autolib import *
fig = figure()
ax = Axes3D(fig)     
x = array([[0],[0],[0],[0],[0],[0],[0],[0]])
θ,ds,dθ,posx,posy,ψ,s1,s2 = list(x[0:8,0])
clean3D(ax,-2,20,-2,20,-1,8)
draw_segway3D(ax,posx,posy,θ,ψ,s1,s2) 
    
pause(1)    