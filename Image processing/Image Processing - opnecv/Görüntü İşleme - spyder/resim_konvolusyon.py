import cv2
import numpy as np

resim = cv2.imread("Galata.jpeg", cv2.IMREAD_GRAYSCALE) # gri
resim = cv2.resize(resim, (646, 756))

# Konvolüsyon kernel'ini oluştur (örneğin, bir kenar bulma kernel'i)
kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

# Görüntüyü konvolüsyon kernel'i ile işle
konvolusyon_cikti = cv2.filter2D(resim, -1, kernel)

# Görüntüleri göster
cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Konvolüsyon Çıktısı", konvolusyon_cikti)
cv2.waitKey(0)
cv2.destroyAllWindows()
