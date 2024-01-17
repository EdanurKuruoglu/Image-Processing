import cv2

resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim,(646,756))

genislik = int(input("Genişlik değerini girin:(0-99 arası tek sayı giriniz) "))
standart_sapma = int(input("Standart sapma değerini girin:(0-99 arası bir değer giriniz) "))

filtrelenmis_resim = cv2.GaussianBlur(resim, (genislik, genislik), standart_sapma)

cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Filtrelenmiş Görüntü", filtrelenmis_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()

