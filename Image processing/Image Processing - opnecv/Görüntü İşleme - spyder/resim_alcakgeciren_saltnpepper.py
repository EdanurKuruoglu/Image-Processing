import cv2
import numpy as np

resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 756))

dusuk_deger = int(input("Siyah noktaların piksel değerini girin (0-255): "))
yuksek_deger = int(input("Beyaz noktaların piksel değerini girin (0-255): "))
gurultu_orani = float(input("Gürültü oranını girin (0-1 arasında): "))

resim_kopya = resim.copy()

# Gürültüyü ekle
gurultu = np.random.rand(resim_kopya.shape[0], resim_kopya.shape[1])
gurultulu_pikseller = gurultu < gurultu_orani
resim_kopya[gurultulu_pikseller] = dusuk_deger  # Siyah noktaları ekle
gurultulu_pikseller = gurultu > 1 - gurultu_orani
resim_kopya[gurultulu_pikseller] = yuksek_deger  # Beyaz noktaları ekle
# Medyan filtresini uygula
filtre_boyutu = int(input("Medyan filtre boyutunu girin (tek sayı): "))
resim_filtrelenmis = cv2.medianBlur(resim_kopya, filtre_boyutu)

cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Gürültülü Görüntü", resim_kopya)
cv2.imshow("Filtrelenmiş Görüntü", resim_filtrelenmis)

cv2.waitKey(0)
cv2.destroyAllWindows()


