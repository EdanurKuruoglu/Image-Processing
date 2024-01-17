resim = imread('lena.jpg');
aci = 30;
dondurulmus_resim = imrotate(resim, aci, 'bilinear', 'crop');
imshow(dondurulmus_resim);