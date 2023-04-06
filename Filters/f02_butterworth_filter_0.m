% Second Order Butterworth Filter (MATLAB)
% Input: inData = raw data;
% Output: outData = filtered data
function [outData] = f02_butterworth_filter_0(inData, cutoff_freq, dt)
persistent b a
if isempty(a) && isempty(b)
    fc = cutoff_freq;   % cutoff frequency (Hz) 
    fs = 1/dt;          % sample frequency (Hz)
    
    order = 2;          % order
    [b, a] = butter(order, fc/(fs/2), 'low');
end

outData = filter(b, a, inData);

end