I1 = imread('lena.jpg');
se = strel('disk',10);
I2 = imclose(I1,se);
figure; imshow(I2)