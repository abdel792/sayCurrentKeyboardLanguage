# Dizer o Idioma Atual do Teclado (sayCurrentKeyboardLanguage) #

* Autores(es): Abdel, Noelia.

# Apresentação #

Este complemento foi criado após uma solicitação de um membro da lista de
discussão nvda-addons.

Ele fornece um script sem gestos, que permite recuperar e fornecer o idioma
do teclado atual.

Se pressionado duas vezes, fornece o idioma padrão do sistema.

Na primeira versão deste módulo, foi proposto como simples plug-in global
(globalPlugin) para colar no diretório de configuração do NVDA, depois foi
transformado em complemento (add-on).

## Notas ##

Para definir um gesto para o script que fornece o idioma do teclado, siga
estas etapas:

* Abra o menu do NVDA com “NVDA + N”;
* Acesse o menu de preferências do NVDA;
* Em seguida, vá para o submenu “Gestos de entrada".
* Em seguida, selecione a categoria “Entrada" e abra-a com a seta para a
  direita.
* Vá para o item denominado “Fornece o idioma do teclado em uso, se
  pressionado duas vezes, fornece o idioma padrão do sistema”;
* Depois disso, pressione Alt + A para adicionar um gesto e digite “NVDA +
  F4” ou outro gesto de sua escolha;
* Feito isso, pressione a seta para cima uma vez e você ouvirá “seu gesto
  escolhido, todo o layout”;
* Valide ao inserir, depois pressione a guia para OK e, em seguida, insira;
* O gesto escolhido deve chamar o script que fornece o idioma do teclado.

## Compatibilidade ##

* Esse complemento é compatível com as versões do NVDA a partir da versão
  2019.3.

## Mudanças na versão 20240326.0.0

* Compatibilidade atualizada para nvda-2024.1;
* Link de download excluído do readme, agora  as futuras atualizações só
  estará disponível na loja de complementos.

## Mudanças na versão 20231229.0.0 ##

* Adicionada uma implementação compatível com versões anteriores para
  oferecer suporte ao modo falar sob demanda, que em breve estará disponível
  com o nvda-2024.1.

## Mudanças na versão 20230729.0.0 ##

* Aplicou as regras flake8 e mypy ao código;
* Alterada a versão mínima suportada do NVDA para 2019.3 para suportar
  anotações introduzidas no Python 3.
* Removido o gesto “NVDA + F4” que chama o script que fornece o idioma do
  teclado, para permitir que os usuários escolham o gesto de sua
  preferência.

## Mudanças na versão 20230426.0.0 e além##

* O número da versão, a versão mínima do NVDA e o link de download foram
  alterados de acordo com as convenções/requisitos da loja.

## Mudanças na versão 19.02 ##

* Numeração de versão alterada usando AA.MM (o ano em 2 dígitos, seguido de
  um ponto, seguido do mês em 2 dígitos);
* Adicionado compatibilidade com o novo formato de versão do complemento,
  surgido desde o nvda 2019.1.

## Mudanças na versão 1.1 ##

* O complemento foi renomeado de ObtenhaIdioma Atual do Teclado para
  (DizerIdioma Atual do Teclado);
* Adicionada a licença GPL ao complemento;
* Adicionado o script getCurKeyboardLanguage à categoria "Status do
  sistema";
* Corrigido alguns erros no código.

## Mudanças na versão 1.0 ##

* Versão inicial.

[[!tag dev stable]]
