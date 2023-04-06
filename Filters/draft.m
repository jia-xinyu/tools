clc
clear
fc = 100;
fs = 500;
omega_c = 2 * pi * fc / fs;
cos_c = cos(omega_c);
Q = 1/sqrt(2);
alpha = sin(omega_c) / (2 * Q);

a0 = 1 + alpha
% b0 = (1 - cos_c) / 2 / a0;

b0 = 1 / (1 + 2*alpha + 4*alpha^2)