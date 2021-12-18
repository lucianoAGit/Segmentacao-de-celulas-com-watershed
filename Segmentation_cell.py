import cv2
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import os

# Carrega todos os arquivos .bmp da pasta
img_names = glob(os.path.join(os.getcwd(), '*.bmp'))

for fn in img_names:

    img = cv2.imread(fn)
    
    # Converte para escala de cinza e aplica um treshold com limiares definidos
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,70,255,cv2.THRESH_BINARY_INV)

    # Aplicacao de operacoes morfologicas
    kernel = np.ones((5,5),np.uint8)
    fg_2 = cv2.erode(thresh,kernel,iterations = 10)
    fg = cv2.dilate(fg_2,kernel,iterations = 18)
  
    # Geracao do background
    bgt = cv2.dilate(thresh,None,iterations = 3)
    ret,bg = cv2.threshold(bgt,1,128,1)
    
    # Marker
    marker = cv2.add(fg,bg)
    marker32 = np.int32(marker)
    
    # Aplicacao watershed
    cv2.watershed(img,marker32)
    m = cv2.convertScaleAbs(marker32)

    # Geracao do resultado da segmentacao
    ret,thresh = cv2.threshold(m,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    res = cv2.bitwise_and(img,img,mask = thresh)
    #plt.imshow(res)
    #plt.show()
    
    # Salvar imagem resultante no diretorio
    cv2.imwrite('SEG_'+str(os.path.basename(fn)), res)

