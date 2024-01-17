import cv2

resim = cv2.imread("Galata.jpeg")
resim=cv2.resize(resim, (646, 756))

# Renkli resim için negatif görüntüleme
negatif_renkli = cv2.bitwise_not(resim)
# Gri tonlamalı resim için negatif görüntüleme
gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
negatif_gri = cv2.bitwise_not(gri_resim)

# Negatif görüntüleri göster
cv2.imshow("Orijinal Resim", resim)
cv2.imshow("Negatif Renkli Resim", negatif_renkli)
cv2.imshow("Negatif Gri Resim", negatif_gri)
cv2.waitKey(0)
cv2.destroyAllWindows()
