function output = combining(alpha, background, im)
    img = double(im);
    c = length(img(1,1,:));
    for i = 1: c
        alpha_fg(:, :, i) = alpha;
        alpha_bg(:, :, i) = 1 - alpha;
    end
%     alpha_fg = alpha;
%     alpha_bg = 1 - alpha;
    for i = 1: c
        output(:, :, i) = alpha_fg(:, :, i) .* img(:, :, i) ./ 255 + ...
            alpha_bg(:, :, i) .* background(:, :, i) ./ 255;
    end

%     for i = 1: c
%         output(:, :, i) = alpha_fg(:, :, i) .* img(:, :, i)./255;
%     end
    
    output = im2uint8(output);
end