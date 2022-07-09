function ex_pools
%-------------------------------------------------
    function draw(x,u)
        clf(); hold on; axis([-10,25,-2,12]); axis square;
        plot([0 0],[10 1],'black')
        plot([-7 23],[0 0],'black')
        plot([16 16],[1 10],'black')
        plot([4 4 6 6],[10 1 1 10],'black')
        plot([10 10 12 12],[10 1 1 10],'black')
        fill([0 0 -6 22 16 16 12 12 10 10 6 6 4 4],...
            [x(1) 1 0 0 1 x(3) x(3) 1 1 x(2) x(2) 1 1 x(1)],'blue')
        fill ([ 1 1 1+0.1*u(1) 1+0.1*u(1)],[10 x(1) x(1) 10],'blue')
        fill([ 13 13 13+0.1*u(2) 13+0.1*u(2)],[10 x(3) x(3) 10],'blue')
        drawnow();
    end
%------------   Main   --------------------------
x=[2;3;5];
u=[5,2];
draw(x,u);
end

