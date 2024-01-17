% Örnek bir görüntü yükleme
img = imread('plaka.PNG'); % Kendi görüntünüzün adını ve uzantısını kullanın

% Köşeleri otomatik olarak tespit etme (örneğin Harris köşe tespiti)
corners = detectHarrisFeatures(rgb2gray(img));

% Köşe noktalarını alınan sıraya göre düzenleme
corner_points = corners.Location;

% Görüntünün genişliği ve yüksekliği
image_size = [size(img, 1), size(img, 2)];

% Dikdörtgenin boyutu ve düzgünleştirilecek dört köşe koordinatları
output_points = [1, 1; size(img, 2), 1; size(img, 2), size(img, 1); 1, size(img, 1)];

% Geometrik dönüşüm matrisi oluşturma
tform = fitgeotrans(corner_points, output_points, 'projective');

% Perspektif düzeltme işlemi
corrected_img = imwarp(img, tform);

% İlk görüntüyü gösterme
subplot(1, 2, 1);
imshow(img);
title('Orijinal Görüntü');

% Düzeltildikten sonra görüntüyü gösterme
subplot(1, 2, 2);
imshow(corrected_img);
title('Perspektif Düzeltme Sonrası Görüntü');
