from PySide6 import QtCore
from widgets.mainwidget import MainWidget
from models.tablemodel import TableModel

class Application(QtCore.QObject):
    def __init__(self, **kwargs):
        super(Application, self).__init__(**kwargs)
        
        self._tablemodel = TableModel()
        self._mainwidget = MainWidget(self._tablemodel)
        self._mainwidget.show()
