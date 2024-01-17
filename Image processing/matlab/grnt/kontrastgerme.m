I1 = imread('lena.jpg');
m=150; E=10;
g=1./(1+(m./double(I1)+eps).^E);
figure,imshow(g);