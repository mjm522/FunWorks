function VanderPol_plot()

steps = 20;

s1 = linspace(-6,6,steps);
s2 = linspace(-6,6,steps);

% creates two matrices one for all the x-values on the grid, and one for
% all the y-values on the grid.

[x,y] = meshgrid(s1,s2);

u = zeros(size(x));
v = zeros(size(x));

for i=1:numel(x)
    [t,y_sol] = ode23(@vdp1,[0 20],[x(i); y(i)]);
    figure(1);
    plot(y_sol(:,1),y_sol(:,2)); hold on;
    figure(2);
    quiver(y_sol(:,1), y_sol(:,2), gradient(y_sol(:,1)), gradient(y_sol(:,2) ), 'r'); hold on;
end

figure(1);
ylabel('Solution plot');
figure(2);
title('Gradient plot')

end
function dydt = vdp1(t,y, mu)
    %Vandepol oscillator ode
    if nargin < 3
        mu = 1;
    end
    dydt = [y(2); (mu-y(1)^2)*y(2)-y(1)];
end