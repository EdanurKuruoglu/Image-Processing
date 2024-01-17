import cv2
import numpy as np

# Görüntüyü yükle
resim = cv2.imread("Galata.jpeg")
gorsel = cv2.resize(resim, (646, 756))

# Orijinal plaka köşe noktaları
orijinal_noktalar = np.float32([[0, 0], [gorsel.shape[1], 0], [0, gorsel.shape[0]], [gorsel.shape[1], gorsel.shape[0]]])
# Yeni plaka köşe noktaları
yeni_noktalar = np.float32([[0, 0], [gorsel.shape[1], 0], [0, gorsel.shape[0]], [gorsel.shape[1], gorsel.shape[0]]])
# Perspektif matrisi oluştur
perspektif_matrisi = cv2.getPerspectiveTransform(orijinal_noktalar, yeni_noktalar)
# Perspektif dönüştürme uygula
sonuc_gorsel = cv2.warpPerspective(gorsel, perspektif_matrisi, (gorsel.shape[1], gorsel.shape[0]))

# Görüntüleri göster
cv2.imshow("Orijinal Görüntü", gorsel)
cv2.imshow("Perspektif Düzeltme", sonuc_gorsel)
cv2.waitKey(0)
cv2.destroyAllWindows()
