import cv2

resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 756))
# Görüntüyü 180 derece döndür
ters_cevirilmis = cv2.flip(resim, -1)  # Hem Dikey Hem Yatay Ters Çevirme

# Orijinal ve ters çevrilmiş görüntüyü göster
cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Ters Çevrilmiş Görüntü", ters_cevirilmis)
cv2.waitKey(0)
cv2.destroyAllWindows()
