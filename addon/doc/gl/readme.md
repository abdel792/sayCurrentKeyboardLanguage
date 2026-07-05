# sayCurrentKeyboardLanguage

* Autor(es): Abdel, Noelia.

# Presentación #

Este complemento foi creado a petición dun membro da lista de correo de complementos de nvda.

Ofrece un script sen xesto asignado, que permite obter e dar o idioma do teclado actual.

Se se preme dúas veces, dá o idioma por defecto do sistema.

Na primeira versión deste módulo, propúxose como un simple globalPlugin para colar no directorio de configuración de NVDA, despois transformouse en complemento.

## Notas ##

Para asignar un xesto ao script que dá o idioma do teclado, segue estes pasos:

* Abre o menú de NVDA con "NVDA + N";
* Vai ao menú de preferencias de NVDA;
* Despois vai ao submenú "Xestos de entrada".
* Logo selecciona a categoría "Entrada", e ábrea coa frecha dereita.
* Vai ao elemento etiquetado como "Dá o idioma do teclado en uso, se se preme dúas veces, dá o idioma por defecto do sistema";
* Unha vez feito isto, preme Alt + A para engadir un xesto, e escribe "NVDA + F4" ou outro xesto da túa elección;
* Feito isto, preme a frecha arriba unha vez, escoitarás "o teu xesto elixido, todas as disposicións";
* Valida con Intro, despois vai con Tab ata Aceptar e preme Intro;
* O xesto elixido debería entón chamar ao script que dá o idioma do teclado.

## Compatibilidade ##

* Este complemento é compatible coas versións de NVDA que van dende a 2019.3 en diante.

## Cambios para 20240326.0.0

* Compatibilidade actualizada para nvda-2024.1;
* Eliminouse a ligazón de descarga do readme, a ligazón de descarga para futuras actualizacións agora só estará dispoñible desde a tenda de complementos.

## Cambios para 20231229.0.0 ##

* Engadiuse unha implementación compatible con versións anteriores para admitir o modo de voz baixo demanda, que pronto estará dispoñible con nvda-2024.1.

## Cambios para 20230729.0.0 ##

* Aplicáronse as regras de flake8 e mypy ao código;
* Cambiouse a versión mínima de NVDA soportada a 2019.3 para admitir as anotacións introducidas en Python 3.
* Eliminouse o xesto "NVDA + F4" que chamaba ao script que dá o idioma do teclado, para permitir aos usuarios elixir o seu xesto preferido.

## Cambios para 20230607.0.0 ##

* Engadíronse os seguintes fluxos de traballo:
 * auto-update-translations - para actualizar automaticamente as traducións desde o sistema de tradución de NVDA.
 * release-on-tag..yaml: para construír e publicar o complemento tan pronto como se envíe unha nova etiqueta;
 * manual-release.yaml: para construír e lanzar novas versións do complemento manualmente.
* Traducións actualizadas.

## Cambios para a versión 20230426.0.0 e posteriores ##

* • Cambiouse o número de versión, a versión mínima de NVDA e a ligazón de descarga de acordo coas convencións/requisitos da tenda.

## Cambios para a versión 19.02 ##

* Cambiouse a numeración das versións usando AA.MM (O ano en 2 díxitos, seguido dun punto, seguido do mes en 2 díxitos);
* Engadiuse compatibilidade co novo formato de versión dos complementos, aparecido desde nvda 2019.1.

## Cambios para a versión 1.1 ##

* O complemento foi renomeado de getCurKeyboardLanguage a sayCurrentKeyboardLanguage;
* Engadiuse a licenza GPL ao complemento;
* Engadiuse o script getCurKeyboardLanguage á categoría "Estado do sistema";
* Corrixíronse algúns erros no código.

## Cambios para a versión 1.0 ##

* Versión inicial.
