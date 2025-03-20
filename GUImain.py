from PyQt5.QtWidgets import QApplication
from GUImodule.gui_main_window import KartMainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KartMainWindow()
    window.show()
    sys.exit(app.exec_())