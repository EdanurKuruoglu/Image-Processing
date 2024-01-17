resim = imread('lena.jpg');
parlaklik_ayar = 0.2;
kontrast_ayar = 1.5;
kontrast_ayarlanmis = imadjust(resim, [], [], kontrast_ayar);
parlaklik_ayarlanmis = parlaklik_ayar * kontrast_ayarlanmis + (1 - parlaklik_ayar) * mean(resim(:));
imshow(parlaklik_ayarlanmis);