from Pyside6.QtWidgets import QMainwindow
from views.main_window import MainWindowForm
class MainWindow (QMainwindow,MainWindowForm):
    def __init__ (self):
        super().__init__()
        self.setupUi(self)

        self.openWindowButton.clicked.connect(self.open_Window)