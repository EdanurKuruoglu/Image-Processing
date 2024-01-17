import cv2

# Görüntüyü yükle
resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 756))

# Görüntüyü düşey eksende aynala
aynalanan_resim = cv2.flip(resim, 1)  # Düşey Aynalama

cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Aynalanmış Görüntü", aynalanan_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
