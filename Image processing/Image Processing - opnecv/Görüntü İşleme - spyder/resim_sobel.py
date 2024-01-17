import cv2
import numpy as np

# Görüntüyü yükle
resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 756))

# Görüntüyü gri tonlamaya çevir
resim_gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
# Yatay (x ekseni) Sobel filtresi uygula
sobel_x = cv2.Sobel(resim_gri, cv2.CV_64F, 1, 0, ksize=3)
# Dikey (y ekseni) Sobel filtresi uygula
sobel_y = cv2.Sobel(resim_gri, cv2.CV_64F, 0, 1, ksize=3)
# Kenarları görselleştir
kenarlar_x = cv2.normalize(cv2.magnitude(sobel_x, np.zeros_like(sobel_x)), None, 0, 255, cv2.NORM_MINMAX)
kenarlar_y = cv2.normalize(cv2.magnitude(np.zeros_like(sobel_y), sobel_y), None, 0, 255, cv2.NORM_MINMAX)
# Yatay ve dikey kenarları birleştir
kenarlar = cv2.addWeighted(kenarlar_x, 0.5, kenarlar_y, 0.5, 0)

# Görüntü, yatay ve dikey kenarları göster
cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Yatay Kenarlar (Sobel)", kenarlar_x.astype(np.uint8))
cv2.imshow("Dikey Kenarlar (Sobel)", kenarlar_y.astype(np.uint8))
cv2.imshow("Toplam Kenarlar (Sobel)", kenarlar.astype(np.uint8))

cv2.waitKey(0)
cv2.destroyAllWindows()
