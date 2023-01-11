import cv2
#Cargo la imagen que voy a analizar
img=cv2.imread('contorno.jpg')
#Combierto a escala de grises la imagen 
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Obtengo el umbral
__,umbral=cv2.threshold(grey,100,255,cv2.THRESH_BINARY)
#obtengo los contornos
contorno,jerarquia=cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
#dibujo los contornos
cv2.drawContours(img,contorno,-1,(65,105,225),3)
#Muestrar
cv2.imshow('imagen',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 