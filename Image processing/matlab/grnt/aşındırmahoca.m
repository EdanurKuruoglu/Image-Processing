I1=imread('lena.jpg');
h=ones(5,5);
I2=imerode(I1,h);
figure; 
imshow(I2)