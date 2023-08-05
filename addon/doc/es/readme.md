# sayCurrentKeyboardLanguage #

* Autor(es): Abdel, Noelia;
* Descargar [versión
  estable](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* Descargar [versión de
  desarrollo](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

# Presentación #

Este complemento fue creado atendiendo a una petición de un miembro de la
lista de correo nvda-addons.

Proporciona un atajo de teclado, sin asignar, el cual permite recuperar y
dar el idioma del teclado actual.

Si se pulsa dos veces, devuelve el idioma por defecto del sistema.

En la primera versión de este módulo, se había propuesto como un simple
plugin global para pegar en el directorio de configuración de NVDA, Entonces
se transformó en un complemento.

## Notas ##

Para configurar un gesto para el script que da el idioma del teclado, sigue
estos pasos:

* Abre el menú de NVDA con "NVDA+n";
* Ve al menú Preferencias de NVDA;
* Después ve al submenú "Gestos de entrada".
* Después selecciona la categoría "Entrada", y ábrela con la flecha derecha.
* Ve al elemento etiquetado como "Indica el idioma de teclado en uso. Si se
  pulsa dos veces, indica el idioma por defecto del sistema";
* A continuación, pulsa alt+a para añadir un gesto, y pulsa "NVDA+f4" o
  cualquier otro gesto que prefieras;
* Después, pulsa flecha arriba una vez. Escucharás "El gesto elegido, todas
  las distribuciones";
* Valida pulsando intro, luego tabula hasta Aceptar e intro;
* Tu gesto elegido debería así llamar al script que dice el idioma del
  teclado.

## Compatibilidad ##

* Este complemento es compatible con las versiones de NVDA que van de la
  2019.3 en adelante.

## Cambios para 20230729.0.0 ##

* Aplicadas las reglas de Flake8 y Mipy al código;
* Cambiada la versión mínima soportada de NVDA a la 2019.3 para soportar las
  anotaciones de tipos introducidas en Python 3.
* Se ha eliminado el gesto que llamaba al script que decía el idioma del
  teclado, "NVDA+f4". Esto permite que los usuarios elijan su propio gesto.

## Cambios para la versión 20230426.0.0 y posteriores##

* Modificado el número de versión, la versión mínima de NVDA y el enlace de
  descarga según las convenciones y requisitos de la tienda.

## Cambios para la versión 19.02 ##

* Se ha cambiado la numeración de versión siguiendo el esquema AA.MM (dos
  dígitos para el año seguidos de un punto y dos dígitos para el mes);
* Se ha añadido compatibilidad con el nuevo formato de versión de
  complementos introducido en NVDA 2019.1.

## Cambios para la versión 1.1 ##

* El complemento se ha renombrado de getCurKeyboardLanguage a
  sayCurrentKeyboardLanguage;
* Añadida la licencia GPL al complemento;
* Añadido el script getCurKeyboardLanguage a la categoría "Estado de
  Sistema";
* Corregidos algunos errores en el código.

## Cambios para la versión 1.0 ##

* Versión inicial.

[[!tag dev stable]]
