from typing import Optional
from PySide6 import QtCore

class TableModel(QtCore.QAbstractTableModel):
    ROW_COUNT    = 5
    COLUMN_COUNT = 5

    def __init__(self, **kwargs):
        super(TableModel, self).__init__(**kwargs)

        self._data = [[i + j for i in range(self.COLUMN_COUNT)] 
                      for j in range(self.ROW_COUNT)]

    def rowCount(self, index: QtCore.QModelIndex) -> int:
        return self.ROW_COUNT

    def columnCount(self, index: QtCore.QModelIndex) -> int:
        return self.COLUMN_COUNT

    def data(self, index: QtCore.QModelIndex, role: int) -> Optional[int]:
        if role == QtCore.Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def increase(self):
        self._data = [[self._data[j][i] + 1 for i in range(self.COLUMN_COUNT)] 
                      for j in range(self.ROW_COUNT)]
        self.layoutChanged.emit()

    def decrease(self):
        self._data = [[self._data[j][i] - 1 for i in range(self.COLUMN_COUNT)] 
                      for j in range(self.ROW_COUNT)]
        self.layoutChanged.emit()
