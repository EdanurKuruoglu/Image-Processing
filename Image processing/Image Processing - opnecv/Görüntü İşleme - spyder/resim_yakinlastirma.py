import cv2

resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 756))

# Kullanıcıdan ölçek faktörünü al
olcek_faktoru = float(input("Ölçek faktörünü girin (örneğin,1' den büyük değer girin= 2.0): "))
# Görüntüyü yakınlaştırma
yakinlastirilmis_resim = cv2.resize(resim,
        None, fx=olcek_faktoru, fy=olcek_faktoru, interpolation=cv2.INTER_LINEAR)

# Orijinal ve yakınlaştırılmış görüntüyü göster
cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Yakınlaştırılmış Görüntü", yakinlastirilmis_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
