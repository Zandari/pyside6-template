from PySide6 import QtWidgets, QtCore
from .forms.editaccountwidget_form import Ui_Form

class EditAccountWidget(QtWidgets.QWidget):
    def __init__(self, **kwargs):
        super(EditAccountWidget, self).__init__(**kwargs)
        self._ui = Ui_Form()
        self._ui.setupUi(self)
        # self._ui.tableview.setModel(table_model)
