% 1-Dimensional Kalman Filter
% Input: inData = raw data
% Output: outData = filtered data
function [outData] = kalman_filter_dim1(inData)
persistent x a b h p q r g
if isempty(x)
    x = 0;      % state, x(k) = a * x(k-1) + b * u(k)
    a = 1;      % state transfer matrix
    b = 0;      % control matrix
    h = 1;      % observer matrix
    p = 0;      % estimate cov
    q = 0.002;  % process cov
    r = 0.05;   % observer cov
    g = 0;      % kalman gain
end

x = a * x + b * inData;
p = a * p * a + q;

g = p * h / (h * p * h + r);
x = x + g * (inData - h * x);
p = (1 - g * h) * p;

outData = x;

end