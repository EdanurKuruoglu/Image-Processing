orijinalGoruntu = imread('lena.jpg');
x_oteleme_miktari = 30;
y_oteleme_miktari = 20;
otelemeGoruntu = imtranslate(orijinalGoruntu, [x_oteleme_miktari, y_oteleme_miktari]);
imshow(otelemeGoruntu)