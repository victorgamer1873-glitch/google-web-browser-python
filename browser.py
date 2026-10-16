from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngine import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):


  def go_url(self):
      url = self.url_bar.text()
      self.browser.setUrl(QUrl(url))

  def update_url(self):
      self.url_bar.setText(url.toString())

  def __init__(self):
      super(MainWindow, self).__init__()
      self.browser = QWebEngineView()
      self.browser.setUrl(QUrl('http://google.com'))
      self.setCentralWidget(self.browser)
      self.showMaximized()

      #barra de navegação
      navbar = QToolBar()
      self.addToolBar(navbar)

      #botao_voltar
      voltar_btn = QAction('<-', self)
      voltar_btn.triggered.connect(self.browser.back)
      navbar.addAction(voltar_btn)

      #botao refresh
      refresh_btn = QAction('recarregar', self)
      refresh_btn.triggered.connect(self.browser.reload)
      navbar.addAction(refresh_btn)

      #botao seguir
      seguir_btn = QAction('->', self)
      seguir_btn.triggered.connect(self.browser.back)
      navbar.addAction(seguir_btn)

      #botao home
      home_btn = QAction('home', self)
      home_btn.triggered.connect(self.browser.back)
      navbar.addAction(home_btn)

      #barra de enderecos
      self.url_bar = QLineEdit()
      self.url_bar.setPlaceholderText('URL')
      navbar.addWidget(self.url_bar)
      self.setCentralWidget(self.browser)





app = QApplication(sys.argv)
QApplication.setApplicationName('browser')
window = MainWindow()

app.exec()
