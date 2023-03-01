%% Input
trimap = imread('image\G01\trimap.png');
im = imread('image\G01\input.png');
new_background = imread('image\G01\background.png');
alpha_ground = imread('image\G01\groundtruth.png');

%% Change form 
alpha_ground = alpha_ground(:, :, 1);
trimap = im2double(trimap);
new_background = double(new_background);
alpha_ground = im2double(alpha_ground);

%% Use Laplacian method
alpha_La = Laplacian_matting(trimap, im);
% alpha_La = Bayesian_function(trimap, im);%Also need change this to get Bayesian result 

%% Show alpha
figure (1)
imshow(alpha_La);%change alpha to Bay...
imwrite(alpha_La, 'image\G01\output_alpha.png');%change alpha to Bay...

%% Show combining result
new_picture = combining(alpha_La, new_background, im);%change alpha to Bay...
figure (2)
imshow(new_picture);
imwrite(new_picture, 'image\G01\new_picture.png');

%% Show combining result
MSE_La = MSE_calculation(alpha_ground, alpha_La);
% MSE_Ba = MSE_calculation(alpha_ground, alpha_Ba);  %change this to get Bayesian result alpha