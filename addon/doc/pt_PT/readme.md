# sayCurrentKeyboardLanguage

* Autor(es): Abdel, Noelia.

# Apresentação #

Este suplemento foi criado na sequência de um pedido de um membro da lista de discussão nvda-addons.

Fornece um script sem gesto, que permite obter e ditar o idioma do teclado atual.

Se for pressionado duas vezes, dita o idioma predefinido do sistema.

Na primeira violentado deste módulo, ele tinha sido proposto como um simples globalPlugin para colar no diretório de configuração do NVDA, tendo sido posteriormente transformado em suplemento.

## Notas ##

Para definir um gesto para o script que dita o idioma do teclado, siga estes passos:

* Abra o menu do NVDA, com "NVDA + N";
* Vá ao menu de preferências do NVDA;
* Em seguida, vai ao submenu "Gestos de entrada".
* Depois selecione a categoria "Introdução", e abra-a com a seta para a direita.
* Vá para o item rotulado "Dita o idioma do teclado em uso, se pressionado duas vezes, dá o idioma padrão do sistema";
* Feito isto, pressione Alt + A para adicionar um gesto, e digite "NVDA + F4" ou outro gesto da sua escolha;
* Feito isso, pressione a seta para cima uma vez, ouvirá "o seu gesto escolhido, todos os esquemas";
* Valide com Enter, depois use o Tab até OK e pressione Enter;
* O gesto escolhido deverá então chamar o script que dita o idioma do teclado.

## Compatibilidade ##

* Este suplemento é compatible com as versões do NVDA desde a 2019.3 e posteriores.

## Alterações para 20240326.0.0

* Compatibilidade atualizada para nvda-2024.1;
* Eliminada a hiperligação de transferência do readme, a hiperligação de transferência para atualizações futuras estará agora apenas disponível na loja de suplementos.

## Alterações para 20231229.0.0 ##

* Adicionada uma implementação retrocompatível para suportar o modo de fala sob demanda, que estará brevemente disponível com o nvda-2024.1.

## Alterações para 20230729.0.0 ##

* Aplicadas as regras flake8 e mypy ao código;
* Alterada a versão mínima do NVDA suportada para 2019.3 para suportar anotações introduzidas no Python 3.
* Removido o gesto "NVDA + F4" que chamava o script que dita o idioma do teclado, para permitir que os utilizadores escolham o seu gesto preferido.

## Alterações para 20230607.0.0 ##

* Adicionados os seguintes fluxos de trabalho:
 * auto-update-translations - para atualizar automaticamente as traduções a partir do sistema de tradução do NVDA.
 * release-on-tag..yaml: para compilar e publicar o suplemento assim que uma nova etiqueta for enviada;
 * manual-release.yaml: para compilar e lançar novas versões do suplemento manualmente.
* Traduções atualizadas.

## Alterações para a versão 20230426.0.0 e posteriores ##

* • Alterado o número da versão, versão mínima do NVDA e hiperligação de transferência de acordo com as convenções/requisitos da loja.

## Alterações para a versão 19.02 ##

* Alterada a numeração das versões utilizando AA.MM (O ano em 2 dígitos, seguido de um ponto, seguido do mês em 2 dígitos);
* Adicionada compatibilidade com o novo formato de numeração de versões de suplementos, surgido desde o nvda 2019.1.

## Alterações para a versão 1.1 ##

* O suplemento foi renomeado de getCurKeyboardLanguage para sayCurrentKeyboardLanguage;
* Adicionada a licença GPL ao suplemento;
* Adicionado o script getCurKeyboardLanguage à categoria "Estado do sistema";
* Corrigidos alguns erros no código.

## Alterações para a versão 1.0 ##

* Versão inicial.
