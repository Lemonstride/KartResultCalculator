# GUImodule/gui_button_manager.py
from PyQt5.QtWidgets import QPushButton, QMessageBox
from module.score_calculator import clear_scores
from GUImodule.gui_folder_selector import select_screenshot_folder

class ButtonManager:
    def __init__(self, main_window):
        self.main_window = main_window
        self.setup_buttons()

    def setup_buttons(self):
        self.update_button = QPushButton("手动更新")
        self.update_button.clicked.connect(self.main_window.manual_update)

        self.clear_button = QPushButton("清空积分")
        self.clear_button.clicked.connect(self.clear_score_action)

        self.select_folder_button = QPushButton("绑定截图路径")
        self.select_folder_button.clicked.connect(self.select_folder_action)

        self.main_window.layout.addWidget(self.update_button)
        self.main_window.layout.addWidget(self.clear_button)
        self.main_window.layout.addWidget(self.select_folder_button)

    def clear_score_action(self):
        reply = QMessageBox.question(
            self.main_window,
            "清空确认",
            "确定要清空所有积分吗？",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            clear_scores()
            self.main_window.refresh_table()

    def select_folder_action(self):
        folder = select_screenshot_folder(self.main_window)
        if folder:
            self.main_window.screenshot_folder = folder