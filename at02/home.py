from PyQt5 import uic, QtWidgets
import mysql.connector
import os
from reportlab.pdfgen import canvas 

# Conexão com o banco de dados
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="agenda"
)

def main():

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

# Função excluir contato
def excluirContato():
    linhacontato = listaContatos.tableWidget.currentRow()
    idContato = listaContatos.tableWidget.item(linhacontato, 0).text()

    cursor = banco.cursor()
    cursor.execute("DELETE FROM contatos WHERE id = %s", (idContato,))
    banco.commit()

    listaContatos.tableWidget.removeRow(linhacontato)

# Função para editar contato
def editarContato():
    linhacontato = listaContatos.tableWidget.currentRow()

    idContato = listaContatos.tableWidget.item(linhacontato, 0).text()
    nomeContato = listaContatos.tableWidget.item(linhacontato, 1).text()
    emailContato = listaContatos.tableWidget.item(linhacontato, 2).text()
    telefoneContato = listaContatos.tableWidget.item(linhacontato, 3).text()
    tipoTelefone = listaContatos.tableWidget.item(linhacontato, 4).text()

    cursor = banco.cursor()
    cursor.execute("UPDATE contatos SET nome = %s, email = %s, telefone = %s, tipoTelefone = %s WHERE id = %s",
                   (nomeContato, emailContato, telefoneContato, tipoTelefone, idContato))           
    banco.commit()

# Função para gerar PDF
def gerarPdf():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM contatos"
    cursor.execute(comando_SQL)
    contatos_lidos = cursor.fetchall()

    y = 0
    pdf = canvas.Canvas("lista_contatos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200, 800, "Lista de Contatos")

    pdf.setFont("Times-Bold", 18)
    pdf.drawString(10, 750, "ID")
    pdf.drawString(110, 750, "NOME")
    pdf.drawString(210, 750, "EMAIL")
    pdf.drawString(410, 750, "TELEFONE")
    pdf.drawString(510, 750, "TIPO DE CONTATO")

    for i in range(0, len(contatos_lidos)):
        y = y + 50
        pdf.drawString(10, 750 - y, str(contatos_lidos[i][0]))
        pdf.drawString(110, 750 - y, str(contatos_lidos[i][1]))
        pdf.drawString(210, 750 - y, str(contatos_lidos[i][2]))
        pdf.drawString(410, 750 - y, str(contatos_lidos[i][3]))
        pdf.drawString(510, 750 - y, str(contatos_lidos[i][4]))

    pdf.save()
    print("📄 PDF gerado com sucesso!")

# Função para voltar à tela principal
def telaVoltar():
    listaContatos.close()
    agenda.show()

# Configuração da aplicação
app = QtWidgets.QApplication([])

# Descobre automaticamente o caminho dos arquivos .ui
base_dir = os.path.dirname(os.path.abspath(__file__))
ui_path = os.path.join(base_dir, "..", "at03", "agenda.ui")
ui_consulta = os.path.join(base_dir, "..", "at03", "listaContatos.ui")

# Carrega as duas telas
agenda = uic.loadUi(ui_path)
listaContatos = uic.loadUi(ui_consulta)

# Ligações de eventos
agenda.cadastrar.clicked.connect(main)
agenda.consultar.clicked.connect(telaConsulta)
listaContatos.delContato.clicked.connect(excluirContato) 
listaContatos.altContato.clicked.connect(editarContato)
listaContatos.voltar.clicked.connect(telaVoltar)
listaContatos.gerarPDF.clicked.connect(gerarPdf) 

agenda.show()
app.exec()
