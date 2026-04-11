%% Publication级别绘图模板
% 用途：生成符合论文发表标准的MATLAB图表
% 使用：修改数据和标签后直接运行

clear; clc; close all;

%% 绘图参数（根据期刊要求修改）
fig_width = 8;     % 图片宽度 (cm)
fig_height = 6;    % 图片高度 (cm)
font_name = 'Helvetica';
font_size = 12;
line_width = 1.5;
axis_width = 1.2;
output_format = '-depsc';  % -depsc(EPS) / -dpng(PNG) / -dpdf(PDF)
output_name = 'publication_figure';

%% 读取数据（替换为你的数据文件）
d1 = readmatrix('data1.csv');
d2 = readmatrix('data2.csv');
d3 = readmatrix('data3.csv');

%% 创建图窗
figure('Units', 'centimeters', 'Position', [2 2 fig_width fig_height]);

%% 绘制数据
h1 = plot(d1(:,1), d1(:,2), 'k-', 'LineWidth', line_width); hold on;
h2 = plot(d2(:,1), d2(:,2), 'r--', 'LineWidth', line_width);
h3 = plot(d3(:,1), d3(:,2), 'b-.', 'LineWidth', line_width);

%% 格式设置
set(gca, 'FontSize', font_size, 'FontName', font_name, ...
    'LineWidth', axis_width, 'Box', 'on');

xlabel('Wavelength (nm)');
ylabel('Transmittance (%)');

%% 图例
legend([h1 h2 h3], {'Sample A', 'Sample B', 'Sample C'}, ...
    'Location', 'northeast', 'FontSize', 10);

%% 轴范围（根据数据调整）
xlim([400 800]);
ylim([0 100]);

%% 导出
print(output_name, output_format, '-r300');
fprintf('图片已保存为 %s\n', output_name);
