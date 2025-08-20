from PyQt5 import uic, QtWidgets

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


app = QtWidgets.QApplication([])
agenda = uic.loadUi("agenda.ui")
agenda.cadastrar.clicked.connect(main)

agenda.show()
app.exec()
    