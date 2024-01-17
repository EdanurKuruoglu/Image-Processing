import cv2
import numpy as np

# Resmi oku
resim = cv2.imread("Galata.jpeg", 0)
resim = cv2.resize(resim, (646, 756))

# Prewitt filtresini tanımla
prewitt_yatay = cv2.getDerivKernels(1, 0, 3, normalize=True)
prewitt_dikey = cv2.getDerivKernels(0, 1, 3, normalize=True)

# Filtreleri uygula
kenarlar_yatay = cv2.filter2D(resim, -1, prewitt_yatay[0] * prewitt_yatay[1].T)
kenarlar_dikey = cv2.filter2D(resim, -1, prewitt_dikey[0] * prewitt_dikey[1].T)

# Sonuçları göster
cv2.imshow("Orijinal Resim", resim)
cv2.imshow("Prewitt Yatay Kenarlar", kenarlar_yatay)
cv2.imshow("Prewitt Dikey Kenarlar", kenarlar_dikey)

cv2.waitKey(0)
cv2.destroyAllWindows()

