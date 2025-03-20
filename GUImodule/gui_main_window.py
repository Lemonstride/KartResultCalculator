from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QCheckBox
from GUImodule.gui_button_manager import ButtonManager
from GUImodule.gui_table_manager import TableManager
from GUImodule.gui_auto_refresh import AutoRefresh

class KartMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kart Result Calculator")
        self.resize(800, 600)

        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.table_manager = TableManager(self.table)
        self.button_manager = ButtonManager(self)
        self.layout.addLayout(self.button_manager.layout)

        self.auto_checkbox = QCheckBox("开启自动刷新")
        self.layout.addWidget(self.auto_checkbox)

        self.auto_refresh = AutoRefresh(self.button_manager.update_score)
        self.auto_checkbox.stateChanged.connect(self.toggle_auto_refresh)

        self.setLayout(self.layout)
        self.table_manager.load_scores()

    def toggle_auto_refresh(self):
        if self.auto_checkbox.isChecked():
            self.auto_refresh.start()
        else:
            self.auto_refresh.stop()
