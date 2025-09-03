
from PyQt5 import uic, QtWidgets
import mysql.connector
import os

# Conexão com o banco de dados
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="agenda"
)

def main():
    campoId = agenda.idAluno.text()
    print("Id: ", campoId)

    campoNome = agenda.nomeAluno.text()
    print("Nome: ", campoNome)

    campoEmail = agenda.emailAluno.text()
    print("Email: ", campoEmail)

    campoTelefone = agenda.telefoneAluno.text()
    print("Telefone: ", campoTelefone)

    if agenda.residencial.isChecked():
        tipoTelefone = "Residencial"
    elif agenda.celular.isChecked():
        tipoTelefone = "Celular"
    else:
        tipoTelefone = "Não informado"

    print("TipoTelefone:", tipoTelefone)

    # Inserindo os dados no banco
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO contatos (nome, email, telefone, tipoTelefone) VALUES (%s, %s, %s, %s)"
    dados = (str(campoNome), str(campoEmail), str(campoTelefone), tipoTelefone)
    cursor.execute(comando_SQL, dados)
    banco.commit()
    print("✅ Registro inserido com sucesso!")

    # Limpando os campos após salvar
    agenda.nomeAluno.setText("")
    agenda.emailAluno.setText("")
    agenda.telefoneAluno.setText("")

    print("Campos limpos.")

# Função para abrir tela de contatos
def telaConsulta():
    listaContatos.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM contatos"
    cursor.execute(comando_SQL)
    contatosLidos = cursor.fetchall()
    
    listaContatos.tableWidget.setRowCount(len(contatosLidos))
    listaContatos.tableWidget.setColumnCount(5)

    for i in range(0, len(contatosLidos)):
        for j in range(0, 5):
            listaContatos.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(contatosLidos[i][j])))

# Configuração da aplicação
app = QtWidgets.QApplication([])

# Descobre automaticamente o caminho dos arquivos .ui
base_dir = os.path.dirname(os.path.abspath(__file__))
ui_path = os.path.join(base_dir, "..", "at02", "agenda.ui")
ui_consulta = os.path.join(base_dir, "..", "at02", "listaContatos.ui")

# Carrega as duas telas em variáveis diferentes
agenda = uic.loadUi(ui_path)
listaContatos = uic.loadUi(ui_consulta)

# Ligações de eventos
agenda.cadastrar.clicked.connect(main)
agenda.consultar.clicked.connect(telaConsulta)

agenda.show()
app.exec()
