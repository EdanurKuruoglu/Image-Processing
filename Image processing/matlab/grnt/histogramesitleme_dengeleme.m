I1 = imread('lena.jpg');
I2 = histeq(I1);
figure, imshow(I2)
figure; imhist(I2)