% 创建两个测试运行的结果
run1 = struct('Time', [1, 2, 3, 4], 'Values', [10, 20, 30, 40]);
run2 = struct('Time', [1, 2, 3, 4], 'Values', [15, 25, 35, 45]);

% 创建 ComparisonPlot 对象
plot = matlab.unittest.measurement.chart.ComparisonPlot();

% 向 plot 对象添加第一个测试运行的结果
series1 = plot.addNewSeries();
series1.Name = 'Run 1';
series1.Time = run1.Time;
series1.Data = run1.Values;

% 向 plot 对象添加第二个测试运行的结果
series2 = plot.addNewSeries();
series2.Name = 'Run 2';
series2.Time = run2.Time;
series2.Data = run2.Values;

% 配置 plot 对象并绘制图表
plot.Title = 'Measurement Comparison';
plot.XLabel = 'Time';
plot.YLabel = 'Value';
plot.show();