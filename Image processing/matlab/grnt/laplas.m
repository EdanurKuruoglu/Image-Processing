I1 = im2double(imread('lena.jpg'));
w4=fspecial('laplacian',0);
w8 = [1 1 1; 1 -8 1; 1 1 1];
g=imfilter(I1,w4,'replicate');
figure,imshow(g,[]);