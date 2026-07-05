# sayCurrentKeyboardLanguage

* Autor(es): Abdel, Noelia.

# Presentación #

Este complemento fue creado a petición de un miembro de la lista de correo de complementos de nvda.

Proporciona un script sin gesto, que permite recuperar y dar el idioma del teclado actual.

Si se presiona dos veces, da el idioma por defecto del sistema.

En la primera versión de este módulo, se había propuesto como un simple globalPlugin para pegar en el directorio de configuración de NVDA, luego se transformó en complemento.

## Notas ##

Para asignar un gesto al script que da el idioma del teclado, sigue estos pasos:

* Abre el menú de NVDA con "NVDA + N";
* Ve al menú de preferencias de NVDA;
* Luego ve al submenú "Gestos de entrada".
* Después selecciona la categoría "Entrada", y ábrela con la flecha derecha.
* Ve al elemento etiquetado como "Da el idioma del teclado en uso, si se presiona dos veces, da el idioma por defecto del sistema";
* Una vez hecho esto, presiona Alt + A para añadir un gesto, y escribe "NVDA + F4" u otro gesto de tu elección;
* Hecho esto, presiona la flecha arriba una vez, escucharás "tu gesto elegido, todas las disposiciones";
* Valida con Enter, luego ve con Tab hasta Aceptar y presiona Enter;
* El gesto elegido debería entonces llamar al script que da el idioma del teclado.

## Compatibilidad ##

* Este complemento es compatible con las versiones de NVDA que van desde la 2019.3 en adelante.

## Cambios para 20240326.0.0

* Compatibilidad actualizada para nvda-2024.1;
* Se eliminó el enlace de descarga del readme, el enlace de descarga para futuras actualizaciones ahora solo estará disponible desde la tienda de complementos.

## Cambios para 20231229.0.0 ##

* Se añadió una implementación compatible con versiones anteriores para admitir el modo de voz bajo demanda, que pronto estará disponible con nvda-2024.1.

## Cambios para 20230729.0.0 ##

* Se aplicaron las reglas de flake8 y mypy al código;
* Se cambió la versión mínima de NVDA soportada a 2019.3 para admitir las anotaciones introducidas en Python 3.
* Se eliminó el gesto "NVDA + F4" que llamaba al script que da el idioma del teclado, para permitir a los usuarios elegir su gesto preferido.

## Cambios para 20230607.0.0 ##

* Se añadieron los siguientes flujos de trabajo:
 * auto-update-translations - para actualizar automáticamente las traducciones desde el sistema de traducción de NVDA.
 * release-on-tag..yaml: para construir y publicar el complemento tan pronto como se envíe una nueva etiqueta;
 * manual-release.yaml: para construir y lanzar nuevas versiones del complemento manualmente.
* Traducciones actualizadas.

## Cambios para la versión 20230426.0.0 y posteriores ##

* • Se cambió el número de versión, la versión mínima de NVDA y el enlace de descarga de acuerdo con las convenciones/requisitos de la tienda.

## Cambios para la versión 19.02 ##

* Se cambió la numeración de las versiones usando AA.MM (El año en 2 dígitos, seguido de un punto, seguido del mes en 2 dígitos);
* Se añadió compatibilidad con el nuevo formato de versión de los complementos, aparecido desde nvda 2019.1.

## Cambios para la versión 1.1 ##

* El complemento ha sido renombrado de getCurKeyboardLanguage a sayCurrentKeyboardLanguage;
* Se añadió la licencia GPL al complemento;
* Se añadió el script getCurKeyboardLanguage a la categoría "Estado del sistema";
* Se corrigieron algunos errores en el código.

## Cambios para la versión 1.0 ##

* Versión inicial.
