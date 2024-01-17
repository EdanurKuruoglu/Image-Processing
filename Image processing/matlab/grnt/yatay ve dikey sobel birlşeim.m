img = imread('lena.jpg');
sobel_horizontal = [-1 -2 -1; 0 0 0; 1 2 1];
sobel_vertical = [-1 0 1; -2 0 2; -1 0 1];
if size(img, 3) == 3
    img = rgb2gray(img);
end

horizontal_edges = conv2(double(img), sobel_horizontal, 'same');
vertical_edges = conv2(double(img), sobel_vertical, 'same');
combined_edges = sqrt(horizontal_edges.^2 + vertical_edges.^2);
imshow(uint8(combined_edges));
title('Birleştirilmiş Kenarlar');