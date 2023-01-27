# contador_de_monedas
Proyecto contador de monedas, imagen estática, con openCV en python 
el archivo contornos es la familiarización con la detección de contornos 
en el archivo contador_monedas realizo los pasos de eliminar el ruido de una imagen
  primero, convierto la imagen a escala de grises
  segundo, aplica gauss blur para realizar un suavizado o desenfoque
  tercero, aplico canny para reducir aun más el ruido de la imagen
    en la matriz kernel utilizo numpy para obtener una matriz de enteros de 8 bits, esto es para evitar que salgan otro tipos de valores numericos 
  cuarto, aplicamos una transformación morfologica de clausura 
  quinto, obtengo los contornos y sus jerarquias. verifico la cantidad de contornos sea correcta si no ajustos parametros de los pasos anteriores
    ya que estos dependen del ruido que tenga la imagen
