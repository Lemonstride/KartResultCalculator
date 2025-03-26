# GUImain.py
import sys
from PyQt5.QtWidgets import QApplication
from GUImodule.gui_main_window import KartMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KartMainWindow()
    window.show()
    sys.exit(app.exec_())