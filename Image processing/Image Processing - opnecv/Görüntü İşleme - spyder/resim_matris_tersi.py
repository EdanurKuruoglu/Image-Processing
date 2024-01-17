import cv2
import numpy as np

resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 646))
# Kırmızı renk kanalını seç
red_channel = resim[:, :, 2]
# Kırmızı renk kanalının matrisini al
matris = np.array(red_channel)
# Matrisin tersini al
ters_matris = np.linalg.inv(matris)

# Ters matrisi ekrana yazdır
print("Orijinal Matris:")
print(matris)
print("\nTers Matris:")
print(ters_matris)

