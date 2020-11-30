# Sistema de Televigilancia

Este repositorio cuenta con tres directorios principales. Uno de ellos es el meta-proyecto2, el cual tiene adentro las
receta del código fuente de reconocimiento de objetos, asi como los modelos de entrenamiento. Además cuenta con layer 
de configuración de la receta.

El segundo directorio es la carpeta de construcción o build llamada  rpi2. Esta tiene adentro los archivos de configuración
necesarios, así como las dependecias que se necesitan para la generación de una imagen personalizada utilizando el flujo 
del Yocto Project para un "target" de raspberrypi2.

El tercer archivo es la interfaz de usuario para el control de la aplicación en python3.

Se necesitan seguir los siguientes pasos si se desea hacer uso de este repositorio:

	1. Clonar poky-warrior: git clone -b warrior git://git.yoctoproject.org/poky.git
	2. Clonar el repositorio de meta-raspberry dentro de la carpeta poky-warrior: git clole -b warrior git://git.yoctoproject.org/meta-raspberrypi
	3. Clonar el master de este repositorio dentro de la carpeta poky-warrior y al mismo nivel de meta-raspberrypi: git clone https://github.com/kendallguido/Proyecto2_Embebidos.git 
	4. Abrir una terminal dentro de carpeta poky-warrior y ejecutar el siguiente comando: source oe-init-build-env rpi2/
	5. Ejecutar el comando: bitbake core-image-sato

Nota: Se deben hacer los cambios pertinentes al archivo bblayers dentro de la carpeta conf con las direcciones absolutas de las carpetas de los layers.
