import cv2
import numpy as np

# Resmi oku
resim = cv2.imread("Galata.jpeg",0)
resim = cv2.resize(resim, (646, 756))

# Sobel operatörü ile gradyan hesapla
grad_x = cv2.Sobel(resim, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(resim, cv2.CV_64F, 0, 1, ksize=3)
# Elde edilen gradyanları birleştir
grad_mag = np.sqrt(grad_x**2 + grad_y**2)
# Gradyanları normalize et
grad_mag = cv2.normalize(grad_mag, None, 0, 255, cv2.NORM_MINMAX)
# Orijinal görüntüyü görüntüle
cv2.imshow("Orijinal Görüntü", resim)
# Gradyan görüntüsünü görüntüle
cv2.imshow("Gradyan Görüntüsü", grad_mag.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
