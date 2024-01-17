import cv2

resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 756))
# Resmin boyutlarını al
satir, sutun = resim.shape[:2]
# Kullanıcıdan döndürme açısını al
aci = float(input("Döndürme açısını girin (derece cinsinden): "))
# Döndürme matrisini oluştur
dondurme_matrisi = cv2.getRotationMatrix2D((sutun / 2, satir / 2), aci, 1)
# Açılı döndürmeyi uygula
dondurulmus_resim = cv2.warpAffine(resim, dondurme_matrisi, (sutun, satir), flags=cv2.INTER_LINEAR)
cv2.imshow("Orijinal Resim", resim)
cv2.imshow("Döndürülmüş Resim", dondurulmus_resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
