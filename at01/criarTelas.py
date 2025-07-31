import sys #Importando biblioteca sys para manipulação de argumentos do sistema
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel #Importando classes necessárias do PyQt5 para criar a interface gráfica

#Criando aplicação
app = QApplication(sys.argv) #Instância da aplicação

#Criar janela principal 
janela = QWidget()
janela.setWindowTitle("Primeira aplicação front em python") #Titulo da janela
janela.setGeometry(50, 200, 350, 150) #Definindo tamanho e posição da janela

#Criando um rótulo (label)
rotulo = QLabel("Hello word!", janela) #Criando um rótulo 
rotulo.move(130, 30) #Posicionando o rótulo na janela

#Criando um botão
botao = QPushButton("Clique aqui!", janela) #Criando um botão
botao.move(150, 70) #Posicionando o botão na janela

#Exibir a janela
janela.show() 

#Iniciando o loop de eventos
sys.exit(app.exec_()) 

