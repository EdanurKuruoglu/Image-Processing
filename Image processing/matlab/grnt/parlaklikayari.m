resim = imread('lena.jpg');
artis_miktari = 100;
parlak_resim = resim + artis_miktari;
parlak_resim(parlak_resim > 255) = 255;
imshow(parlak_resim);