# 🛒 Gerenciador de Lista de Compras (Python CLI)

Este é um projeto de terminal desenvolvido em Python para gerenciar listas de compras de forma persistente e organizada. O sistema permite o controle de itens e suas respectivas quantidades, salvando os dados automaticamente em um arquivo de texto.

## ⚙️ Funcionalidades

- **Adicionar Itens:** Permite inserir o nome do produto e a quantidade (salvos no formato `Item (Quantidade)`).
- **Listagem Dinâmica:** Exibe os itens numerados para fácil identificação.
- **Remoção por Índice:** Permite remover produtos informando apenas o número correspondente na lista.
- **Persistência de Dados:** Os dados são carregados de um arquivo `lista_compras.txt` ao iniciar e salvos ao fechar o programa.
- **Tratamento de Erros:** Sistema protegido contra entradas inválidas e arquivos inexistentes.

## 📁 Estrutura de Arquivos

O projeto está dividido em três módulos principais:

1.  **`main.py`**: O ponto de entrada que gerencia o loop do menu principal.
2.  **`core.py`**: Responsável pela Manipulação de Arquivos (Leitura e Escrita).
    - `carregar_itens()`
    - `salvar_itens()`
3.  **`functions.py`**: Contém a Lógica de Negócio.
    - `adicionar_item()`
    - `exibir_lista()`
    - `remover_item()`

## 🚀 Como Utilizar

1. Certifique-se de ter o Python instalado.
2. Salve os módulos em seus respectivos arquivos.
3. Execute o comando:
   ```bash
   python main.py
   ---

### Simulação do Fluxo da Lista

Para ajudar a entender como o Python manipula essa lista internamente entre os módulos `functions` e `core`, criei este simulador que replica a lógica do seu código:

```json?chameleon
{"component":"LlmGeneratedComponent","props":{"height":"600px","prompt":"Crie um simulador interativo de Lista de Compras que replica a lógica do script Python fornecido. \n\nObjetivo: Demonstrar as operações de CRUD (Criar, Ler, Atualizar, Deletar) e como o formato 'Item (Qtd)' funciona.\n\nEstrutura visual:\n1. Uma área central exibindo a 'Lista Atual' (estilizada como uma lista de papel ou quadro).\n2. Controles de entrada: Campo para 'Nome do Produto' e 'Quantidade'.\n3. Botões de ação: 'Adicionar Item', 'Limpar Tudo' e botões de 'Remover' individuais ao lado de cada item.\n\nComportamento:\n- Ao adicionar, o item deve aparecer no formato 'Produto (Quantidade)'.\n- Deve haver uma simulação de 'Status de Salvamento': quando um item é adicionado ou removido, mostre uma pequena mensagem de 'Ação Realizada' (ex: '❌ removido!' ou '✔ Item adicionado!'), assim como no print do código Python.\n- Se a lista estiver vazia, exibir 'A lista está vazia' no centro.\n\nInteração:\n- Destaque visualmente o item quando o mouse passar por cima para simular a seleção para remoção.\n- Exiba o contador de itens no topo.","id":"im_954d074c05055183"}}
