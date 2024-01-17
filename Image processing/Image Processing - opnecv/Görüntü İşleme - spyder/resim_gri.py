import cv2
import numpy as np

resim = cv2.imread("Galata.jpeg") 
resim = cv2.resize(resim, (646, 756)) 
resim_gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

cv2.imshow("Galata",resim)
cv2.imshow("Galata_gri", resim_gri)
cv2.waitKey(0)       # Burada ekrana başka tuşa tıklanmadığı müddetçe kalması sağlanır.
cv2.destroyAllWindows()      # OpenCV'ye bağlı bütün pencerlerin kapanmasını sağlar.
