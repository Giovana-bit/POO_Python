import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QHBoxLayout, QVBoxLayout

# Criando aplicação
app = QApplication(sys.argv)

# Carregando QSS externo
with open("estilo.qss", "r") as arquivo_qss:
    estilo = arquivo_qss.read()
    app.setStyleSheet(estilo)

# Criar janela principal 
janela = QWidget()
janela.setWindowTitle("Primeira aplicação front em Python")
janela.setGeometry(100, 200, 500, 200)
janela.setObjectName("janelaPrincipal")

# Criando um rótulo (label)
rotulo = QLabel("Hello world!", janela)

# Função que será chamada ao clicar no botão
def botaoClicado():
    print("Botão clicado!")

# Criando botões
botao1 = QPushButton("Clique aqui!")
botao1.setObjectName("botaoCustom")
botao1.setFixedSize(120, 40)
botao1.clicked.connect(botaoClicado)

botao2 = QPushButton("Meow")
botao2.setObjectName("botaoCustom2")
botao2.setFixedSize(120, 40)

botao3 = QPushButton("Woof")
botao3.setObjectName("botaoCustom3")
botao3.setFixedSize(120, 40)

# Layouts
layoutPrincipal = QVBoxLayout()
layoutBotoes = QHBoxLayout()

layoutBotoes.addWidget(botao1)
layoutBotoes.addWidget(botao2)
layoutBotoes.addWidget(botao3)

layoutPrincipal.addWidget(rotulo)
layoutPrincipal.addLayout(layoutBotoes)

janela.setLayout(layoutPrincipal)

# Exibir a janela
janela.show()

# Iniciando o loop de eventos
sys.exit(app.exec_())
