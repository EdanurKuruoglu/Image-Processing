import cv2
import matplotlib.pyplot as plt

resim = cv2.imread("Galata.jpeg", 0)  # Gri renkte resmi yükle
resimm = cv2.resize(resim, (646, 756)) 
# Histogramı hesapla
# 0 gri görüntü, 256 histogram bin sayısı, 0-256 pixel değer arası, none maske
histogram = cv2.calcHist([resim], [0], None, [256], [0, 256])
cv2.imshow("Galata",resimm)

# Histogramı görselleştir
plt.figure()
plt.title("Histogram")
plt.xlabel("Piksel Değeri")
plt.ylabel("Piksel Sayısı")
# ravel fonksiyonu, görüntünün piksel değerlerini birleştirir. Tek boyutlu dizide düzenler.
plt.hist(resim.ravel(), 256, [0, 256], color='gray')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
