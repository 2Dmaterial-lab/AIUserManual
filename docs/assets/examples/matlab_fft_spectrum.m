%% FFT频谱分析示例
% 用途：对时域信号进行FFT频谱分析
% 使用：修改文件路径和参数后直接运行

clear; clc; close all;

%% 参数设置
filename = 'signal_data.csv';  % CSV文件路径
fs = 10000;                     % 采样率 (Hz)
freq_range = [0, 2000];         % 显示频率范围 (Hz)

%% 读取数据
data = readmatrix(filename);
t = data(:, 1);
signal = data(:, 2);
N = length(signal);

%% 预处理
% 去除直流分量
signal = signal - mean(signal);

% 汉宁窗
window = hanning(N);
signal_windowed = signal .* window;

%% FFT计算
Y = fft(signal_windowed);
P2 = abs(Y / N);          % 双边谱
P1 = P2(1:N/2+1);         % 单边谱
P1(2:end-1) = 2*P1(2:end-1);
f = fs*(0:(N/2))/N;

%% 绘图
figure('Position', [100 100 800 500]);
plot(f, P1, 'LineWidth', 1.5);
xlim(freq_range);
xlabel('Frequency (Hz)');
ylabel('Amplitude');
title('FFT Spectrum');

% 标注峰值
[~, idx] = max(P1);
text(f(idx), P1(idx), sprintf('  Peak: %.1f Hz', f(idx)), ...
    'FontSize', 11, 'Color', 'r');

%% 保存
print('fft_spectrum', '-dpng', '-r300');
fprintf('频谱图已保存为 fft_spectrum.png\n');
