from autolib import *

def f(x) :
    return 2*x-floor(2*x)

ax = init_figure(0,1,0,1)
X = arange(0,1,0.01)
Y = f(X)
plot(X,Y,'red')
plot(X,X,'green')
x = 0.2

for k in range (0,10) :
    print(x)
    y=f(x)
    plot([x,x,y], [x,y,y], 'black')
    x = y

pause(10) 
