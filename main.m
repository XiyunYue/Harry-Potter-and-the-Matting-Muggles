clc
clear all
close all
%% Input
trimap = imread('image\trimap\Trimap1\GT16.png');
im = imread('image\input_img\GT16.png');
new_background = imread('background1.jpg');
alpha_ground = imread('image\ground_truth\GT16.png');

p = makeParameters;
%% Change form 
alpha_ground = alpha_ground(:, :, 1);
trimap = im2double(trimap);
new_background = im2double(new_background);
alpha_ground = im2double(alpha_ground);
x1 = (im);
x2 = (new_background);
x3 = imresize(new_background, size(im(:, :, 1)));
%% Use Laplacian method
alpha_La = Laplacian_matting(trimap, im);
[F, B, alpha_Ba] = bayes(im, trimap, p);%Also need change this to get Bayesian result 

%% Show alpha
figure (1)
imshow(alpha_La);%change alpha to Bay...
title('Laplacian')
%imwrite(alpha_La, 'image\G01\output_alpha.png');%change alpha to Bay...

%% Show combining result
new_picture = combining(alpha_La, x3, im);%change alpha to Bay...
new_picture2 = combining(alpha_Ba, x3, im) ;
%figure (2)
figure;
imshow(new_picture);
title('Lap_Out')
%imwrite(new_picture, 'image\G01\new_picture.png');
figure;
imshow(new_picture2)
title('Bayes_Output')

figure;
imshow(im);
title('Input');

figure;
imshow(trimap);
title('Trimap');

figure;
imshow(alpha_Ba);
title('Alpha');

%% Show combining result
MSE_La = MSE_calculation(alpha_ground, alpha_La);
MSE_Ba = MSE_calculation(alpha_ground, alpha_Ba);  %change this to get Bayesian result alpha