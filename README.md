# contador_de_monedas
Proyecto con openCV y python, que cuenta las monedas en una imagen estática.
El archivo "contornos.py" contiene los primeros pasos para la detección de contornos y familiarización con la libreria.
En el archivo "contador_monedas.py" realizo los pasos para eliminar el ruido de una imagen y para su posterior procesado.
  *primero, convierto la imagen a escala de grises.
  *segundo, aplica gauss blur para realizar un suavizado o desenfoque.
  *tercero, aplico canny para reducir aun más el ruido de la imagen.
    **en la matriz kernel utilizo numpy para obtener una matriz cuadrada de enteros de 8 bits, esto es para evitar que salgan otro tipos de valores numericos.
  *cuarto, aplicamos una transformación morfologica de clausura 
  *quinto, obtengo los contornos y sus jerarquias.
	**verifico la cantidad de contornos sea correcta si no ajustos parametros de los pasos anterioresya que estos dependen del ruido que tenga la imagen.
