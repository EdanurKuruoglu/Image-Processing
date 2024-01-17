I1 = im2double(imread('lena.jpg'));
h=fspecial('gaussian',10,2)
I2=imfilter(I1,h,'replicate');
figure,imshow(I2,[]);