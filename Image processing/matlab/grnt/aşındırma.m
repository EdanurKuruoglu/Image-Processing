I1 = imread('lena.jpg');
se = strel('disk', 5);
I2 = imerode(I1 , se);
imshow(I2);