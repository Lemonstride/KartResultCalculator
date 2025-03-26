# module/screenshot_listener.py
import os
import time

def get_latest_screenshot(folder):
    """
    获取指定文件夹下最新的图片文件
    """
    if not os.path.exists(folder):
        return None

    files = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not files:
        return None

    latest_file = max(files, key=os.path.getctime)
    return latest_file


def watch_screenshot_folder(folder, callback, interval=3):
    """
    简易轮询监听器：监控截图文件夹是否有新图片，自动调用回调处理
    :param folder: 监听的文件夹
    :param callback: 检测到新图片时执行的函数（参数为图片路径）
    :param interval: 轮询间隔（秒）
    """
    print(f"[监听开始] 文件夹：{folder}")
    last_processed = None
    while True:
        latest = get_latest_screenshot(folder)
        if latest and latest != last_processed:
            print(f"[检测到新图片] {latest}")
            callback(latest)
            last_processed = latest
        time.sleep(interval)