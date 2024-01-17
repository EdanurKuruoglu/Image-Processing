import cv2
import numpy as np

resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 756))

# Kullanıcıdan kontrast ayarını al
kontrast_ayar = float(input("Kontrast ayarını girin (1' den büyükse kontras artar (1.5), 1' den küçükse kontras azalır(0.5)): "))

# Kontrast ayarlamayı uygula
# npclip diziyi belli aralıkta kırpmak için kullanılır.0-255 arasında olmalı çarpmadaki fazla değerleri düzeltmek için.
# np.uint8 bu işaretsiz 8 bit veri tipine dönüştürür. 0-255 arasındaki her değer için uygulanır.
resim_kontrastli = np.clip(resim * kontrast_ayar, 0, 255).astype(np.uint8)

cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Kontrastlı Görüntü", resim_kontrastli)
cv2.waitKey(0)
cv2.destroyAllWindows()
