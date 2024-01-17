# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage
import cv2
import numpy as np
from PyQt5.QtCore import pyqtSlot
import math
from PIL import Image
from PIL import Image, ImageDraw
from QtDesigner3 import Ui_MainWindow # MODÜL ADI

class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.qtTasarim = Ui_MainWindow()
        self.qtTasarim.setupUi(self)
        self.qtTasarim.pushButton_resimdegistir.clicked.connect(self.show_image)
        self.qtTasarim.pushButton_ResimOku.clicked.connect(self.resim_oku)  
        self.qtTasarim.pushButton_griton.clicked.connect(self.griye_cevir)  
        self.qtTasarim.pushButton_parlaklik.clicked.connect(self.parlaklik)
        self.qtTasarim.pushButton_esikleme.clicked.connect(self.esikleme)
        self.qtTasarim.pushButton_Negatif.clicked.connect(self.Negatif)
        self.qtTasarim.pushButton_alcakgeciren_gauss.clicked.connect(self.Gauss)
        self.qtTasarim.pushButton_alcakgeciren_mean.clicked.connect(self.Mean)
        self.qtTasarim.pushButton_TuzBiber.clicked.connect(self.TuzBiber)
        self.qtTasarim.pushButton_Ortanca.clicked.connect(self.Ortanca)
        self.qtTasarim.pushButton_kontrast.clicked.connect(self.Kontrast)
        self.qtTasarim.pushButton_kontrass_germe.clicked.connect(self.Kontrast_Germe)
        self.qtTasarim.pushButton_sobel.clicked.connect(self.Sobel)
        self.qtTasarim.pushButton_prewitt.clicked.connect(self.Prewitt)
        self.qtTasarim.pushButton_yayma.clicked.connect(self.Yayma)
        self.qtTasarim.pushButton_asindirma.clicked.connect(self.Asindirma)
        self.qtTasarim.pushButton_opening.clicked.connect(self.Acma)
        self.qtTasarim.pushButton_close.clicked.connect(self.Kapama)
        self.qtTasarim.pushButton_kenar_netlestirme.clicked.connect(self.KenarResmiNetlestirme)
        self.qtTasarim.pushButton_konvolusyon_netlestirme.clicked.connect(self.Konvolusyon)
        self.qtTasarim.pushButton_cevirme.clicked.connect(self.AciliDondurme)
        self.qtTasarim.pushButton_tersdondurme.clicked.connect(self.TersDondurme)
        self.qtTasarim.pushButton_aynalama.clicked.connect(self.Aynalama)
        self.qtTasarim.pushButton_uzaklastirma.clicked.connect(self.Uzaklastirma)
        self.qtTasarim.pushButton_yakinlastirma.clicked.connect(self.Yakinlastirma)
        self.qtTasarim.pushButton_oteleme.clicked.connect(self.Oteleme_Tasima)
        self.qtTasarim.pushButton_histogram.clicked.connect(self.Histogram)
        self.qtTasarim.pushButton_kontrast_parlaklik.clicked.connect(self.Kontrast_Parlaklik_Ayari)
        self.qtTasarim.pushButton_goruntu_cevirme.clicked.connect(self.Goruntu_Cevirme)
        self.qtTasarim.pushButton_konvolusyon_cekirdek_matrisi.clicked.connect(self.Konvolusyon_Yontemi_Cekirdek_Matrisi_Netlestirme)
        self.qtTasarim.pushButton_histogram_esitleme.clicked.connect(self.Histogram_Esitleme)        
        #self.qtTasarim.pushButton_laplacian.clicked.connect(self.Laplacian)
        #self.qtTasarim.pushButton_gradyent.clicked.connect(self.Gradyent)        
        self.qtTasarim.pushButton_perspektif_duzeltme.clicked.connect(self.perspektif_duzeltme)     
        #self.qtTasarim.pushButton_korelasyon.clicked.connect(self.Korelasyon)
        #self.qtTasarim.pushButton_korelasyon_2.clicked.connect(self.Capraz_Korelasyon)
        
        self.current_image_path = None
        self.image_pixmap = None
        
      
    def show_image(self):
        dosya_isimleri, _ = QFileDialog.getOpenFileNames(self, 'Resim Seç', '', 'Resim Dosyaları (*.png *.jpg *.bmp *.jpeg)')

        if dosya_isimleri:
            self.current_image_path = dosya_isimleri[0]
            self.image_pixmap = QPixmap(self.current_image_path)
            self.qtTasarim.label_resim.setPixmap(self.image_pixmap)
            self.qtTasarim.label_resim.setScaledContents(True)
            
            
    def resim_oku(self):
        if self.current_image_path:
            
            from PIL import Image

            GirisResmi = Image.open(self.current_image_path)   
            ResimEn, ResimBoy = GirisResmi.size

            CikisResmi = Image.new("RGB", (ResimEn, ResimBoy))

            for x in range(ResimEn):
               for y in range(ResimBoy):
                   OkunanRenk = GirisResmi.getpixel((x, y))
                   CikisResmi.putpixel((x, y), OkunanRenk)

            #CikisResmi.save("resim_okuma.jpg")
            
            width, height = CikisResmi.size
            gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

            pixmap_gri = QPixmap.fromImage(gray_img_qimage)

            self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
            self.qtTasarim.label_cikti.setScaledContents(True)
            
    def matrix_multiply(matrix1, matrix2):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

        return result

