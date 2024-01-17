originalImage = imread('lena.jpg');
imshow(originalImage);
title('Orijinal Resim');
[rows, columns, ~] = size(originalImage);
scalingFactor = 2;
newRows = rows * scalingFactor;
newColumns = columns * scalingFactor;
enlargedImage = zeros(newRows, newColumns, 3, 'uint8');
kernel = [0.25, 0.5, 0.25;
          0.5, 1, 0.5;
          0.25, 0.5, 0.25];
for i = 1:3
    enlargedImage(:, :, i) = uint8(conv2(double(originalImage(:, :, i)), kernel, 'same'));
end
figure;
imshow(enlargedImage);
title('Büyütülmüş Resim');