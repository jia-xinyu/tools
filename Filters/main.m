% Test filters
% Author: Jia, Xinyu
% Last modified: 2023/4/6

%% Initialization
clear all;close all;clc
fs = 500;                   % sample frequency
dt = 1/fs;
N  = 1000;               	% number
t = (0:N-1)*dt;
delta_f = 1*fs/N;
f1 = 10;
f2 = 100;
x1 = 0.5*sin(2*pi*f1*t);
x2 = 0.2*sin(2*pi*f2*t);
x3 = 0.2*randn(size(t));	% Gaussian noise
input = x1 + x2 + x3;     	% raw data

cutoff_frequency = 20;      % unit: Hz
true_data = x1;

%% First Order Filter
lpf_d1_data = zeros(N,1);
for i = 1:N
    lpf_d1_data(i) = f01_pass_filter(input(i), cutoff_frequency, dt, 'low');
end

%% Second Order Command Filter
damping = 1/sqrt(2);
Omega_0 = 2*pi*cutoff_frequency;	% unit: rad/s (Undamped natural frequency)
Omega = Omega_0*sqrt(1-damping^2);	% unit: rad/s (Damped natural frequency)
lpf_d2_data = zeros(N,1);
for i = 1:N
    lpf_d2_data(i) = f02_command_filter(input(i), Omega, dt, damping);
end

%% Second Order Butterworth Filter
Q = 1;                              % quality factor
bf_data_1 = zeros(N,1);
bf_data_2 = zeros(N,1);
bf_data_0 = f02_butterworth_filter_0(input, cutoff_frequency, dt);                  % MATLAB
for i = 1:N
	bf_data_1(i) = f02_butterworth_filter_1(input(i), cutoff_frequency, dt, Q, 'low');
	bf_data_2(i) = f02_butterworth_filter_2(input(i), cutoff_frequency, dt, Q);     % [Error]
end

%% 1-Dimension Kalman Filter
kf_data = zeros(N,1);
for i = 1:N
    kf_data(i) = kalman_filter_dim1(input(i));
end

%% Plot
figure(1);

subplot(4,1,1);
plot(t, input, 'Color', '#0072BD', 'LineWidth', 1); hold on
plot(t, true_data, 'Color', '#77AC30', 'LineWidth', 1); hold on
plot(t, lpf_d1_data, 'Color', '#D95319', 'LineWidth', 1); hold off
legend('raw', 'true', 'filtered');
title('First-Order LPF');

subplot(4,1,2);
plot(t, input, 'Color', '#0072BD', 'LineWidth', 1); hold on
plot(t, true_data, 'Color', '#77AC30', 'LineWidth', 1); hold on
plot(t, lpf_d2_data, 'Color', '#D95319', 'LineWidth', 1); hold off
legend('raw', 'true', 'filtered');
title('Second-Order Command Filter');

subplot(4,1,3);
plot(t, input, 'Color', '#0072BD', 'LineWidth', 1); hold on
plot(t, true_data, 'Color', '#77AC30', 'LineWidth', 1); hold on
plot(t, bf_data_0, 'Color', '#000000', 'LineWidth', 1); hold on
plot(t, bf_data_1, 'Color', '#D95319', 'LineWidth', 1); hold on
plot(t, bf_data_2, 'Color', '#EDB120', 'LineWidth', 1); hold off
legend('raw', 'true', 'filtered_0', 'filtered_1', 'filtered_2');
title('Second-Order Butterworth Filter');

subplot(4,1,4);
plot(t, input, 'Color', '#0072BD', 'LineWidth', 1); hold on
plot(t, true_data, 'Color', '#77AC30', 'LineWidth', 1); hold on
plot(t, kf_data, 'Color', '#D95319', 'LineWidth', 1); hold off
legend('raw', 'true', 'filtered');
title('Kalman Filter');