# Şimdi de perspektif_duzeltme fonksiyonunu ekleyelim
    def perspektif_duzeltme(self):
        if self.current_image_path:
      

            GirisResmi = Image.open(self.current_image_path)
            ResimGenisligi, ResimYuksekligi = GirisResmi.size

            # Kenarları belirle
            pts1 = [[x1, y1, 1], [x2, y2, 1], [x3, y3, 1], [x4, y4, 1]]

            # Düzeltilecek perspektifi belirle
            pts2 = [[X1, Y1, 1], [X2, Y2, 1], [X3, Y3, 1], [X4, Y4, 1]]

            # Perspektif dönüşüm matrisini hesapla
            matrix = matrix_multiply(pts1, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
            matrix = matrix_multiply(matrix, pts2)

            # Normalize et
            matrix = [[elem / matrix[2][2] for elem in row] for row in matrix]

            # Perspektifi düzelt
            CikisResmi = Image.new('RGB', (ResimGenisligi, ResimYuksekligi))

            for x in range(ResimGenisligi):
                for y in range(ResimYuksekligi):
                    src_coords = matrix_multiply(matrix, [[x], [y], [1]])
                    src_x, src_y = int(src_coords[0][0]), int(src_coords[1][0])

                    if 0 <= src_x < ResimGenisligi and 0 <= src_y < ResimYuksekligi:
                        CikisResmi.putpixel((x, y), GirisResmi.getpixel((src_x, src_y)))

            # Düzeltildikten sonra resmi göster
            width, height = CikisResmi.size
            gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

            pixmap_gri = QPixmap.fromImage(gray_img_qimage)

            self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
            self.qtTasarim.label_cikti.setScaledContents(True)

    def griye_cevir(self):
        if self.current_image_path:
            
            from PIL import Image 
            GirisResmi = Image.open(self.current_image_path)  
            ResimEn, ResimBoy = GirisResmi.size 

            CikisResmi = Image.new("RGB", (ResimEn, ResimBoy)) 

            for x in range(ResimEn):
                for y in range(ResimBoy):
                    GelenRenk = GirisResmi.getpixel((x, y))
                    R, G, B = GelenRenk[0], GelenRenk[1], GelenRenk[2]
                    GriDeger = int(R * 0.3 + G * 0.6 + B * 0.1)
                    DonusenRenk = (GriDeger, GriDeger, GriDeger)
                    CikisResmi.putpixel((x, y), DonusenRenk)

            #CikisResmi.save("siyah_beyaz.jpg")
            
            width, height = CikisResmi.size
            gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

            pixmap_gri = QPixmap.fromImage(gray_img_qimage)

            self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
            self.qtTasarim.label_cikti.setScaledContents(True)

    def parlaklik(self):
        
        if self.current_image_path:
            from PIL import Image
            GirisResmi = Image.open(self.current_image_path) 
            ResimGenisligi, ResimYuksekligi = GirisResmi.size

            CikisResmi = Image.new("RGB", (ResimGenisligi, ResimYuksekligi))  

            try:
                ParlaklikDegeri = int(self.qtTasarim.textEdit.toPlainText())
                # Bu kısım sadece sayı girildiyse çalışacaktır
                print("Parlaklık Değeri:", ParlaklikDegeri)
            except ValueError:
                print("Hata: Geçerli bir sayı girin.")

            for x in range(ResimGenisligi):
                for y in range(ResimYuksekligi):
                    OkunanRenk = GirisResmi.getpixel((x, y))
                    R = OkunanRenk[0] + ParlaklikDegeri
                    G = OkunanRenk[1] + ParlaklikDegeri
                    B = OkunanRenk[2] + ParlaklikDegeri

            # EğerR,G,B değeri 255'i geçerse 255 olarak al dedim. 
            # Çünkü çok yüksek parlaklık değeri girince "unexpected indent" bu hatayı veriyor.
                    if R > 255:
                        R = 255
                    if G > 255:
                        G = 255
                    if B > 255:
                        B = 255

                    DonusenRenk = (R, G, B)
                    CikisResmi.putpixel((x, y), DonusenRenk)

            #CikisResmi.save("parlaklik.jpg")

            width, height = CikisResmi.size
            gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

            pixmap_gri = QPixmap.fromImage(gray_img_qimage)

            self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
            self.qtTasarim.label_cikti.setScaledContents(True)
            
    def esikleme(self):
        if self.current_image_path:
            
            from PIL import Image

            GirisResmi = Image.open(self.current_image_path) 
            ResimGenisligi, ResimYuksekligi = GirisResmi.size

            CikisResmi = Image.new("RGB", (ResimGenisligi, ResimYuksekligi))

            EsiklemeDegeri = int(self.qtTasarim.textEdit.toPlainText())

            for x in range(ResimGenisligi):
                for y in range(ResimYuksekligi):
                    OkunanRenk = GirisResmi.getpixel((x, y))
                    
                    if OkunanRenk[0] >= EsiklemeDegeri :
                        R = 255 
                    else : 
                        R = 0
                    if OkunanRenk[1] >= EsiklemeDegeri :
                        G = 255
                    else : 
                        G = 0
                    if OkunanRenk[2] >= EsiklemeDegeri : 
                        B = 255
                    else : 
                        B = 0

                    DonusenRenk = (R, G, B)
                    CikisResmi.putpixel((x, y), DonusenRenk)

            #CikisResmi.save("esikleme.jpg")
            
            width, height = CikisResmi.size
            gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

            pixmap_gri = QPixmap.fromImage(gray_img_qimage)

            self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
            self.qtTasarim.label_cikti.setScaledContents(True)
            
    def Negatif(self):
        if self.current_image_path:
            
            from PIL import Image

            GirisResmi = Image.open(self.current_image_path)
            ResimGenisligi, ResimYuksekligi = GirisResmi.size
            CikisResmi = Image.new("RGB", (ResimGenisligi, ResimYuksekligi))  

            for x in range(ResimGenisligi):
                for y in range(ResimYuksekligi):
                    OkunanRenk = GirisResmi.getpixel((x, y))
                    R = 255 - OkunanRenk[0]
                    G = 255 - OkunanRenk[1]
                    B = 255 - OkunanRenk[2]
                    DonusenRenk = (R, G, B)
                    CikisResmi.putpixel((x, y), DonusenRenk)

            #CikisResmi.save("negatifleme.jpg")
            
            width, height = CikisResmi.size
            gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

            pixmap_gri = QPixmap.fromImage(gray_img_qimage)

            self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
            self.qtTasarim.label_cikti.setScaledContents(True)
        
    def Gauss(self):
        if self.current_image_path:
            
            from PIL import Image
            import numpy as np
                
            sablon_boyutu = int(self.qtTasarim.textEdit.toPlainText())
            sigma = int(self.qtTasarim.textEdit_2.toPlainText())
                
            GirisResmi = Image.open(self.current_image_path)
            ResimGenisligi, ResimYuksekligi = GirisResmi.size
            CikisResmi = Image.new("RGB", (ResimGenisligi, ResimYuksekligi))

            ElemanSayisi = sablon_boyutu * sablon_boyutu

            matris = []
            for i in range(sablon_boyutu):
                for j in range(sablon_boyutu):
                    x = i - (sablon_boyutu - 1) / 2
                    y = j - (sablon_boyutu - 1) / 2
                    matris.append(1 / (2 * np.pi * sigma**2) * np.exp(-(x**2 + y**2) / (2 * sigma**2)))

            matris /= sum(matris)

            for x in range((sablon_boyutu - 1) // 2, ResimGenisligi - (sablon_boyutu - 1) // 2):
                for y in range((sablon_boyutu - 1) // 2, ResimYuksekligi - (sablon_boyutu - 1) // 2):
                    
                    toplamR, toplamG, toplamB = 0, 0, 0
                    k = 0

                    for i in range(-((sablon_boyutu - 1) // 2), (sablon_boyutu - 1) // 2 + 1):
                        for j in range(-((sablon_boyutu - 1) // 2), (sablon_boyutu - 1) // 2 + 1):
                            
                            OkunanRenk = GirisResmi.getpixel((x + i, y + j))
                            toplamR += OkunanRenk[0] * matris[k]
                            toplamG += OkunanRenk[1] * matris[k]
                            toplamB += OkunanRenk[2] * matris[k]
                            
                            k += 1

                    totelR = toplamR
                    totalG = toplamG
                    totalB = toplamB
                    CikisResmi.putpixel((x, y), (int(totelR), int(totalG), int(totalB)))

            #CikisResmi.save("gauss_filtre.jpg")
            
            width, height = CikisResmi.size
            gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

            pixmap_gri = QPixmap.fromImage(gray_img_qimage)

            self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
            self.qtTasarim.label_cikti.setScaledContents(True)
            
    def Mean(self):
        if self.current_image_path:
            
            from PIL import Image

            GirisResmi = Image.open(self.current_image_path) 
            ResimGenisligi, ResimYuksekligi = GirisResmi.size

            CikisResmi = Image.new("RGB", (ResimGenisligi, ResimYuksekligi))

            SablonBoyutu = int(self.qtTasarim.textEdit.toPlainText())  

            for x in range((SablonBoyutu - 1) // 2, ResimGenisligi - (SablonBoyutu - 1) // 2):
                for y in range((SablonBoyutu - 1) // 2, ResimYuksekligi - (SablonBoyutu - 1) // 2):
                    
                    toplamR, toplamG, toplamB = 0, 0, 0
                    
                    for i in range(-(SablonBoyutu - 1) // 2, (SablonBoyutu - 1) // 2 + 1):
                        for j in range(-(SablonBoyutu - 1) // 2, (SablonBoyutu - 1) // 2 + 1):
                            
                            OkunanRenk = GirisResmi.getpixel((x + i, y + j))
                            toplamR += OkunanRenk[0]
                            toplamG += OkunanRenk[1]
                            toplamB += OkunanRenk[2]
                            
                    ortalamaR = toplamR // (SablonBoyutu * SablonBoyutu)
                    ortalamaG = toplamG // (SablonBoyutu * SablonBoyutu)
                    ortalamaB = toplamB // (SablonBoyutu * SablonBoyutu)
                    CikisResmi.putpixel((x, y), (ortalamaR, ortalamaG, ortalamaB))

            #CikisResmi.save("mean_filtresi.jpg")
            
            width, height = CikisResmi.size
            gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

            pixmap_gri = QPixmap.fromImage(gray_img_qimage)

            self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
            self.qtTasarim.label_cikti.setScaledContents(True)
            
    def TuzBiber(self):
        if self.current_image_path:
            
            from PIL import Image
            import random

            GirisResmi = Image.open(self.current_image_path)
            ResimEn, ResimBoy = GirisResmi.size

            CikisResmi = GirisResmi.copy()

            tuz_orani = float(self.qtTasarim.textEdit.toPlainText())
            biber_orani = float(self.qtTasarim.textEdit_2.toPlainText())

            tuz_piksel_sayisi = int(tuz_orani * ResimEn * ResimBoy)
            biber_piksel_sayisi = int(biber_orani * ResimEn * ResimBoy)

            # Tuz eklenmesi
            for _ in range(tuz_piksel_sayisi):
               x, y = random.randint(0, ResimEn-1), random.randint(0, ResimBoy-1)
               CikisResmi.putpixel((x, y), (255, 255, 255))  # Beyaz renk (tuz)

            # Biber eklenmesi
            for _ in range(biber_piksel_sayisi):
               x, y = random.randint(0, ResimEn-1), random.randint(0, ResimBoy-1)
               CikisResmi.putpixel((x, y), (0, 0, 0))  # Siyah renk (biber)

            CikisResmi.save("tuz_biber.jpg")
            
            width, height = CikisResmi.size
            gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

            pixmap_gri = QPixmap.fromImage(gray_img_qimage)

            self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
            self.qtTasarim.label_cikti.setScaledContents(True)
            
    def Ortanca(self):
        if self.current_image_path:
            
            from PIL import Image
            import random

            GirisResmi = Image.open(self.current_image_path)
            ResimEn, ResimBoy = GirisResmi.size

            CikisResmi = GirisResmi.copy()

            tuz_orani = float(self.qtTasarim.textEdit.toPlainText())
            biber_orani = float(self.qtTasarim.textEdit_2.toPlainText())

            tuz_piksel_sayisi = int(tuz_orani * ResimEn * ResimBoy)
            biber_piksel_sayisi = int(biber_orani * ResimEn * ResimBoy)

            # Tuz eklenmesi
            for _ in range(tuz_piksel_sayisi):
               x, y = random.randint(0, ResimEn-1), random.randint(0, ResimBoy-1)
               CikisResmi.putpixel((x, y), (255, 255, 255))  # Beyaz renk (tuz)

            # Biber eklenmesi
            for _ in range(biber_piksel_sayisi):
               x, y = random.randint(0, ResimEn-1), random.randint(0, ResimBoy-1)
               CikisResmi.putpixel((x, y), (0, 0, 0))  # Siyah renk (biber)

            CikisResmi.save("tuz_biber.jpg")  

            # -----------------------------------------------------------------------------

            GirisResmi = Image.open("tuz_biber.jpg")
            ResimGenislik, ResimYukseklik = GirisResmi.size

            SablonBoyutu = int(self.qtTasarim.textEdit_3.toPlainText())

            ElemanSayisi = SablonBoyutu * SablonBoyutu

            R = [0] * ElemanSayisi
            G = [0] * ElemanSayisi
            B = [0] * ElemanSayisi
            Gri = [0] * ElemanSayisi


            for x in range(ResimGenislik-SablonBoyutu):
                for y in range(ResimYukseklik-SablonBoyutu):
                    
                    k = 0
                           
                    for i in range(-((SablonBoyutu - 1) // 2), (SablonBoyutu - 1) // 2 + 1):
                        for j in range(-((SablonBoyutu - 1) // 2), (SablonBoyutu - 1) // 2 + 1):
                            
                            OkunanRenk = GirisResmi.getpixel((x + i, y + j))
                            
                            R[k] = OkunanRenk[0]
                            G[k] = OkunanRenk[1]
                            B[k] = OkunanRenk[2]
                            
                            Gri[k] = int(R[k] * 0.299 + G[k] * 0.587 + B[k] * 0.114)
                            k += 1

                    # Gri tona göre sıralama yapıyor. Aynı anda üç rengi değiştiriyor.
                    for i in range(ElemanSayisi):
                        for j in range(i + 1, ElemanSayisi):
                            
                            if Gri[j] < Gri[i]:
                                
                                temp_Gri = Gri[i]
                                temp_R = R[i]
                                temp_G = G[i]
                                temp_B = B[i]

                                # Elemanlar yer değiştirildi
                                Gri[i] = Gri[j]
                                R[i] = R[j]
                                G[i] = G[j]
                                B[i] = B[j]

                                Gri[j] = temp_Gri
                                R[j] = temp_R
                                G[j] = temp_G
                                B[j] = temp_B

                    # Sıralama sonrası ortadaki değeri çıkış resminin piksel değeri olarak atılıyor
                    CikisResmi.putpixel((x, y), (R[(ElemanSayisi - 1) // 2], G[(ElemanSayisi - 1) // 2], B[(ElemanSayisi - 1) // 2]))

            #CikisResmi.save("medyan_filtresi.jpg")
            
            width, height = CikisResmi.size
            gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

            pixmap_gri = QPixmap.fromImage(gray_img_qimage)

            self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
            self.qtTasarim.label_cikti.setScaledContents(True)
            
    def Kontrast(self):
        if self.current_image_path:
                    
            from PIL import Image

            R, G, B = 0, 0, 0
            GirisResmi = Image.open(self.current_image_path)
            ResimEn, ResimBoy = GirisResmi.size

            CikisResmi = Image.new("RGB", (ResimEn, ResimBoy))

            c_kontrast_seviyesi = float(self.qtTasarim.textEdit.toPlainText())
            f_kontrast_faktoru = (259 * (c_kontrast_seviyesi + 255)) / (255 * (259 - c_kontrast_seviyesi))

            for x in range(ResimEn):
                for y in range(ResimBoy):
                           
                    OkunanRenk = GirisResmi.getpixel((x, y))
                    R, G, B = OkunanRenk[0], OkunanRenk[1], OkunanRenk[2]

                    R = int((f_kontrast_faktoru * (R - 128)) + 128)
                    G = int((f_kontrast_faktoru * (G - 128)) + 128)
                    B = int((f_kontrast_faktoru * (B - 128)) + 128)

                    R = min(255, max(0, R))
                    G = min(255, max(0, G))
                    B = min(255, max(0, B))

                    donusen_renk = (R, G, B)
                    CikisResmi.putpixel((x, y), donusen_renk)

            #CikisResmi.save("kontrast.jpg")
                    
            width, height = CikisResmi.size
            gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

            pixmap_gri = QPixmap.fromImage(gray_img_qimage)

            self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
            self.qtTasarim.label_cikti.setScaledContents(True)
            
    def Kontrast_Germe(self):
        if self.current_image_path:
                    
           from PIL import Image

           GirisResmi = Image.open(self.current_image_path)
           ResimEn, ResimBoy = GirisResmi.size

           CikisResmi = Image.new("RGB", (ResimEn, ResimBoy))

           x1 = int(self.qtTasarim.textEdit.toPlainText()) 
           x2 = int(self.qtTasarim.textEdit_2.toPlainText()) 
           a = 0  
           b = 255  

           for x in range(ResimEn):
               for y in range(ResimBoy):
                   
                   OkunanRenk = GirisResmi.getpixel((x, y))
                   red = OkunanRenk[0]

                   gri = red

                   x_value = gri
                   c = (((x_value - x1) * (b - a)) / (x2 - x1)) + a

                   c = min(255, max(0, int(c)))

                   DonusenRenk = (c, c, c)
                   CikisResmi.putpixel((x, y), DonusenRenk)

           CikisResmi.save("kontrastGerme.jpg")
                    
        width, height = CikisResmi.size
        gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

        pixmap_gri = QPixmap.fromImage(gray_img_qimage)

        self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
        self.qtTasarim.label_cikti.setScaledContents(True)            

    def Laplacian(self):
        if self.current_image_path:
                    
           from PIL import Image

           GirisResmi = Image.open(self.current_image_path)
           ResimEn, ResimBoy = GirisResmi.size

           CikisResmi = Image.new("RGB", (ResimEn, ResimBoy))

           x1 = int(self.qtTasarim.textEdit.toPlainText()) 
           x2 = int(self.qtTasarim.textEdit_2.toPlainText()) 
           a = 0  # int(input("A Değeri: "))
           b = 255  # int(input("B Değeri: "))

           for x in range(ResimEn):
               for y in range(ResimBoy):
                   
                   OkunanRenk = GirisResmi.getpixel((x, y))
                   red = OkunanRenk[0]

                   gri = red

                   x_value = gri
                   c = (((x_value - x1) * (b - a)) / (x2 - x1)) + a

                   c = min(255, max(0, int(c)))

                   DonusenRenk = (c, c, c)
                   CikisResmi.putpixel((x, y), DonusenRenk)

           CikisResmi.save("kontrastGerme.jpg")
                    
        width, height = CikisResmi.size
        gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

        pixmap_gri = QPixmap.fromImage(gray_img_qimage)

        self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
        self.qtTasarim.label_cikti.setScaledContents(True)    
          
    def Sobel(self):
        if self.current_image_path:
                    
           from PIL import Image
           import math

           GirisResmi = Image.open(self.current_image_path)
           ResimEn, ResimBoy = GirisResmi.size

           CikisResmi_x = Image.new("RGB", (ResimEn, ResimBoy))
           CikisResmi_y = Image.new("RGB", (ResimEn, ResimBoy))
           CikisResmi_xy = Image.new("RGB", (ResimEn, ResimBoy))

           SablonBoyutu = int(self.qtTasarim.textEdit.toPlainText()) 
           x1, x2 = (SablonBoyutu - 1) // 2, ResimEn - (SablonBoyutu - 1) // 2

           for x in range(x1, x2):
               for y in range((SablonBoyutu - 1) // 2, ResimBoy - (SablonBoyutu - 1) // 2):
                   p1 = sum(GirisResmi.getpixel((x - 1, y - 1))) // 3
                   p2 = sum(GirisResmi.getpixel((x, y - 1))) // 3
                   p3 = sum(GirisResmi.getpixel((x + 1, y - 1))) // 3
                   p4 = sum(GirisResmi.getpixel((x - 1, y))) // 3
                   p5 = sum(GirisResmi.getpixel((x, y))) // 3
                   p6 = sum(GirisResmi.getpixel((x + 1, y))) // 3
                   p7 = sum(GirisResmi.getpixel((x - 1, y + 1))) // 3
                   p8 = sum(GirisResmi.getpixel((x, y + 1))) // 3
                   p9 = sum(GirisResmi.getpixel((x + 1, y + 1))) // 3

                   gx = abs(-p1 + p3 - 2 * p4 + 2 * p6 - p7 + p9)
                   gy = abs(p1 + 2 * p2 + p3 - p7 - 2 * p8 - p9)
                   gxy = gx + gy

                   gx = min(255, max(0, gx))
                   gy = min(255, max(0, gy))
                   gxy = min(255, max(0, gxy))

                   CikisResmi_x.putpixel((x, y), (gx, gx, gx))
                   CikisResmi_y.putpixel((x, y), (gy, gy, gy))
                   CikisResmi_xy.putpixel((x, y), (gxy, gxy, gxy))
                   

           #CikisResmi_x.save("Sobel_X.jpg")
           #CikisResmi_y.save("Sobel_Y.jpg")
           #CikisResmi_xy.save("Sobel_XY.jpg")
                    
        width, height = CikisResmi_xy.size
        gray_img_qimage = QImage(CikisResmi_xy.tobytes(), width, height, QImage.Format_RGB888)

        pixmap_gri = QPixmap.fromImage(gray_img_qimage)

        self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
        self.qtTasarim.label_cikti.setScaledContents(True) 
        
    def Prewitt(self):
        if self.current_image_path:
                    
           from PIL import Image
           import math

           GirisResmi = Image.open(self.current_image_path)
           ResimEn, ResimBoy = GirisResmi.size

           CikisResmi = Image.new("RGB", (ResimEn, ResimBoy))

           SablonBoyutu = int(self.qtTasarim.textEdit.toPlainText()) 
           x1, x2 = (SablonBoyutu - 1) // 2, ResimEn - (SablonBoyutu - 1) // 2

           for x in range(x1, x2):
               for y in range((SablonBoyutu - 1) // 2, ResimBoy - (SablonBoyutu - 1) // 2):
                   p1 = sum(GirisResmi.getpixel((x - 1, y - 1))) // 3
                   p2 = sum(GirisResmi.getpixel((x, y - 1))) // 3
                   p3 = sum(GirisResmi.getpixel((x + 1, y - 1))) // 3
                   p4 = sum(GirisResmi.getpixel((x - 1, y))) // 3
                   p5 = sum(GirisResmi.getpixel((x, y))) // 3
                   p6 = sum(GirisResmi.getpixel((x + 1, y))) // 3
                   p7 = sum(GirisResmi.getpixel((x - 1, y + 1))) // 3
                   p8 = sum(GirisResmi.getpixel((x, y + 1))) // 3
                   p9 = sum(GirisResmi.getpixel((x + 1, y + 1))) // 3

                   gx = abs(-p1 + p3 - p4 + p6 - p7 + p9)  # Dikey çizgileri Bulur
                   gy = abs(p1 + p2 + p3 - p7 - p8 - p9)  # Yatay Çizgileri Bulur.

                   prewitt_degeri = gx + gy  # 1. Formül
                   # prewitt_degeri = int(math.sqrt(gx * gx + gy * gy))  # 2. Formül

                   prewitt_degeri = min(255, prewitt_degeri)  # Sınırların dışına çıktıysa, sınır değer alınacak.
                   CikisResmi.putpixel((x, y), (prewitt_degeri, prewitt_degeri, prewitt_degeri))

           #CikisResmi.save("Prewitt.jpg")
                    
        width, height = CikisResmi.size
        gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

        pixmap_gri = QPixmap.fromImage(gray_img_qimage)

        self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
        self.qtTasarim.label_cikti.setScaledContents(True)

    def Yayma(self):
        if self.current_image_path:
                    
           from PIL import Image

           GirisResmi = Image.open(self.current_image_path)
           ResimEn, ResimBoy = GirisResmi.size

           CikisResmi = Image.new("RGB", (ResimEn, ResimBoy))

           SablonBoyutu = int(self.qtTasarim.textEdit.toPlainText())  

           for x in range((SablonBoyutu - 1) // 2, ResimEn - (SablonBoyutu - 1) // 2):
               for y in range((SablonBoyutu - 1) // 2, ResimBoy - (SablonBoyutu - 1) // 2):
                   kendi_rengi = GirisResmi.getpixel((x, y))

                   if kendi_rengi[0] < 128:  # Kendi rengi siyahsa, komşuları tara beyaz bulmak için.
                       komsularda_beyaz_renk_var = False

                       for i in range(-((SablonBoyutu - 1) // 2), (SablonBoyutu - 1) // 2 + 1):
                           for j in range(-((SablonBoyutu - 1) // 2), (SablonBoyutu - 1) // 2 + 1):
                               komsu_rengi = GirisResmi.getpixel((x + i, y + j))

                               if komsu_rengi[0] > 128:  # Komsu rengi beyaz ise
                                   komsularda_beyaz_renk_var = True

                       if komsularda_beyaz_renk_var:  # Komşularda beyaz renk varsa kendi rengini beyaz yap
                           CikisResmi.putpixel((x, y), (255, 255, 255))
                       else:  # Komşularda siyah yok ise kendi rengi yine aynı beyaz kalmalı.
                           CikisResmi.putpixel((x, y), (0, 0, 0))
                   else:  # Kendi rengi beyaz ise beyaz kal.
                       CikisResmi.putpixel((x, y), (255, 255, 255))

           #CikisResmi.save("Yayma.jpg")
                    
        width, height = CikisResmi.size
        gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

        pixmap_gri = QPixmap.fromImage(gray_img_qimage)

        self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
        self.qtTasarim.label_cikti.setScaledContents(True)    
        
    def Asindirma(self):
        if self.current_image_path:
                    
           from PIL import Image

           giris_resmi = Image.open(self.current_image_path)
           ResimEn, ResimBoy = giris_resmi.size

           CikisResmi = Image.new("RGB", (ResimEn, ResimBoy))

           SablonBoyutu = int(self.qtTasarim.textEdit.toPlainText()) 

           for x in range((SablonBoyutu - 1) // 2, ResimEn - (SablonBoyutu - 1) // 2):
               for y in range((SablonBoyutu - 1) // 2, ResimBoy - (SablonBoyutu - 1) // 2):
                   kendi_rengi = giris_resmi.getpixel((x, y))

                   if kendi_rengi[0] > 128:  
                       komsularda_siyah_var = False

                       for i in range(-((SablonBoyutu - 1) // 2), (SablonBoyutu - 1) // 2 + 1):
                           for j in range(-((SablonBoyutu - 1) // 2), (SablonBoyutu - 1) // 2 + 1):
                               komsu_rengi = giris_resmi.getpixel((x + i, y + j))

                               if komsu_rengi[0] < 128:  
                                   komsularda_siyah_var = True

                       if komsularda_siyah_var:  
                           CikisResmi.putpixel((x, y), (0, 0, 0))
                       else:  
                           CikisResmi.putpixel((x, y), (255, 255, 255))
                   else:  
                       CikisResmi.putpixel((x, y), (0, 0, 0))

           #CikisResmi.save("Asindirma.jpg")
                    
        width, height = CikisResmi.size
        gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

        pixmap_gri = QPixmap.fromImage(gray_img_qimage)

        self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
        self.qtTasarim.label_cikti.setScaledContents(True) 

    def Acma(self):
        if self.current_image_path:
                    
           from PIL import Image

           giris_resmi = Image.open(self.current_image_path)
           ResimEn, ResimBoy = giris_resmi.size

           CikisResmi1 = Image.new("RGB", (ResimEn, ResimBoy))

           SablonBoyutu1 = int(self.qtTasarim.textEdit.toPlainText()) 

           for x in range((SablonBoyutu1 - 1) // 2, ResimEn - (SablonBoyutu1 - 1) // 2):
               for y in range((SablonBoyutu1 - 1) // 2, ResimBoy - (SablonBoyutu1 - 1) // 2):
                   kendi_rengi = giris_resmi.getpixel((x, y))

                   if kendi_rengi[0] > 128:  
                       komsularda_siyah_var = False

                       for i in range(-((SablonBoyutu1 - 1) // 2), (SablonBoyutu1 - 1) // 2 + 1):
                           for j in range(-((SablonBoyutu1 - 1) // 2), (SablonBoyutu1 - 1) // 2 + 1):
                               komsu_rengi = giris_resmi.getpixel((x + i, y + j))

                               if komsu_rengi[0] < 128:  
                                   komsularda_siyah_var = True

                       if komsularda_siyah_var:  
                           CikisResmi1.putpixel((x, y), (0, 0, 0))
                       else:  
                           CikisResmi1.putpixel((x, y), (255, 255, 255))
                   else:  
                       CikisResmi1.putpixel((x, y), (0, 0, 0))

           CikisResmi1.save("Asindirma.jpg")

           GirisResmi = Image.open("Asindirma.jpg")
           ResimEn, ResimBoy = GirisResmi.size

           CikisResmi = Image.new("RGB", (ResimEn, ResimBoy))

           SablonBoyutu = SablonBoyutu1 

           for x in range((SablonBoyutu - 1) // 2, ResimEn - (SablonBoyutu - 1) // 2):
               for y in range((SablonBoyutu - 1) // 2, ResimBoy - (SablonBoyutu - 1) // 2):
                   kendi_rengi = GirisResmi.getpixel((x, y))

                   if kendi_rengi[0] < 128:  # Kendi rengi siyahsa, komşuları tara beyaz var mı
                       komsularda_beyaz_renk_var = False

                       for i in range(-((SablonBoyutu - 1) // 2), (SablonBoyutu - 1) // 2 + 1):
                           for j in range(-((SablonBoyutu - 1) // 2), (SablonBoyutu - 1) // 2 + 1):
                               komsu_rengi = GirisResmi.getpixel((x + i, y + j))

                               if komsu_rengi[0] > 128:  # Komsu rengi beyaz ise
                                   komsularda_beyaz_renk_var = True

                       if komsularda_beyaz_renk_var:  # Madem komsularda beyaz renk var, o zaman kendi rengini de beyaz yap.
                           CikisResmi.putpixel((x, y), (255, 255, 255))
                       else:  # Komşularda siyah yok ise kendi rengi yine aynı beyaz kalmalı.
                           CikisResmi.putpixel((x, y), (0, 0, 0))
                   else:  # Kendi rengi beyaz ise beyaz kal.
                       CikisResmi.putpixel((x, y), (255, 255, 255))

           #CikisResmi.save("AcmaIslemi.jpg")
                    
        width, height = CikisResmi.size
        gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

        pixmap_gri = QPixmap.fromImage(gray_img_qimage)

        self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
        self.qtTasarim.label_cikti.setScaledContents(True)
        
    def Kapama(self):
        if self.current_image_path:
                    
           from PIL import Image

           GirisResmi = Image.open(self.current_image_path)
           ResimEn, ResimBoy = GirisResmi.size

           CikisResmi1 = Image.new("RGB", (ResimEn, ResimBoy))

           SablonBoyutu1 = int(self.qtTasarim.textEdit.toPlainText())  

           for x in range((SablonBoyutu1 - 1) // 2, ResimEn - (SablonBoyutu1 - 1) // 2):
               for y in range((SablonBoyutu1 - 1) // 2, ResimBoy - (SablonBoyutu1 - 1) // 2):
                   kendi_rengi = GirisResmi.getpixel((x, y))

                   if kendi_rengi[0] < 128:  # Kendi rengi siyahsa, komşuları tara beyaz var mı
                       komsularda_beyaz_renk_var = False

                       for i in range(-((SablonBoyutu1 - 1) // 2), (SablonBoyutu1 - 1) // 2 + 1):
                           for j in range(-((SablonBoyutu1 - 1) // 2), (SablonBoyutu1 - 1) // 2 + 1):
                               komsu_rengi = GirisResmi.getpixel((x + i, y + j))

                               if komsu_rengi[0] > 128:  # Komsu rengi beyaz ise
                                   komsularda_beyaz_renk_var = True

                       if komsularda_beyaz_renk_var:  # Madem komsularda beyaz renk var, o zaman kendi rengini de beyaz yap.
                           CikisResmi1.putpixel((x, y), (255, 255, 255))
                       else:  # Komşularda siyah yok ise kendi rengi yine aynı beyaz kalmalı.
                           CikisResmi1.putpixel((x, y), (0, 0, 0))
                   else:  # Kendi rengi beyaz ise beyaz kal.
                       CikisResmi1.putpixel((x, y), (255, 255, 255))

           CikisResmi1.save("Yayma.jpg")

           giris_resmi = Image.open("Yayma.jpg")
           ResimEn, ResimBoy = giris_resmi.size

           CikisResmi = Image.new("RGB", (ResimEn, ResimBoy))

           SablonBoyutu = SablonBoyutu1 

           for x in range((SablonBoyutu - 1) // 2, ResimEn - (SablonBoyutu - 1) // 2):
               for y in range((SablonBoyutu - 1) // 2, ResimBoy - (SablonBoyutu - 1) // 2):
                   kendi_rengi = giris_resmi.getpixel((x, y))

                   if kendi_rengi[0] > 128:  
                       komsularda_siyah_var = False

                       for i in range(-((SablonBoyutu - 1) // 2), (SablonBoyutu - 1) // 2 + 1):
                           for j in range(-((SablonBoyutu - 1) // 2), (SablonBoyutu - 1) // 2 + 1):
                               komsu_rengi = giris_resmi.getpixel((x + i, y + j))

                               if komsu_rengi[0] < 128:  
                                   komsularda_siyah_var = True

                       if komsularda_siyah_var:  
                           CikisResmi.putpixel((x, y), (0, 0, 0))
                       else:  
                           CikisResmi.putpixel((x, y), (255, 255, 255))
                   else:  
                       CikisResmi.putpixel((x, y), (0, 0, 0))

           #CikisResmi.save("Kapama.jpg")
                    
        width, height = CikisResmi.size
        gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

        pixmap_gri = QPixmap.fromImage(gray_img_qimage)

        self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
        self.qtTasarim.label_cikti.setScaledContents(True)

    def KenarResmiNetlestirme(self):
        if self.current_image_path:
                    
           from PIL import Image

           def netlestirme():
               GirisResmi = Image.open(self.current_image_path)
               ResimGenisligi, ResimYuksekligi = GirisResmi.size
               
               # BULANIKLAŞTIRILMIŞ RESİM (MEAN FİLTRESİ)

               CikisResmi = Image.new("RGB", (ResimGenisligi, ResimYuksekligi))

               SablonBoyutu = int(self.qtTasarim.textEdit.toPlainText())   

               for x in range((SablonBoyutu - 1) // 2, ResimGenisligi - (SablonBoyutu - 1) // 2):
                   for y in range((SablonBoyutu - 1) // 2, ResimYuksekligi - (SablonBoyutu - 1) // 2):
                       
                       toplamR, toplamG, toplamB = 0, 0, 0
                       
                       for i in range(-(SablonBoyutu - 1) // 2, (SablonBoyutu - 1) // 2 + 1):
                           for j in range(-(SablonBoyutu - 1) // 2, (SablonBoyutu - 1) // 2 + 1):
                               
                               OkunanRenk = GirisResmi.getpixel((x + i, y + j))
                               toplamR += OkunanRenk[0]
                               toplamG += OkunanRenk[1]
                               toplamB += OkunanRenk[2]
                               
                       ortalamaR = toplamR // (SablonBoyutu * SablonBoyutu)
                       ortalamaG = toplamG // (SablonBoyutu * SablonBoyutu)
                       ortalamaB = toplamB // (SablonBoyutu * SablonBoyutu)
                       CikisResmi.putpixel((x, y), (ortalamaR, ortalamaG, ortalamaB))

               CikisResmi.save("mean_filtresi.jpg")
               
               # FONKSİYONLARA GİTME
               
               bulanik_resim = Image.open("mean_filtresi.jpg")  # veya gauss_filtresi() fonksiyonunu kullanabilirsiniz.
               
               kenar_goruntusu = orijinal_resimden_bulanik_resmi_cikarma(GirisResmi, bulanik_resim)
               netlesmis_resim = kenar_goruntusu_ile_orjinal_resmi_birlestir(GirisResmi, kenar_goruntusu)

               netlesmis_resim.save("NetlesmisResim.jpg")
               
               width, height = netlesmis_resim.size
               gray_img_qimage = QImage(netlesmis_resim.tobytes(), width, height, QImage.Format_RGB888)

               pixmap_gri = QPixmap.fromImage(gray_img_qimage)

               self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
               self.qtTasarim.label_cikti.setScaledContents(True)

           def orijinal_resimden_bulanik_resmi_cikarma(orjinal_resim, bulanik_resim):
               resim_genisligi, resim_yuksekligi = orjinal_resim.size
               cikis_resmi = Image.new("RGB", (resim_genisligi, resim_yuksekligi))

               olcekleme = 2

               for x in range(resim_genisligi):
                   for y in range(resim_yuksekligi):
                       okunan_renk1 = orjinal_resim.getpixel((x, y))
                       okunan_renk2 = bulanik_resim.getpixel((x, y))

                       r = int(olcekleme * abs(okunan_renk1[0] - okunan_renk2[0]))
                       g = int(olcekleme * abs(okunan_renk1[1] - okunan_renk2[1]))
                       b = int(olcekleme * abs(okunan_renk1[2] - okunan_renk2[2]))

                       r = min(max(0, r), 255)
                       g = min(max(0, g), 255)
                       b = min(max(0, b), 255)

                       donusen_renk = (r, g, b)
                       cikis_resmi.putpixel((x, y), donusen_renk)

               return cikis_resmi

           def kenar_goruntusu_ile_orjinal_resmi_birlestir(orjinal_resim, kenar_goruntusu):
               resim_genisligi, resim_yuksekligi = orjinal_resim.size
               cikis_resmi = Image.new("RGB", (resim_genisligi, resim_yuksekligi))

               for x in range(resim_genisligi):
                   for y in range(resim_yuksekligi):
                       okunan_renk1 = orjinal_resim.getpixel((x, y))
                       okunan_renk2 = kenar_goruntusu.getpixel((x, y))

                       r = okunan_renk1[0] + okunan_renk2[0]
                       g = okunan_renk1[1] + okunan_renk2[1]
                       b = okunan_renk1[2] + okunan_renk2[2]

                       r = min(max(0, r), 255)
                       g = min(max(0, g), 255)
                       b = min(max(0, b), 255)

                       donusen_renk = (r, g, b)
                       cikis_resmi.putpixel((x, y), donusen_renk)

               return cikis_resmi

           netlestirme()

           CikisResmi.save("Kapama.jpg")
           
    def Konvolusyon(self):
        if self.current_image_path:
                    
           from PIL import Image

           GirisResmi = Image.open(self.current_image_path)
           ResimGenisligi, ResimYuksekligi = GirisResmi.size
               
           CikisResmi = Image.new("RGB", (ResimGenisligi, ResimYuksekligi))
               
           # Define the convolution matrix
           convolution_matrix = [0, -2, 0, -2, 11, -2, 0, -2, 0]
           matrix_sum = sum(convolution_matrix)
               
               # Apply convolution to each pixel in the image
           for x in range((3 - 1) // 2, ResimGenisligi - (3 - 1) // 2):
               for y in range((3 - 1) // 2, ResimYuksekligi - (3 - 1) // 2):
                   total_r, total_g, total_b = 0, 0, 0
                   k = 0
                       
                       # Iterate through the convolution matrix
                   for i in range(-(3 - 1) // 2, (3 - 1) // 2 + 1):
                       for j in range(-(3 - 1) // 2, (3 - 1) // 2 + 1):
                           pixel = GirisResmi.getpixel((x + i, y + j))
                           total_r += pixel[0] * convolution_matrix[k]
                           total_g += pixel[1] * convolution_matrix[k]
                           total_b += pixel[2] * convolution_matrix[k]
                           k += 1
                       
                       # Calculate new RGB values
                   new_r = total_r // matrix_sum
                   new_g = total_g // matrix_sum
                   new_b = total_b // matrix_sum
                       
                       # Clip values to be within 0-255
                   new_r = min(max(0, new_r), 255)
                   new_g = min(max(0, new_g), 255)
                   new_b = min(max(0, new_b), 255)
                       
                       # Set the pixel value in the output image
                   CikisResmi.putpixel((x, y), (new_r, new_g, new_b))
               
               # Display the output image
           #CikisResmi.save("Konvolusyon.jpg")
                    
        width, height = CikisResmi.size
        gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

        pixmap_gri = QPixmap.fromImage(gray_img_qimage)

        self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
        self.qtTasarim.label_cikti.setScaledContents(True)
    
    def AciliDondurme(self):
        if self.current_image_path:
                    
           from PIL import Image, ImageDraw, ImageTk
           import math

           GirisResmi = Image.open(self.current_image_path)
           ResimGenisligi, ResimYuksekligi = GirisResmi.size
               
           angle =  int(self.qtTasarim.textEdit.toPlainText())
           radian_angle = math.radians(angle)
               
               # Create a blank output image
           CikisResmi = Image.new("RGB", (ResimGenisligi, ResimYuksekligi), color="white")
               
               # Find the center of the image
           center_x = ResimGenisligi // 2
           center_y = ResimYuksekligi // 2
               
               # Perform rotation around the center of the image
           for x1 in range(ResimGenisligi):
               for y1 in range(ResimYuksekligi):
                       # Apply rotation formulas
                   x2 = math.cos(radian_angle) * (x1 - center_x) - math.sin(radian_angle) * (y1 - center_y) + center_x
                   y2 = math.sin(radian_angle) * (x1 - center_x) + math.cos(radian_angle) * (y1 - center_y) + center_y
                       
                       # Check if the new coordinates are within the bounds of the image
                   if 0 < x2 < ResimGenisligi and 0 < y2 < ResimYuksekligi:
                       pixel_value = GirisResmi.getpixel((x1, y1))
                       CikisResmi.putpixel((int(x2), int(y2)), pixel_value)
               
           #CikisResmi.save("Dondurme.jpg")
                    
        width, height = CikisResmi.size
        gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

        pixmap_gri = QPixmap.fromImage(gray_img_qimage)

        self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
        self.qtTasarim.label_cikti.setScaledContents(True)

    def TersDondurme(self):
        if self.current_image_path:
                    
           from PIL import Image, ImageDraw, ImageTk
           import math

           GirisResmi = Image.open(self.current_image_path)
           ResimGenisligi, ResimYuksekligi = GirisResmi.size
               
           angle = 180
           radian_angle = math.radians(angle)
               
               # Create a blank output image
           CikisResmi = Image.new("RGB", (ResimGenisligi, ResimYuksekligi), color="white")
               
               # Find the center of the image
           center_x = ResimGenisligi // 2
           center_y = ResimYuksekligi // 2
               
               # Perform rotation around the center of the image
           for x1 in range(ResimGenisligi):
               for y1 in range(ResimYuksekligi):
                       # Apply rotation formulas
                   x2 = math.cos(radian_angle) * (x1 - center_x) - math.sin(radian_angle) * (y1 - center_y) + center_x
                   y2 = math.sin(radian_angle) * (x1 - center_x) + math.cos(radian_angle) * (y1 - center_y) + center_y
                       
                       # Check if the new coordinates are within the bounds of the image
                   if 0 < x2 < ResimGenisligi and 0 < y2 < ResimYuksekligi:
                       pixel_value = GirisResmi.getpixel((x1, y1))
                       CikisResmi.putpixel((int(x2), int(y2)), pixel_value)
               
           #CikisResmi.save("TersCevirme.jpg")
                    
        width, height = CikisResmi.size
        gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

        pixmap_gri = QPixmap.fromImage(gray_img_qimage)

        self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
        self.qtTasarim.label_cikti.setScaledContents(True)

    def Aynalama(self):
        if self.current_image_path:
                    
           from PIL import Image, ImageDraw, ImageTk
           import math

           GirisResmi = Image.open(self.current_image_path)
           ResimGenisligi, ResimYuksekligi = GirisResmi.size
               
           CikisResmi = Image.new("RGB", (ResimGenisligi, ResimYuksekligi), color="white")
               
           angle = 90
           radian_angle = angle * 2 * math.pi / 360
               
           center_x = ResimGenisligi // 2
           center_y = ResimYuksekligi // 2
               
           for x1 in range(ResimGenisligi):
               for y1 in range(ResimYuksekligi):
                   delta = (x1 - center_x) * math.sin(radian_angle) - (y1 - center_y) * math.cos(radian_angle)
                   x2 = int(x1 + 2 * delta * (-math.sin(radian_angle)))
                   y2 = int(y1 + 2 * delta * (math.cos(radian_angle)))
                       
                   if 0 < x2 < ResimGenisligi and 0 < y2 < ResimYuksekligi:
                       pixel_value = GirisResmi.getpixel((x1, y1))
                       CikisResmi.putpixel((x2, y2), pixel_value)
               
           #CikisResmi.save("Aynalama.jpg")
                    
        width, height = CikisResmi.size
        gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

        pixmap_gri = QPixmap.fromImage(gray_img_qimage)

        self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
        self.qtTasarim.label_cikti.setScaledContents(True)
        
    def Uzaklastirma(self):
        if self.current_image_path:
            
           from PIL import Image, ImageDraw, ImageTk
           import math
                    
           GirisResmi = Image.open(self.current_image_path)
           ResimGenisligi, ResimYuksekligi = GirisResmi.size
           CikisResmi = Image.new("RGB", (ResimGenisligi // 2, ResimYuksekligi // 2))

           x2, y2 = 0, 0  # Çıkış resminin x ve y'si
           KucultmeKatsayisi = int(self.qtTasarim.textEdit.toPlainText())

           for x1 in range(0, ResimGenisligi, KucultmeKatsayisi):
               y2 = 0
               for y1 in range(0, ResimYuksekligi, KucultmeKatsayisi):
                   OkunanRenk = GirisResmi.getpixel((x1, y1))
                   CikisResmi.putpixel((x2, y2), OkunanRenk)
                   y2 += 1
               x2 += 1

           #CikisResmi.save("Kucultme.jpg")
           
           width, height = CikisResmi.size
           gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

           pixmap_gri = QPixmap.fromImage(gray_img_qimage)

           self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
           self.qtTasarim.label_cikti.setScaledContents(True)
           
    def Yakinlastirma(self):
        if self.current_image_path:
            
           from PIL import Image
            
           GirisResmi = Image.open(self.current_image_path)
           ResimGenisligi, ResimYuksekligi = GirisResmi.size
           BuyultmeKatsayisi = int(self.qtTasarim.textEdit.toPlainText())

           # Çıkış resminin boyutlarını aşmamak için bu kod satırı yazıldı
           CikisResmi = Image.new("RGB", (ResimGenisligi * BuyultmeKatsayisi, ResimYuksekligi * BuyultmeKatsayisi))

           for x1 in range(ResimGenisligi):
               for y1 in range(ResimYuksekligi):
                   OkunanRenk = GirisResmi.getpixel((x1, y1))

                   for i in range(BuyultmeKatsayisi):
                       for j in range(BuyultmeKatsayisi):
                           x2 = x1 * BuyultmeKatsayisi + i
                           y2 = y1 * BuyultmeKatsayisi + j

                           # Koordinat sınırlarını kontrol et
                           if 0 <= x2 < ResimGenisligi * BuyultmeKatsayisi and 0 <= y2 < ResimYuksekligi * BuyultmeKatsayisi:
                               CikisResmi.putpixel((x2, y2), OkunanRenk)

           #CikisResmi.save("Buyultme.jpg")
           
           width, height = CikisResmi.size
           gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

           pixmap_gri = QPixmap.fromImage(gray_img_qimage)

           self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
           self.qtTasarim.label_cikti.setScaledContents(True)
           
    def Oteleme_Tasima(self):
        if self.current_image_path:
            
           from PIL import Image

           GirisResmi = Image.open(self.current_image_path)
           ResimGenisligi, ResimYuksekligi = GirisResmi.size
           CikisResmi = Image.new("RGB", (ResimGenisligi, ResimYuksekligi))

           # Taşıma mesafelerini atıyor.
           x_Tasima = int(self.qtTasarim.textEdit.toPlainText())
           y_Tasima = int(self.qtTasarim.textEdit_2.toPlainText())

           for x1 in range(ResimGenisligi):
               for y1 in range(ResimYuksekligi):
                   OkunanRenk = GirisResmi.getpixel((x1, y1))
                   x2 = x1 + x_Tasima
                   y2 = y1 + y_Tasima

                   # Koordinat sınırlarını kontrol et
                   if 0 <= x2 < ResimGenisligi and 0 <= y2 < ResimYuksekligi:
                       CikisResmi.putpixel((int(x2), int(y2)), OkunanRenk)

           #CikisResmi.save("Tasima.jpg")
           
           width, height = CikisResmi.size
           gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

           pixmap_gri = QPixmap.fromImage(gray_img_qimage)

           self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
           self.qtTasarim.label_cikti.setScaledContents(True)

    def Histogram(self):
        if self.current_image_path:
            
            from PIL import Image
            import matplotlib.pyplot as plt

            GirisResmi = Image.open(self.current_image_path)
            ResimGenisligi, ResimYuksekligi = GirisResmi.size

            # Histogram için gri-tona dönüştürüldü
            Piksel = []
            for y in range(ResimYuksekligi):
                for x in range(ResimGenisligi):
                    renk = GirisResmi.getpixel((x, y))
                    gri = renk[0]  # Sadece kırmızı kanalı alındı çünkü resim gri tonlu
                    Piksel.append(gri)

            # Renk sayımları
            DiziPikselSayilari = [0] * 256
            for piksel in Piksel:
                DiziPikselSayilari[piksel] += 1

            # Grafik çizme
            plt.bar(range(256), DiziPikselSayilari, color='black')
            plt.savefig('histogram.png')  # Grafiği dosyaya kaydet

            # Kaydedilen dosyayı tekrar yükleme
            CikisResmi = Image.open('histogram.png')

            width, height = CikisResmi.size
            gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)
            #gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_Grayscale8)
            pixmap_gri = QPixmap.fromImage(gray_img_qimage)

            self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
            self.qtTasarim.label_cikti.setScaledContents(True) 

    def Kontrast_Parlaklik_Ayari(self):
        if self.current_image_path:
            
            from PIL import Image

            R, G, B = 0, 0, 0
            GirisResmi1 = Image.open(self.current_image_path) 
            ResimEn, ResimBoy = GirisResmi1.size

            CikisResmi1 = Image.new("RGB", (ResimEn, ResimBoy))

            c_kontrast_seviyesi = float(self.qtTasarim.textEdit.toPlainText())
            ParlaklikDegeri = int(self.qtTasarim.textEdit_2.toPlainText())
            f_kontrast_faktoru = (259 * (c_kontrast_seviyesi + 255)) / (255 * (259 - c_kontrast_seviyesi))

            for x in range(ResimEn):
                for y in range(ResimBoy):
               
                    OkunanRenk = GirisResmi1.getpixel((x, y))
                    R, G, B = OkunanRenk[0], OkunanRenk[1], OkunanRenk[2]

                    R = int((f_kontrast_faktoru * (R - 128)) + 128)
                    G = int((f_kontrast_faktoru * (G - 128)) + 128)
                    B = int((f_kontrast_faktoru * (B - 128)) + 128)

                    R = min(255, max(0, R))
                    G = min(255, max(0, G))
                    B = min(255, max(0, B))

                    donusen_renk = (R, G, B)
                    CikisResmi1.putpixel((x, y), donusen_renk)

            CikisResmi1.save("kontrast.png")

            GirisResmi = Image.open("kontrast.png") 
            ResimGenisligi, ResimYuksekligi = GirisResmi.size

            CikisResmi = Image.new("RGB", (ResimGenisligi, ResimYuksekligi))  

            # Parlaklık Değeri Bu Satırdan Sonra Kullanıldı

            for x in range(ResimGenisligi):
                for y in range(ResimYuksekligi):
                    OkunanRenk = GirisResmi.getpixel((x, y))
                    R = OkunanRenk[0] + ParlaklikDegeri
                    G = OkunanRenk[1] + ParlaklikDegeri
                    B = OkunanRenk[2] + ParlaklikDegeri

            # EğerR,G,B değeri 255'i geçerse 255 olarak al. 
            # Çünkü çok yüksek parlaklık değeri girince "unexpected indent" bu hatayı veriyor.
                    if R > 255:
                        R = 255
                    if G > 255:
                        G = 255
                    if B > 255:
                        B = 255

                    DonusenRenk = (R, G, B)
                    CikisResmi.putpixel((x, y), DonusenRenk)

            #CikisResmi.save("Parlaklik_Karsitlik_Ayari.jpg")

            width, height = CikisResmi.size
            gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)
            pixmap_gri = QPixmap.fromImage(gray_img_qimage)

            self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
            self.qtTasarim.label_cikti.setScaledContents(True)     
            
    def Goruntu_Cevirme(self):
        if self.current_image_path:

           from PIL import Image, ImageDraw, ImageTk
           import math

           GirisResmi = Image.open(self.current_image_path)
           ResimGenisligi, ResimYuksekligi = GirisResmi.size
               
           angle =  int(self.qtTasarim.textEdit.toPlainText())
           radian_angle = math.radians(angle)
               
           CikisResmi = Image.new("RGB", (ResimGenisligi, ResimYuksekligi), color="white")
               
           center_x = ResimGenisligi // 2
           center_y = ResimYuksekligi // 2
               
           for x1 in range(ResimGenisligi):
               for y1 in range(ResimYuksekligi):

                   x2 = math.cos(radian_angle) * (x1 - center_x) - math.sin(radian_angle) * (y1 - center_y) + center_x
                   y2 = math.sin(radian_angle) * (x1 - center_x) + math.cos(radian_angle) * (y1 - center_y) + center_y
                       
                   if 0 < x2 < ResimGenisligi and 0 < y2 < ResimYuksekligi:
                       pixel_value = GirisResmi.getpixel((x1, y1))
                       CikisResmi.putpixel((int(x2), int(y2)), pixel_value)
               
           #CikisResmi.save("Goruntu_Cevirme.jpg")            
            

           width, height = CikisResmi.size
           gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)
           pixmap_gri = QPixmap.fromImage(gray_img_qimage)

           self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
           self.qtTasarim.label_cikti.setScaledContents(True)   
            
    def Konvolusyon_Yontemi_Cekirdek_Matrisi_Netlestirme(self):
        if self.current_image_path:

          from PIL import Image

          image = Image.open(self.current_image_path)
          ResimGenisligi, ResimYuksekligi = image.size
          SablonBoyutu = int(self.qtTasarim.textEdit.toPlainText())
          ElemanSayisi = SablonBoyutu * SablonBoyutu
          CikisResmi = Image.new("RGB", (ResimGenisligi, ResimYuksekligi))
          Matris = [0, -2, 0, -2, 11, -2, 0, -2, 0]
          MatrisToplami = sum(Matris)
              
          for x in range((SablonBoyutu - 1) // 2, ResimGenisligi - (SablonBoyutu - 1) // 2):
              for y in range((SablonBoyutu - 1) // 2, ResimYuksekligi - (SablonBoyutu - 1) // 2):
                  toplamR = toplamG = toplamB = 0
                  k = 0
                      
                  for i in range(-((SablonBoyutu - 1) // 2), (SablonBoyutu - 1) // 2 + 1):
                      for j in range(-((SablonBoyutu - 1) // 2), (SablonBoyutu - 1) // 2 + 1):
                          OkunanRenk = image.getpixel((x + i, y + j))
                          toplamR += OkunanRenk[0] * Matris[k]
                          toplamG += OkunanRenk[1] * Matris[k]
                          toplamB += OkunanRenk[2] * Matris[k]
                          k += 1
                      
                  R = max(0, min(255, toplamR // MatrisToplami))
                  G = max(0, min(255, toplamG // MatrisToplami))
                  B = max(0, min(255, toplamB // MatrisToplami))
                      
                  CikisResmi.putpixel((x, y), (R, G, B))
              
          #CikisResmi.save("konvolusyon_yontemi_ile_netlestirme.png")

          width, height = CikisResmi.size
          gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)
          pixmap_gri = QPixmap.fromImage(gray_img_qimage)

          self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
          self.qtTasarim.label_cikti.setScaledContents(True)            
            
    """def Laplacian(self):
        if self.current_image_path:
            
          GirisResmi = Image.open("manzara.jpg").convert('L')  # 'L' moduyla resmi gri tonlama dönüştür
          ResimEn, ResimBoy = GirisResmi.size

          CikisResmi = Image.new("L", (ResimEn, ResimBoy))

          # Laplacian filtre çekirdeği
          L_Filtre = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]

          # Filtreleme işlemi
          for x in range(1, ResimEn - 1):
              for y in range(1, ResimBoy - 1):
                  # Çekirdek matrisi ile piksel komşularının ağırlıklı toplamını hesapla
                  result = 0
                  for i in range(3):
                      for j in range(3):
                              result += GirisResmi.getpixel((x - 1 + i, y - 1 + j)) * L_Filtre[i][j]

                  # Elde edilen değeri yeni görüntüye ata (ve sınırları kontrol et)
                  CikisResmi.putpixel((x, y), int(result))

          # Çıkış resmini kaydet
          CikisResmi.save("Laplacian.png")

          width, height = CikisResmi.size
          gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)

          pixmap_gri = QPixmap.fromImage(gray_img_qimage)

          self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
          self.qtTasarim.label_cikti.setScaledContents(True)"""           

    def Histogram_Esitleme(self):
        if self.current_image_path:

          from PIL import Image

          resim = Image.open(self.current_image_path)
          genislik, yukseklik = resim.size

          # Histogram hesaplama
          histogram = [0] * 256
          for y in range(yukseklik):
              for x in range(genislik):
                  piksel = resim.getpixel((x, y))
                  gri_deger = int(sum(piksel) / 3)  # Renkli resimse ortalama al
                  histogram[gri_deger] += 1

          # Kumulatif histogram hesaplama
          kumulatif_histogram = [sum(histogram[:i+1]) for i in range(256)]

          # Piksel değerlerini eşitleme
          faktor = 255.0 / (genislik * yukseklik)
          CikisResmi = Image.new("RGB", (genislik, yukseklik))

          for y in range(yukseklik):
              for x in range(genislik):
                  piksel = resim.getpixel((x, y))
                  gri_deger = int(sum(piksel) / 3)  # Renkli resimse ortalama al
                  yeni_gri_deger = int(kumulatif_histogram[gri_deger] * faktor)
                  yeni_piksel = (yeni_gri_deger, yeni_gri_deger, yeni_gri_deger)
                  CikisResmi.putpixel((x, y), yeni_piksel)

          # Eşitlenmiş histogramı gösterme
          #CikisResmi.save("Histogram_Esitleme.png")

          width, height = CikisResmi.size
          gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)
          pixmap_gri = QPixmap.fromImage(gray_img_qimage)

          self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
          self.qtTasarim.label_cikti.setScaledContents(True)                        

    def Gradyent(self):
        if self.current_image_path:

          from PIL import Image

          import numpy as np
          import matplotlib.pyplot as plt

          def sobel_operatörü(img):
              
              # Sobel operatörü çekirdekleri
              kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
              kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

              # Görüntü boyutları
              Satir, Sutun = img.shape

              # Gradyan hesaplamaları
              gradyan_x = np.zeros_like(img, dtype=np.float64)
              gradyan_y = np.zeros_like(img, dtype=np.float64)

              for i in range(1, Satir-1):
                  for j in range(1, Sutun-1):
                      gradyan_x[i, j] = np.sum(img[i-1:i+2, j-1:j+2] * kernel_x)
                      gradyan_y[i, j] = np.sum(img[i-1:i+2, j-1:j+2] * kernel_y)

              gradyan = np.sqrt(gradyan_x**2 + gradyan_y**2)

              return gradyan
         
              
          # Görüntüyü oku ve gri tonlamaya dönüştür
          Resim = plt.imread(self.current_image_path)
          GriResim = np.mean(Resim, axis=-1)

          # Gradyanları hesapla
          gradyanlari_hesapla = sobel_operatörü(GriResim)

          # Elde edilen gradyanları görselleştir
          plt.imshow(gradyanlari_hesapla, cmap='gray')
          plt.axis('off')
          plt.savefig('keskin.png')

          CikisResmi = Image.open('keskin.png')

          width, height = CikisResmi.size
          gray_img_qimage = QImage(CikisResmi.tobytes(), width, height, QImage.Format_RGB888)
          pixmap_gri = QPixmap.fromImage(gray_img_qimage)

          self.qtTasarim.label_cikti.setPixmap(pixmap_gri)
          self.qtTasarim.label_cikti.setScaledContents(True)

          
                                              
if __name__ == "__main__":
    app = QApplication([])
    pencere = main()
    pencere.show()
    app.exec_()