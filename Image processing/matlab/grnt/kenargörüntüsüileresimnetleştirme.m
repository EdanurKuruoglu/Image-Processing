original_image = imread('lena.jpg');
edge_image = edge(rgb2gray(original_image), 'Canny');
blurred_image = imgaussfilt(original_image, 2);
imshow(blurred_image);
title('Netleştirilmiş Resim');