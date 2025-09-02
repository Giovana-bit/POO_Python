from PyQt5 import uic, QtWidgets
import mysql.connector

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

# Configuração da aplicação
app = QtWidgets.QApplication([])
agenda = uic.loadUi("agenda.ui")
agenda.cadastrar.clicked.connect(main)

agenda.show()
app.exec()
