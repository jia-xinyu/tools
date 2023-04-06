% Second Order Butterworth Filter (Low Pass)
% Input: nowData = raw data
% Output: nowOutData = filtered data
function [outData] = f02_butterworth_filter_2(inData, cutoff_freq, dt, Q)
persistent b0 b1 b2 a1 a2 x1 x2 y1 y2 C
if isempty(C)
    fc = cutoff_freq;   % cutoff frequency (Hz) 
    fs = 1/dt;          % sample frequency (Hz)
    omega_c = 2 * pi * fc / fs;     % Normalized cutoff frequency
    alpha = sin(omega_c) / (2 * Q);
    
    b0 = 1/(1 + 2*alpha + 4*alpha^2);
    b1 = 2*b0;
    b2 = b0;
    a1 = 2*(1 - 2*alpha^2)*b0;
    a2 = (1 - 2*alpha + 4*alpha^2)*b0;     % [TO DO] if has "-"
    
    x1 = 0; x2 = 0;
    y1 = 0; y2 = 0; 
    
    C = 0;      % only for initialization;
end

outData = b0 * inData + b1 * x1 + b2 * x2 - a1 * y1 - a2 * y2;

x2 = x1;
x1 = inData;
y2 = y1;
y1 = outData;

end