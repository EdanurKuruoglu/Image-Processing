import cv2
import numpy as np

# Görüntüyü yükle
resim = cv2.imread("Galata.jpeg", 0)  # Gri tonlama ile yükle
resim = cv2.resize(resim, (646, 756))

# Medyan filtresi uygulanacak pencere boyutu
pencere_boyutu = 5

# Medyan filtresini uygula
medyan_filtre = cv2.medianBlur(resim, pencere_boyutu)

# Görüntüleri göster
cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Medyan Filtresi Uygulanmış Görüntü", medyan_filtre)
cv2.waitKey(0)
cv2.destroyAllWindows()
