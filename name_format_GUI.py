# pylint : disable=<no-name-in-module>
# pylint : disable=<missing-module-docstring>

from calendar import *
import sys
import time
import os
from datetime import datetime, timedelta
from PyQt6.QtCore import QSize, QThread
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QMessageBox,
)


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the main window and set up the UI elements.
        """

        super().__init__()

        # App window settings
        self.setWindowTitle("Auto Renomear")
        self.setMaximumSize(QSize(600, 400))
        self.setMinimumSize(QSize(400, 200))

        self.label = QLabel()  # sets label for the UI

        # sets up the inputs variables
        self.mes = QLineEdit()
        self.ano = QLineEdit()
        self.caminho = QLineEdit()

        self.mes.textChanged.connect(self.label.setText)
        self.ano.textChanged.connect(self.label.setText)
        self.caminho.textChanged.connect(self.label.setText)
        layout = QVBoxLayout()

        # Add line inputs
        layout.addWidget(QLabel("Insira o número do mês (MM):"))
        layout.addWidget(self.mes)

        layout.addWidget(QLabel("Insira o ano (AAAA):"))
        layout.addWidget(self.ano)

        layout.addWidget(QLabel("Insira o caminho para a pasta dos arquivos:"))
        layout.addWidget(self.caminho)

        container = QWidget()
        container.setLayout(layout)

        # Rename start button
        self.button = QPushButton("Renomear Arquivos")
        self.button.clicked.connect(self.iniciar)

        layout.addWidget(self.button)

        self.setCentralWidget(container)

    def iniciar(self):
        """
        Handle the click event of the button.
        Start the data processing thread and disable the button.

        """
        self.button.setText("Carregando...")
        self.button.setEnabled(False)

        self.getdata = getData()
        self.getdata.finished.connect(self.finalizar)

        self.getdata.mes = self.mes.text()
        self.getdata.ano = self.ano.text()
        self.getdata.caminho = self.caminho.text()

        # handles the error for incorrect info inputs
        if len(self.getdata.ano) != 4 or len(self.getdata.mes) != 2:
            self.mensagem_erro()
            return

        try:
            self.getdata.mes = int(self.getdata.mes)
            self.getdata.ano = int(self.getdata.ano)
        except ValueError:
            self.mensagem_erro()

        self.getdata.start()

    def finalizar(self):
        """
        Handle the completion of the data processing.
        Show a message box and finalize the application.
        """

        self.button.setText("Finalizando")
        self.button.setEnabled(False)

        QMessageBox.information(
            self, "Name Format APP", "Arquivos renomeados com sucesso"
        )
        time.sleep(1)
        QMessageBox.information(self, "Name Format APP", "Finalizando APP")

        time.sleep(2)
        sys.exit()

    # defines a function for clearing inputs
    def restart(self):
        self.mes.clear()
        self.ano.clear()
        self.caminho.clear()

    def mensagem_erro(self):
        """
        Handles ValueErrors
        """
        erro = QMessageBox()
        erro.setText("Formato inválido, tente novamente")

        time.sleep(2)
        return self.restart


class getData(QThread):
    def __init__(self):
        super().__init__()

    """
    Initializes the Thread for processing the inputs

    """


    def run(self):
        files = os.listdir(self.caminho)

        try:
            data = datetime(self.ano, self.mes, 1)
            dias_no_mes = monthrange(data.year, data.month)[1]
        except ValueError:
            # FIXME
            return QMessageBox.information(self, "Name Format APP", "Mês invalido")

        for file in files:
            try:
                if file.endswith(".xlsx") or file.endswith(".xls"):
                    novo_nome = data.strftime("%d-%m-%Y.xlsx")

                    caminho_antigo = os.path.join(self.caminho, file)
                    caminho_novo = os.path.join(self.caminho, novo_nome)
                    os.rename(caminho_antigo, caminho_novo)

                if data.day < dias_no_mes:
                    data += timedelta(days=1)
                else:
                    break

            except FileExistsError:
                continue
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
