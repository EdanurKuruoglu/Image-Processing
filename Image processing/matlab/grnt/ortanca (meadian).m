I1 = imread('lena.jpg');
I2 = imnoise(I1,'salt & pepper',0.02);
I3 = medfilt2(I2);
imshow(I2)
figure, imshow(I3)