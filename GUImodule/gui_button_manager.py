from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QMessageBox
from module.save_results import clear_scores, save_to_csv, load_scores
from GUImodule import screenshot_manager, gui_table_manager
from module.crop import crop_image
from module.preprocess import preprocess_image
from module.ocr_processing import ocr_and_process

class ButtonManager:
    def __init__(self, main_window):
        self.main = main_window
        self.layout = QVBoxLayout()

        self.update_btn = QPushButton("手动更新")
        self.update_btn.clicked.connect(self.update_score)
        self.layout.addWidget(self.update_btn)

        self.clear_btn = QPushButton("清空积分")
        self.clear_btn.clicked.connect(self.clear_scores)
        self.layout.addWidget(self.clear_btn)

    def update_score(self):
        latest_img = screenshot_manager.get_latest_screenshot('./ScreenShots/')
        if not latest_img:
            QMessageBox.warning(self.main, "错误", "未找到截图")
            return

        crop_image(latest_img, './ScreenShots/cropped.png')
        preprocess_image('./ScreenShots/cropped.png', './ScreenShots/preprocessed.png')
        pairs = ocr_and_process('./ScreenShots/preprocessed.png')
        save_to_csv(pairs, './results/results.csv')

        self.main.table_manager.load_scores()

    def clear_scores(self):
        clear_scores('./results/results.csv')
        self.main.table.clear()
        self.main.table.setRowCount(0)
        QMessageBox.information(self.main, "已清空", "积分已清空")