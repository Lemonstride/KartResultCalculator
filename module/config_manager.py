# module/config_manager.py
import json
import os

CONFIG_FILE = './config.json'

def load_config():
    """
    加载配置，自动处理空文件或格式错误
    """
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if not content:
                    print("[⚠️ 警告] config.json 文件为空，使用默认配置")
                    return {}
                return json.loads(content)
        except json.JSONDecodeError:
            print("[⚠️ 错误] config.json 格式错误，使用默认配置")
            return {}
    return {}

def save_config(config_data):
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config_data, f, indent=4, ensure_ascii=False)

def get_screenshot_folder():
    config = load_config()
    return config.get('screenshot_folder', './ScreenShots/')

def set_screenshot_folder(path):
    config = load_config()
    config['screenshot_folder'] = path
    save_config(config)