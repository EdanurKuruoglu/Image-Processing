import cv2
import numpy as np

resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 756))

# Kullanıcıdan yatay ve dikey öteleme miktarını al
yatay_oteleme = int(input("Yatay öteleme miktarını girin: "))
dikey_oteleme = int(input("Dikey öteleme miktarını girin: "))
# Öteleme matrisini oluştur
oteleme_matrisi = np.float32([[1, 0, yatay_oteleme], [0, 1, dikey_oteleme]])
# Öteleme işlemini uygula
oteleme_resim = cv2.warpAffine(resim, oteleme_matrisi, (resim.shape[1], resim.shape[0]))

# Orijinal ve öteltilmiş görüntüyü göster
cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Öteltilmiş Görüntü", oteleme_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
