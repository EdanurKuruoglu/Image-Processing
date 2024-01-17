import cv2

resim = cv2.imread("Galata.jpeg", 0)  # Gri tonlama ile yükle
resim = cv2.resize(resim, (646, 756)) 
esikleme_degeri = float(input("Eşikleme yapmak için 0-255 arasında bir değer girin: "))
# Görüntüyü eşikle
eşiklenmiş_resim = cv2.threshold(resim, esikleme_degeri, 255, cv2.THRESH_BINARY)[1]

cv2.imshow("orijinal görüntü", resim)
cv2.imshow("Eşiklenmiş Görüntü", eşiklenmiş_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()

