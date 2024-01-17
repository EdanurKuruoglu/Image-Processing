I1 = imread('lena.jpg');
gurultu_yuzdesi = 1; 
gurultulu_resim = I1;
boyut = numel(I1);
gurultu_miktari = round(boyut * gurultu_yuzdesi / 100);
for i = 1:gurultu_miktari
    x = randi(size(resim, 1));
    y = randi(size(resim, 2));
    
    if rand() < 0.5
        gurultulu_resim(x, y, :) = 0;
    else
        gurultulu_resim(x, y, :) = 255;
    end
end

subplot(1, 2, 1);
imshow(I1);
title('Orjinal Resim');
subplot(1, 2, 2);
imshow(gurultulu_resim);
title('Tuz-Biber Gürültülü Resim');