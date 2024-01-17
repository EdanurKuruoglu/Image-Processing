img = imread('lena.jpg');
enlarged_img = imresize(img, 2);
subplot(1, 2, 1);
imshow(img);
title('Orijinal Görüntü');
subplot(1, 2, 2);
imshow(enlarged_img);
title('Yakınlaştırılmış Görüntü');
