import cv2
import numpy as np

resim = cv2.imread("Galata.jpeg", cv2.IMREAD_GRAYSCALE)
resim = cv2.resize(resim, (646, 756))

# Kenar algılama için kernel (korelasyon filtresi)
kernel = np.array([[1, 1, 1],
                   [1, -7, 1],
                   [1, 1, 1]])

# Görüntüyü korelasyon filtresi ile işle
korelasyon_cikti = cv2.filter2D(resim, -1, kernel)

cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Korelasyon Çıktısı", korelasyon_cikti)
cv2.waitKey(0)
cv2.destroyAllWindows()
