import cv2
import matplotlib.pyplot as plt

resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 756))

# Kullanıcıdan kontrast genişletme ayarlarını al
alt_limit = int(input("Kontrast için alt limiti girin (0-255): "))
ust_limit = int(input("Kontrast için üst limiti girin (0-255): "))

# Görüntüyü gri tonlamaya çevir
resim_gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
# Histogramı eşitleme işlemi
resim_esitleme = cv2.equalizeHist(resim_gray)
# Kontrast genişletme işlemi
kontrast_genisletme = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
resim_genisletilmis = kontrast_genisletme.apply(resim_gray)

# Orijinal, eşitlenmiş ve genişletilmiş görüntüyü göster
cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Kontrast Genişletilmiş Görüntü",  resim_genisletilmis)
cv2.imshow("Histogram Eşitlenmiş Görüntü",resim_esitleme)
# Gri tonlamalı histogramı göster
# alpha=0.5: Histogramın saydamlığını belirtir (0 ile 1 arasında bir değer).
#density=True: Histogramın normalleştirilmiş olup olmadığını belirtir.True ise alanlar 1 olur normalleştirme vardır.
plt.hist(resim_genisletilmis.flatten(), bins=256, range=[0, 256], color='gray', alpha=0.5, density=True)
plt.title('Kontrast Genişletilmiş Görüntü Gri Histogramı')
plt.xlabel('Piksel Değeri')
plt.ylabel('Frekans')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()



