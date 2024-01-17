import cv2
import numpy as np

resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 756))

# Kullanıcıdan ölçek faktörünü al
olcek_faktoru = float(input("Ölçek faktörünü girin (örneğin, 0.5): "))
# Görüntüyü uzaklaştırma
uzaklastirilmis_resim = cv2.resize(resim, None, fx=olcek_faktoru, fy=olcek_faktoru, interpolation=cv2.INTER_LINEAR)
# Yeni bir görüntü oluştur ve beyaz arka plana sahip yap
boyut = resim.shape[:2]
arka_plan = np.ones((boyut[0], boyut[1], 3), dtype=np.uint8) * 255  # 255 değeri beyaz rengi temsil eder
arka_plan[0:uzaklastirilmis_resim.shape[0], 0:uzaklastirilmis_resim.shape[1], :] = uzaklastirilmis_resim

# Orijinal ve uzaklaştırılmış görüntüyü göster
cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Uzaklaştırılmış Görüntü", arka_plan)
cv2.waitKey(0)
cv2.destroyAllWindows()
