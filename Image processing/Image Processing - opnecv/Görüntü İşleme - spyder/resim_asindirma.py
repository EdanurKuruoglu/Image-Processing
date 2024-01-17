import cv2
import numpy as np

resim = cv2.imread("Galata.jpeg", 0)  # Gri tonlamalı olarak yükle
resim = cv2.resize(resim, (646, 756))

cekirdek_boyutu = int(input("Çekirdek boyutunu girin (örneğin, 3): "))
tekrar_sayisi = int(input("Tekrar sayısını girin: "))
# Aşındırma işlemi için çekirdek oluştur
cekirdek = np.ones((cekirdek_boyutu, cekirdek_boyutu), np.uint8)
# Aşındırma işlemi uygula
kucultulmus_resim = cv2.erode(resim, cekirdek, iterations=tekrar_sayisi)

cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Küçültülmüş Görüntü", kucultulmus_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
