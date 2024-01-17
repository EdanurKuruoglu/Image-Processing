I1 = imread('lena.jpg');
level = graythresh(I1);
bw = im2bw(I1,level);
figure, imshow(bw)