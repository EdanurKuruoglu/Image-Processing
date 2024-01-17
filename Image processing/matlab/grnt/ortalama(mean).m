I1 = im2double(imread('lena.jpg'));
g=fspecial('average',10)
I2=imfilter(I1,g,'replicate');
figure,imshow(I2,[]);