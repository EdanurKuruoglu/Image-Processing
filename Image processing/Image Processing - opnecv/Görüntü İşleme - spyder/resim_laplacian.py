import cv2

resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 756))

# Kullanıcıdan Laplacian filtresi ayarlarını al
laplacian_kenar_boyu = int(input("Laplacian filtresi çekirdek boyutunu girin (örneğin, 3 gibi tek sayı): "))
laplacian_olcek_faktoru = float(input("Laplacian filtresi ölçek faktörünü girin (örneğin, 1): "))
laplacian_delta_degeri = float(input("Laplacian filtresi delta değerini girin (örneğin, 0): "))

# Görüntüyü gri tonlamaya çevir
resim_gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

# Laplacian filtresi uygula
resim_laplacian = cv2.Laplacian(resim_gri, cv2.CV_64F, ksize=laplacian_kenar_boyu,
                                scale=laplacian_olcek_faktoru, delta=laplacian_delta_degeri)
resim_laplacian = cv2.convertScaleAbs(resim_laplacian)

# Orijinal ve Laplacian filtresi uygulanmış görüntüyü göster
cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Laplacian Filtre Uygulanmış Görüntü", resim_laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()

