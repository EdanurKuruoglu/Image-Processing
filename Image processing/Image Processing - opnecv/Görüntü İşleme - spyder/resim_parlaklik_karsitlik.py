import cv2
import numpy as np

resim = cv2.imread("Galata.jpeg")
resim = cv2.resize(resim, (646, 756))

# Kullanıcıdan parlaklık ve kontrast ayarlarını al
parlaklik_ayar = float(input("Parlaklık ayarını girin (örneğin, 1.5): "))
kontrast_ayar = float(input("Kontrast ayarını girin (örneğin, 1.5): "))

# Parlaklık ve kontrast ayarlamayı uygula
resim_ayarlanmis = np.clip(resim * kontrast_ayar + parlaklik_ayar, 0, 255).astype(np.uint8)

# Orijinal ve ayarlanmış görüntüyü göster
cv2.imshow("Orijinal Görüntü", resim)
cv2.imshow("Ayarlanmış Görüntü", resim_ayarlanmis)
cv2.waitKey(0)
cv2.destroyAllWindows()
