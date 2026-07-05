# sayCurrentKeyboardLanguage

* Autor(es): Abdel, Noelia.

# Apresentação #

Este complemento foi criado a pedido de um membro da lista de discussão nvda-addons.

Ele fornece um script sem gesto, que permite recuperar e anunciar o idioma do teclado atual.

Se pressionado duas vezes, informa o idioma padrão do sistema.

Na primeira versão deste módulo, ele havia sido proposto como um simples globalPlugin para colar no diretório de configuração do NVDA, sendo posteriormente transformado em complemento.

## Notas ##

Para definir um gesto para o script que informa o idioma do teclado, siga estas etapas:

* Abra o menu do NVDA, com "NVDA + N";
* Vá para o menu de preferências do NVDA;
* Em seguida, vá para o submenu "Gestos de entrada".
* Depois selecione a categoria "Entrada" e abra-a com a seta para a direita.
* Vá para o item rotulado "Informa o idioma do teclado em uso, se pressionado duas vezes, informa o idioma padrão do sistema";
* Feito isso, pressione Alt + A para adicionar um gesto e digite "NVDA + F4" ou outro gesto de sua escolha;
* Feito isso, pressione a seta para cima uma vez, você ouvirá "o gesto escolhido, todos os layouts";
* Confirme com Enter, depois use o Tab até OK e pressione Enter;
* O gesto escolhido deverá então chamar o script que informa o idioma do teclado.

## Compatibilidade ##

* Este complemento é compatível com as versões do NVDA que vão de 2019.3 em diante.

## Alterações para 20240326.0.0

* Compatibilidade atualizada para nvda-2024.1;
* Link de download removido do readme, o link de download para atualizações futuras agora estará disponível apenas na loja de complementos.

## Alterações para 20231229.0.0 ##

* Adicionada uma implementação retrocompatível para suportar o modo de fala sob demanda, que estará disponível em breve com o nvda-2024.1.

## Alterações para 20230729.0.0 ##

* Aplicadas as regras do flake8 e mypy ao código;
* Alterada a versão mínima do NVDA suportada para 2019.3 para suportar anotações introduzidas no Python 3.
* Removido o gesto "NVDA + F4" que chamava o script que informa o idioma do teclado, para permitir que os usuários escolham seu gesto preferido.

## Alterações para 20230607.0.0 ##

* Adicionados os seguintes fluxos de trabalho:
 * auto-update-translations - para atualizar automaticamente as traduções a partir do sistema de tradução do NVDA.
 * release-on-tag..yaml: para construir e publicar o complemento assim que uma nova tag for enviada;
 * manual-release.yaml: para construir e lançar novas versões do complemento manualmente.
* Traduções atualizadas.

## Alterações para a versão 20230426.0.0 e posteriores ##

* • Alterado o número da versão, versão mínima do NVDA e link de download de acordo com as convenções/requisitos da loja.

## Alterações para a versão 19.02 ##

* Alterada a numeração das versões utilizando AA.MM (O ano em 2 dígitos, seguido de um ponto, seguido do mês em 2 dígitos);
* Adicionada compatibilidade com o novo formato de numeração de versões de complementos, surgido desde o nvda 2019.1.

## Alterações para a versão 1.1 ##

* O complemento foi renomeado de getCurKeyboardLanguage para sayCurrentKeyboardLanguage;
* Adicionada a licença GPL ao complemento;
* Adicionado o script getCurKeyboardLanguage à categoria "Status do sistema";
* Corrigidos alguns erros no código.

## Alterações para a versão 1.0 ##

* Versão inicial.
