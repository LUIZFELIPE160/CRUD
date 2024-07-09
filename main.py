import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTreeWidgetItem
from PyQt5.QtCore import QDate
from cadastro import Ui_MainWindow  #CHAMANDO A PASTA E IMPORTANDO A CLASS DA INTERFACE GRÁFICA
import database #IMPORT DO BANCO DE DADOS


class MainWindow(QMainWindow, Ui_MainWindow): 
    def __init__(self) -> None:  # 
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # DANDO FUNCAO AOS BOTOES
        self.btn_adicionar.clicked.connect(self.adicionar_func)
        self.btn_delete.clicked.connect(self.deletar_func)
        self.btn_atualizar.clicked.connect(self.atualizar_func)
        self.btn_veritem.clicked.connect(self.limpar)
        #MOSTRANDO RESULTADO NA TELA
        self.tw_funcionarios.itemSelectionChanged.connect(self.selecionar_item)
        self.mostrar()

    def adicionar_func(self):
        cpf = self.l_cpf.text()
        nome = self.l_nome.text()
        idade = int(self.l_idade.text())
        funcao = self.l_funcao.text()
        admissao = self.l_date.date().toString('yyyy-MM-dd')
        remuneracao = self.l_remuneracao.text()
        observacoes = self.l_observacao.text()

        if database.cpf_exists(cpf): # VERIFICA NO BANCO SE JA EXISTE TAL PESSOA 
            msg = QMessageBox()
            msg.setWindowTitle("ERRO")
            msg.setText("Funcionário já existente no banco de dados!")
            msg.exec()
            return
        try:
            database.add_func(cpf, nome, idade, funcao, admissao, remuneracao, observacoes)
            msg = QMessageBox()
            msg.setWindowTitle("Sucesso")
            msg.setText("Funcionário adicionado com sucesso!")
            msg.exec()
            self.mostrar()
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao adicionar funcionário: {e}")
            msg.exec()
        self.limpar()

    def mostrar(self):
        try:
            # Limpar o QTreeWidget antes de adicionar novos itens
            self.tw_funcionarios.clear()

            # Obter dados do banco de dados
            data = database.select_func()

            for row in data:
                item = QTreeWidgetItem([str(field) for field in row])
                self.tw_funcionarios.addTopLevelItem(item)
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao carregar dados: {e}")
            msg.exec()

    def deletar_func(self):
        selected_items = self.tw_funcionarios.selectedItems()
        if not selected_items:
            msg = QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText("Por favor, selecione um funcionário para deletar.")
            msg.exec()
            return

        cpf = selected_items[0].text(0)
        try:
            database.delete_func(cpf)
            msg = QMessageBox()
            msg.setWindowTitle("Sucesso")
            msg.setText("Funcionário deletado com sucesso!")
            msg.exec()
            self.mostrar()
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao deletar funcionário: {e}")
            msg.exec()

    def atualizar_func(self):
        selected_items = self.tw_funcionarios.selectedItems()
        if not selected_items:
            msg = QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText("Por favor, selecione um funcionário para atualizar.")
            msg.exec()
            return

        cpf = selected_items[0].text(0)
        nome = self.l_nome.text()
        idade = int(self.l_idade.text())
        funcao = self.l_funcao.text()
        admissao = self.l_date.date().toString('yyyy-MM-dd')
        remuneracao = self.l_remuneracao.text()
        observacoes = self.l_observacao.text()

        try:
            database.update_func(cpf, nome, idade, funcao, admissao, remuneracao, observacoes)
            msg = QMessageBox()
            msg.setWindowTitle("Sucesso")
            msg.setText("Funcionário atualizado com sucesso!")
            msg.exec()
            self.mostrar()
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao atualizar funcionário: {e}")
            msg.exec()
        self.limpar()

    def selecionar_item(self):
        selected_items = self.tw_funcionarios.selectedItems()
        if selected_items:
            item = selected_items[0]
            self.l_cpf.setText(item.text(0))
            self.l_nome.setText(item.text(1))
            self.l_idade.setText(item.text(2))
            self.l_funcao.setText(item.text(3))
            self.l_date.setDate(QDate.fromString(item.text(4), 'yyyy-MM-dd'))
            self.l_remuneracao.setText(item.text(5))
            self.l_observacao.setText(item.text(6))

    def limpar (self):
        self.l_cpf.clear()
        self.l_nome.clear()
        self.l_idade.clear()
        self.l_funcao.clear()
        self.l_date.setDate(QDate.currentDate())
        self.l_remuneracao.clear()
        self.l_observacao.clear()


if __name__ == "__main__":
    database.create_table()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
