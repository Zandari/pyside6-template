from PySide6 import QtWidgets, QtCore
from .forms.accountwidget_form import Ui_Form
from .browserwidget import BrowserWidget

class AccountWidget(QtWidgets.QWidget):
    def __init__(self, username, **kwargs):
        super(AccountWidget, self).__init__(**kwargs)
        self._ui = Ui_Form()
        self._ui.setupUi(self)

        self.setLayout(self._ui.horizontalLayout)

        self._ui.browser_button.clicked.connect(self._open_browser)
        self._browser_widget = BrowserWidget(parent=self)

    def _open_browser(self):
        self._browser_widget.show
