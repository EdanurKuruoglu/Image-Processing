I1 = imread('lena.jpg');
se = strel('disk',5);
I2 = imopen(I1,se);
figure; 
imshow(I2)