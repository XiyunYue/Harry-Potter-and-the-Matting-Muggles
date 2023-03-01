function MSE = MSE_calculation(alpha_ground, result)
    x_max = length(result(:, 1));
    y_max = length(result(1, :));
    n = x_max * y_max;
    sum_MSE = 0;
    for x = 1 : x_max
        for y = 1 : y_max
            sum_MSE = sum_MSE + (result(x, y) - alpha_ground(x, y)) ^ 2;
        end
    end
    MSE = sum_MSE / n;
            


