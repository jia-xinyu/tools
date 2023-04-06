% Second Order Command Filter (State Space Equation, Low Pass)
% Input: nowData = raw data; natural_freq = natural angular frequency (rad/s)
% Output: nowOutData = filtered data
function [nowOutData] = f02_command_filter(nowData, natural_freq, dt, damping)
persistent Omega Dt Damping x1 x2
if isempty(Damping)
    Omega = natural_freq;
    Dt = dt;
    Damping = damping;
    x1 = 0;
    x2 = 0;
end

x2 = x2 + Dt * (-2*Damping*Omega*x2 + Omega^2*(nowData - x1));
x1 = x1 + Dt * x2;

nowOutData = x1;

end