% Örnek bir görüntü yükleme
img = imread('lena.jpg'); % Kendi görüntünüzün adını ve uzantısını kullanın

% Gaussian filtresi oluşturma
filter_size = 5; % Filtre boyutu (genellikle tek sayı olmalıdır)
filter_std = 1; % Gaussian filtresinin standart sapması
gaussian_filter = fspecial('gaussian', filter_size, filter_std);

% Görüntüyü netleştirme (konvolüsyon)
blurred_img = imfilter(img, gaussian_filter);

% İlk görüntüyü gösterme
subplot(1, 2, 1);
imshow(img);
title('Orijinal Görüntü');

% Netleştirilmiş görüntüyü gösterme
subplot(1, 2, 2);
imshow(blurred_img);
title('Netleştirilmiş Görüntü');
