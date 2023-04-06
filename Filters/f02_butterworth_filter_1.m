% Second Order Butterworth Filter (Low/High Pass, sin/cos)
% Input: inData = raw data; Q = quality factor
% Output: outData = filtered data
function [outData] = f02_butterworth_filter_1(inData, cutoff_freq, dt, Q, type)
persistent b0 b1 b2 a0 a1 a2 x1 x2 y1 y2 B
if isempty(B)
    fc = cutoff_freq;   % cutoff frequency (Hz) 
    fs = 1/dt;          % sample frequency (Hz)
    omega_c = 2 * pi * fc / fs;
    cos_c = cos(omega_c);
    alpha = sin(omega_c) / (2 * Q);
    
    switch type
        case 'low'
            b0 = (1 - cos_c) / 2;
            b1 = 2*b0;
            b2 = b0;
        case 'high'
            b0 = (1 + cos_c) / 2;
            b1 = -2*b0;
            b2 = b0;
    end
    a0 = 1 + alpha;
    a1 = -2 * cos_c;
    a2 = 1 - alpha;
    
    x1 = 0; x2 = 0;
    y1 = 0; y2 = 0; 
    
    B = 0;      % only for initialization
end

outData = (b0 * inData + b1 * x1 + b2 * x2 - a1 * y1 - a2 * y2) / a0;

x2 = x1;
x1 = inData;
y2 = y1;
y1 = outData;

end