import sys
import traceback
import os 
from datetime import datetime
from PySide6 import QtWidgets

from application import Application


def setup_logging():
    if not os.path.isdir("logs"):
        os.mkdir("logs")
    cur_time = datetime.now().strftime("logging_%m_%d_%H_%M_%S")
    logging.basicConfig(
        format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
        datefmt='%H:%M:%S',
        filename=f"logs\\{cur_time}.log",
        level=logging.DEBUG
    )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Application()
    app.setStyle('Fusion')
    app.exec()
