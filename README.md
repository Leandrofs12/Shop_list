# 🛒 Gerenciador de Lista de Compras

Um aplicativo de linha de comando (CLI) simples e eficiente, desenvolvido em Python, para gerenciar listas de compras. O projeto permite adicionar, visualizar, remover e salvar os itens de forma persistente.

## 🚀 Funcionalidades

O script apresenta um menu interativo com as seguintes opções:

1. **Adicionar:** Insere novos itens na lista de compras.
2. **Listar:** Exibe todos os itens atualmente cadastrados.
3. **Remover:** Deleta um item específico da lista.
4. **Sair e Salvar:** Salva todas as alterações feitas e encerra a aplicação com segurança.

## 📁 Arquitetura do Projeto

O código foi modularizado para facilitar a manutenção e a leitura, dividindo as responsabilidades da seguinte forma:

* **`main.py`** (ou arquivo principal): Contém o loop do menu principal e a interface com o usuário.
* **`core.py`**: Responsável pela persistência dos dados, contendo as funções de leitura (`carregar_itens`) e gravação (`salvar_itens`).
* **`functions.py`**: Contém a lógica de negócio do aplicativo, com as funções operacionais (`adicionar_item`, `exibir_lista`, `remover_item`).

## 💻 Como executar

Certifique-se de ter o Python instalado em sua máquina. Para iniciar o programa, basta rodar o arquivo principal no terminal:

```bash
python nome_do_seu_arquivo_principal.py
