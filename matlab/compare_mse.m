function compare_mse(alpha_La, alpha_Be)
    fprintf('Method1 MSE: %.4f\n', mse1);
    fprintf('Method2 MSE: %.4f\n', mse2);
    if mse1 < mse2
        fprintf('Method1 更优\n');
    elseif mse2 < mse1
        fprintf('Method2 更优\n');
    else
        fprintf('两种方法相同\n');
    end
end