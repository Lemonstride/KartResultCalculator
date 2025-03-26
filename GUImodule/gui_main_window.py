# GUImodule/gui_main_window.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from GUImodule.gui_button_manager import ButtonManager
from GUImodule.gui_table_manager import TableManager
from GUImodule.gui_auto_refresh import AutoRefresh
from GUImodule.screenshot_manager import get_latest_screenshot
from module.ocr_processing import ocr_and_process
from module.score_calculator import update_total_score
from module.config_manager import get_screenshot_folder
import pandas as pd

class KartMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kart Result Calculator")
        self.resize(900, 650)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # 配置截图文件夹
        self.screenshot_folder = get_screenshot_folder()

        # 表格管理
        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)
        self.table_manager = TableManager(self.table_widget)

        # 按钮管理
        self.button_manager = ButtonManager(self)

        # 自动刷新模块
        self.auto_refresh = AutoRefresh(self)

        # 初始化积分表
        self.refresh_table()

    def manual_update(self):
        """
        手动更新触发
        """
        latest_image = get_latest_screenshot(self.screenshot_folder)
        if not latest_image:
            print("[⚠️ 未找到最新截图]")
            return

        print(f"[✅ 正在处理] {latest_image}")
        known_players = self.table_manager.get_all_players()

        # ✅ 全流程OCR直接调用（裁剪+预处理已接入）
        pairs = ocr_and_process(latest_image, known_players)

        # 积分累加
        df = update_total_score(pairs)
        self.table_manager.update_table(df)

    def refresh_table(self):
        """
        重新加载积分表
        """
        try:
            df = pd.read_csv('./results/results.csv')
            self.table_manager.update_table(df)
        except FileNotFoundError:
            self.table_manager.clear_table()