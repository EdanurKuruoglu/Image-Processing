originalImage = imread('lena.jpg');
grayImage = rgb2gray(originalImage);
[gradMagnitude, gradDirection] = imgradient(grayImage, 'Sobel');
sharpEdges = imsharpen(originalImage, 'Amount', 1.5, 'Radius', 1);
figure;
imshow(sharpEdges);
title('Keskinleştirilmiş Kenarlar');