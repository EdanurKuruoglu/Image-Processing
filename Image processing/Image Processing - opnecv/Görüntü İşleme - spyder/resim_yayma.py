import cv2
import numpy as np

resim = cv2.imread("Galata.jpeg", 0)  # Gri tonlamalı olarak yükle
resim = cv2.resize(resim, (646, 756))

# Kullanıcıdan çekirdek boyutunu ve tekrar sayısını al
cekirdek_boyutu = int(input("Çekirdek boyutunu girin (örneğin, 3): "))
tekrar_sayisi = int(input("Tekrar sayısını girin: "))
# Yayma işlemi için çekirdek oluştur
cekirdek = np.ones((cekirdek_boyutu, cekirdek_boyutu), np.uint8)
# Yayma işlemi uygula
genisletilmis_resim = cv2.dilate(resim, cekirdek, iterations=tekrar_sayisi)

# Orijinal ve genişletilmiş görüntüyü göster
cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Genişletilmiş Görüntü", genisletilmis_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
