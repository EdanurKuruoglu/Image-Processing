I1=imread('lena.jpg');
h=[0 1 0;1 1 1;0 1 0];
I2=imdilate(I1,h);
imshow(I2)