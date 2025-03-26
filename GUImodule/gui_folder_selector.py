# GUImodule/gui_folder_selector.py
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from module import config_manager

def select_screenshot_folder(parent=None):
    """
    弹出文件夹选择框，选择截图文件夹并保存到 config.json
    """
    folder = QFileDialog.getExistingDirectory(parent, "选择截图文件夹")
    if folder:
        config_manager.set_screenshot_folder(folder)
        QMessageBox.information(parent, "路径已保存", f"已选择截图文件夹:\n{folder}")
        return folder
    else:
        QMessageBox.warning(parent, "未选择", "未选择任何文件夹")
        return None

def get_current_folder():
    """
    获取当前截图文件夹路径
    """
    return config_manager.get_screenshot_folder()