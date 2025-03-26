# GUImodule/gui_auto_refresh.py
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtCore import QTimer
from GUImodule.screenshot_manager import get_latest_screenshot
from module.ocr_processing import ocr_and_process
from module.score_calculator import update_total_score
import pandas as pd

class AutoRefresh:
    def __init__(self, main_window):
        self.main_window = main_window
        self.auto_refresh_checkbox = QCheckBox("开启自动刷新")
        self.main_window.layout.addWidget(self.auto_refresh_checkbox)

        # 定时器轮询文件夹
        self.timer = QTimer()
        self.timer.timeout.connect(self.auto_check)

        # 勾选后启动/关闭自动刷新
        self.auto_refresh_checkbox.stateChanged.connect(self.toggle_auto_refresh)

        self.last_processed = None

    def toggle_auto_refresh(self, state):
        if state:
            self.timer.start(3000)  # 每3秒检测一次
            print("[✅ 自动刷新已开启]")
        else:
            self.timer.stop()
            print("[⏸️ 自动刷新已关闭]")

    def auto_check(self):
        latest_image = get_latest_screenshot(self.main_window.screenshot_folder)
        if latest_image and latest_image != self.last_processed:
            print(f"[🆕 自动检测到新图片] {latest_image}")
            known_players = self.main_window.table_manager.get_all_players()
            pairs = ocr_and_process(latest_image, known_players)

            # 更新总积分
            df = update_total_score(pairs)
            self.main_window.table_manager.update_table(df)

            # 记录已处理图片
            self.last_processed = latest_image