import cv2
import numpy as np

resim = cv2.imread("Galata.jpeg")
resim= cv2.resize(resim, (646,756))
# Filtre boyutunu belirle (örnek 5x5)
filtre_boyutu = int(input("Filtre boyutunu girin (tek tam sayı): "))
# Ortalama filtreyi oluştur
ortalama_filtre = np.ones((filtre_boyutu, filtre_boyutu), np.float32) / (filtre_boyutu**2)
# Ortalama filtreyi uygula
filtrelenmis_resim = cv2.filter2D(resim, -1, ortalama_filtre)
# Orijinal ve filtrelenmiş görüntüyü göster
cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Filtrelenmiş Görüntü", filtrelenmis_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
