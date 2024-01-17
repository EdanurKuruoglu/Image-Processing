img = imread('lena.jpg');
prewitt_horizontal = [-1 -1 -1; 0 0 0; 1 1 1];
prewitt_vertical = [-1 0 1; -1 0 1; -1 0 1];
if size(img, 3) == 3
    img = rgb2gray(img);
end

horizontal_edges = conv2(double(img), prewitt_horizontal, 'same');
vertical_edges = conv2(double(img), prewitt_vertical, 'same');
combined_edges = sqrt(horizontal_edges.^2 + vertical_edges.^2);
subplot(1, 2, 1);
imshow(img);
title('Orijinal Görüntü');
subplot(1, 2, 2);
imshow(uint8(combined_edges));
title('Birleştirilmiş Kenarlar');
