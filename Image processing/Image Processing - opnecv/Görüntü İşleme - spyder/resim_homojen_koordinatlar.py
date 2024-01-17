import cv2
import numpy as np

resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 756))
# Orjinal noktanın kartez koordinatları
orijinal_nokta = np.array([100, 100, 1])
# Hareket matrisi oluştur
donusum_matrisi = np.array([[1, 0, 50],
                             [0, 1, 30],
                             [0, 0, 1]])

# Homojen koordinatları oluştur
homojen_nokta = np.append(orijinal_nokta[:2], 1)
# Hareket matrisini homojen koordinatlarla çarp
donusen_nokta_homojen = np.dot(donusum_matrisi, homojen_nokta)
# Homojen koordinatları kartezene çevir
donusen_nokta_kartez = donusen_nokta_homojen[:2]
# Dönüştürülmüş noktayı bir tam sayı konumuna çevir (görüntüde kullanmak için)
donusen_nokta_kartez_int = np.round(donusen_nokta_kartez).astype(int)
# Orjinal noktayı ve dönüştürülmüş noktayı görüntü üzerine çiz
resim_noktalari = resim.copy()
cv2.circle(resim_noktalari, tuple(orijinal_nokta[:2]), 5, (0, 0, 255), -1)
cv2.circle(resim_noktalari, tuple(donusen_nokta_kartez_int), 5, (0, 255, 0), -1)
# Görüntüyü göster
cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Orjinal ve Dönüştürülmüş Noktalar", resim_noktalari)
cv2.waitKey(0)
cv2.destroyAllWindows()
