import cv2


resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 756))
# Kullanıcıdan yumuşatma faktörünü al
yumusatma_faktoru = float(input("Yumuşatma faktörünü girin (örneğin, 1): "))
# Yumuşatılmış görüntüyü elde et
yumusatilmis_resim = cv2.GaussianBlur(resim, (5, 5), 0)
# Belirgin kenar görüntüsünü elde et
kenar_goruntu = cv2.subtract(resim, yumusatilmis_resim)
# Netleştirilmiş görüntüyü elde et
netlesmis_resim = cv2.addWeighted(resim, 1, kenar_goruntu, yumusatma_faktoru, 0)
# Orijinal, yumuşatılmış, kenar görüntüsü ve netleştirilmiş görüntüyü göster
cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Netleştirilmiş Görüntü", netlesmis_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()


