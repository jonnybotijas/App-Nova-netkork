from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6.QtSql import QSqlDatabase, QSqlTableModel

# Conectar ao banco de dados
db = QSqlDatabase.addDatabase('')
db.setHostName('10.0.21.105')
db.setDatabaseName('postgres')
db.setUserName('postgres')
db.setPassword('basededados2023')
if not db.open():
    print('Não foi possível conectar ao banco de dados')


# Executar a consulta SQL
query = "SELECT * FROM mytable"
model = QSqlTableModel()
model.setTable('mytable')
model.setEditStrategy(QSqlTableModel.OnFieldChange)
model.select()

# Criar o tablewidget e associar ao modelo de tabela
table = QTableView()
table.setModel(model)

# Exibir o tablewidget
main_window = QMainWindow()
main_window.setCentralWidget(table)
main_window.show()

# Executar o loop de eventos do aplicativo
app = QApplication()
app.exec_()