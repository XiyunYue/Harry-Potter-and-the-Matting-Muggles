
function alpha = Laplacian_matting(trimap, im)
    img = im2double(im);
    [x, y, c] = size(img);
    fg = trimap > 0.9;
    bg = trimap < 0.01;
    unk = ~(fg | bg);
    [X, Y]=find(unk);
    Laplacian = del2(img);
    alpha = zeros(x, y);
    alpha(bg(:, :, 1)) = 0;
    alpha(fg(:, :, 1)) = 1;
    for k = 1: length(Y)
        for i = 1: c
            alpha(X(k), Y(k)) = alpha(X(k), Y(k)) + Laplacian(X(k), Y(k), i) .^ 2;
        end
    end
    alpha = (1 - sqrt(alpha ./ c));
    alpha(bg(:, :, 1)) = 0;
    alpha(fg(:, :, 1)) = 1;    
end