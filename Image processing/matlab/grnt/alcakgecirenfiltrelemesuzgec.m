I1 = im2double(imread('lena.jpg')); 
w1=ones(2);
I2 = imfilter(I1,w1,'replicate');
figure, imshow(I2,[]); 