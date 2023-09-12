from PySide6 import QtWidgets, QtCore
from .editaccountwidget import EditAccountWidget
from .accountwidget import AccountWidget
from .forms.mainwidget_form import Ui_Form

class MainWidget(QtWidgets.QWidget):
    def __init__(self, table_model: QtCore.QAbstractTableModel, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self._ui = Ui_Form()
        self._ui.setupUi(self)
        # self._ui.tableview.setModel(table_model)
        self._ui.add_button.clicked.connect(self._show_add_widget)
        self._edit_account_widget = EditAccountWidget()


        for i in range(5):
            item = QtWidgets.QListWidgetItem(self._ui.listWidget)
            widget = AccountWidget(f"Username{i}")
            item.setSizeHint(widget.minimumSizeHint())
            self._ui.listWidget.addItem(item)
            self._ui.listWidget.setItemWidget(item, widget)

    def _show_add_widget(self):
        self._edit_account_widget.show()
