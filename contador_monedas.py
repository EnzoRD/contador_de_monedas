import  cv2
import numpy as np
#Cargo la imagen
orig = cv2.imread("monedassoles.jpg")
#paso la imagen a escala de grises para implementar los metodoes es necesario
en_gris = cv2.cvtColor(orig,cv2.COLOR_BGR2GRAY)

#implementación del modelado GaussianBlur para suavizado de imagen, siempre valores iumpares
var_gauss = 1
var_kernel = 33

#desenfoque con gaussian blur, siempre es una matriz cuadrada
suavizado = cv2.GaussianBlur(en_gris, (var_gauss,var_gauss), 0)

#encuentro los bordes con canny
canny = cv2.Canny(suavizado,60,100)

#matriz de enteros de  8 byts y realizo una transformación morfologica de clausura 
kernel = np.ones((var_kernel,var_kernel), np.uint8)
clausura = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

contornos,jerarquia = cv2.findContours(clausura.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("monedas encontradas: {}".format(len(contornos)))
cv2.drawContours(orig, contornos, -1, (0,0,255), 2)
#Resultado
cv2.imshow("grises",en_gris)
cv2.imshow("gauss",canny)
cv2.imshow("resultado final", orig)
cv2.waitKey(0)