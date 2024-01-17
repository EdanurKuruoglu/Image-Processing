import cv2
import numpy as np

# Görüntüyü yükle
resim = cv2.imread("Galata.jpeg", 0)  # Gri tonlamalı olarak yükle
resim = cv2.resize(resim, (646, 756))

# Kullanıcıdan çekirdek boyutunu ve tekrar sayısını al
cekirdek_boyutu = int(input("Çekirdek boyutunu girin (örneğin, 3): "))
tekrar_sayisi = int(input("Tekrar sayısını girin: "))

# Kapama işlemi için çekirdek oluştur
cekirdek = np.ones((cekirdek_boyutu, cekirdek_boyutu), np.uint8)

# Kapama işlemi uygula
kapama_resim = cv2.morphologyEx(resim,
                cv2.MORPH_CLOSE, cekirdek, iterations=tekrar_sayisi)

cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Kapama İşlemi Uygulanmış Görüntü", kapama_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
