function trimap = read_trimap(trimap_filename)
    trimap = imread(trimap_filename);
%     trimap = im2double(trimap);
    size_trimap = size(trimap);
    if length(size_trimap) == 3
        trimap = trimap(:, :, 1);
    end
    trimap_max = max(trimap(:));
    if trimap_max > 1
        trimap = im2double(trimap);
    end



            