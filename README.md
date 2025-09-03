# 🐍 Primeira Aplicação Front-end em Python com PyQt5

Este projeto foi desenvolvido como **conteúdo visto em sala de aula**, com o objetivo de aprender e praticar conceitos básicos de criação de interfaces gráficas utilizando **PyQt5**.

---

## 📚 Sobre o Projeto (Fase 1)
O código cria uma janela interativa em Python com botões, rótulo (label) e estilos personalizados definidos via arquivo externo **QSS**.  
Foi utilizado o **PyQt5**, uma biblioteca popular para desenvolvimento de GUIs em Python, explorando:

- Criação de janelas (`QWidget`)
- Uso de layouts (`QVBoxLayout`, `QHBoxLayout`)
- Botões interativos (`QPushButton`)
- Estilização externa com **QSS**
- Eventos com `clicked.connect()`

---

## 🖥️ Demonstração (Fase 1)

A aplicação exibe uma janela com:
- Um rótulo com a mensagem **"Hello World!"**.
- Três botões personalizados (`Clique aqui!`, `Meow`, `Woof`).
- Evento que imprime no terminal quando o botão "Clique aqui!" é pressionado.
- Criação de telas pelo **Designer**.
- Adicionado conexão com Banco de dados para inserimento e dados pelo Python.

---

# 📒 Evolução do Projeto – Agenda com PyQt5 e MySQL (Fase 2)

Na segunda parte da atividade, o projeto foi evoluído para uma **Agenda de Contatos**, integrando **PyQt5** com banco de dados **MySQL**.

---

## 📚 Sobre o Projeto (Fase 2)
A aplicação implementa uma **agenda de contatos** com interface gráfica construída no **Qt Designer** e carregada no Python via `uic.loadUi`.  
O sistema permite **cadastrar contatos** e **consultar registros** armazenados no banco de dados.

### Funcionalidades principais:
- 📌 **Cadastro de contatos**: Nome, Email, Telefone e Tipo de Telefone (Residencial ou Celular).  
- 💾 **Armazenamento em MySQL**: uso de `mysql.connector` para persistência dos dados.  
- 🔎 **Consulta de contatos**: listagem dos registros já cadastrados em uma tabela (QTableWidget).  
- 🎨 **Interface gráfica (PyQt5)**: criada via Qt Designer (`.ui`) e estilizada com QSS.  
- 🖥️ **Múltiplas telas**: `agenda.ui` para cadastro e `listaContatos.ui` para consulta.  

---
