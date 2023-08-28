from PySide6 import QtWidgets, QtCore
from .forms.mainwidget_form import Ui_Form

class MainWidget(QtWidgets.QWidget):
    incr_clicked: QtCore.Signal = None 
    decr_clicked: QtCore.Signal = None 

    def __init__(self, table_model: QtCore.QAbstractTableModel, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self._ui = Ui_Form()
        self._ui.setupUi(self)
        self._ui.tableview.setModel(table_model)
        self.incr_clicked = self._ui.incr_button.clicked
        self.decr_clicked = self._ui.decr_button.clicked
