# GUImodule/screenshot_manager.py
import os

def get_latest_screenshot(folder):
    """
    获取指定文件夹下最新的图片文件（支持png/jpg/jpeg）
    """
    if not os.path.exists(folder):
        return None

    image_files = [os.path.join(folder, f) for f in os.listdir(folder)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not image_files:
        return None

    latest_image = max(image_files, key=os.path.getctime)
    return latest_image