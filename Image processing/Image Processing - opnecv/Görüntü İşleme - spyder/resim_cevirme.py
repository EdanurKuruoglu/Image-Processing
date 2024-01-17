import cv2

resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 756))
# Görüntü boyutlarını al
satir, sutun = resim.shape[:2]
aci = float(input("Döndürme açısını girin (saat yönünde pozitif, saat yönünün tersi negatif): "))
# Döndürme matrisini oluştur
dondurme_matrisi = cv2.getRotationMatrix2D((sutun / 2, satir / 2), aci, 1)
# Çevirme işlemini uygula
cevirilmis_resim = cv2.warpAffine(resim, dondurme_matrisi, (sutun, satir), flags=cv2.INTER_LINEAR)
cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Çevrilmiş Görüntü", cevirilmis_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
