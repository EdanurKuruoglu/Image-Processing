img = imread('lenaa.PNG');
adjusted_img = imadjust(img, [0.3 0.7], [0 1]);
imshow(adjusted_img);
title('Kontrast Artırılmış Görüntü');