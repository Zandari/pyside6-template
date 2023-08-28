from PySide6 import QtCore
from widgets.mainwidget import MainWidget
from models.tablemodel import TableModel

class Application(QtCore.QObject):
    def __init__(self, **kwargs):
        super(Application, self).__init__(**kwargs)
        
        self._tablemodel = TableModel()
        self._mainwidget = MainWidget(self._tablemodel)
        self._mainwidget.incr_clicked.connect(self._tablemodel.increase)
        self._mainwidget.decr_clicked.connect(self._tablemodel.decrease)
        self._mainwidget.show()
        print("asdfasfd")
