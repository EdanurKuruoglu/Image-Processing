import cv2
import numpy as np

resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 756))

alinan_deger = float(input("Negatif bir değer girin karanlık yapmak için, pozitif bir değer girin (aydınlık yapmak için): "))

# Giriş değerine bağlı olarak görüntüyü aydınlat veya karart
resim_aydinlik_karanlik = np.uint8(np.clip(resim + alinan_deger, 0, 255))

cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Aydınlık/Karanlık Görüntü", resim_aydinlik_karanlik)
cv2.waitKey(0)
cv2.destroyAllWindows()





