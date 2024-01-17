import cv2

resim = cv2.imread("Galata.jpeg") 
resim = cv2.resize(resim, (646, 756))           # Ekrandaki resmin boyutunu düzenler.
cv2.imshow("Galata", resim)                 # Resmi ekranda gösterir.

cv2.waitKey(0)
cv2.destroyAllWindows()
