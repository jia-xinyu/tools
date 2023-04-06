% First Order Low/High Pass filter (LPF/HPF)
% Input: inputData = raw data; cutoff_freq = cut off frequency (Hz)
% Output: outData = filtered data
function [outData] = f01_pass_filter(inData, cutoff_freq, dt, type)
persistent cutoffFreq T inData_old outData_old A
if isempty(A)
    cutoffFreq = cutoff_freq;
    T = dt;
    inData_old = 0;
    outData_old = 0;
    
    A = 0;      % only for initialization
end

RC = 1/(2*pi*cutoffFreq);
switch type
    case 'low'
        a = min(max(T/(T+RC), 0), 1);       % filter coefficient
        outData = a * inData  + (1-a) * outData_old;
    case 'high'
        a = min(max(RC/(T+RC), 0), 1);      % filter coefficient
        outData = a * (inData - inData_old + outData_old);
end

inData_old = inData;
outData_old = outData;

end