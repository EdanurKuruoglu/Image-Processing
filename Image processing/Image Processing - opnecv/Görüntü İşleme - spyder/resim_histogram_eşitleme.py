import cv2
import matplotlib.pyplot as plt

resim = cv2.imread("Galata.jpeg", 0)  # Gri renkte resmi yükle
resim = cv2.resize(resim, (646, 756)) 

# Histogram eşitleme işlemi
resim_esitleme = cv2.equalizeHist(resim)

# Orijinal ve eşitlenmiş görüntüyü göster
cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Histogram Eşitlenmiş Görüntü", resim_esitleme)

# Gri tonlamalı histogramları göster
plt.hist(resim.flatten(), bins=256, range=[0, 256], color='blue', alpha=0.5, label='Orijinal Görüntü')
plt.hist(resim_esitleme.flatten(), bins=256, range=[0, 256], color='red', alpha=0.5, label='Eşitlenmiş Görüntü')
plt.legend(loc='upper right')
plt.title('Histogram Eşitleme')
plt.xlabel('Piksel Değeri')
plt.ylabel('Frekans')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


