I1 = imread('lena.jpg');
I2 = imrotate(I1,35,'bilinear');
figure, imshow(I2)
I3 = imrotate(I1,180,'bicubic');
figure, imshow(I3)