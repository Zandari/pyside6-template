from PySide6 import QtWidgets, QtCore

class BrowserWidget(QtWidgets.QWidget):
    def __init__(self, **kwargs):
        super(BrowserWidget, self).__init__(**kwargs)

        self.setMinimumHeight(500)
        self.setMinimumWidth(500)
