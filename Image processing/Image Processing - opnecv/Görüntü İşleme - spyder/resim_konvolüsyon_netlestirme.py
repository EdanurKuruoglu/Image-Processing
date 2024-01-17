import cv2
import numpy as np

# Görüntüyü yükle
resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 756))

# Yaygın olarak kullanılan çekirdek matrisi
kernel_matrix = np.array([[0, -1, 0],
                          [-1, 5, -1],
                          [0, -1, 0]])

# Netleştirme işlemi
netlesmis_resim = cv2.filter2D(resim, -1, kernel_matrix)

# Orijinal ve netleştirilmiş görüntüyü göster
cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Netleştirilmiş Görüntü", netlesmis_resim)

cv2.waitKey(0)
cv2.destroyAllWindows()


