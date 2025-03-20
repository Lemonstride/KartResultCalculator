import json
import os

MAPPING_FILE = './results/id_mapping.json'

def load_mapping():
    """
    加载ID映射表
    """
    if os.path.exists(MAPPING_FILE):
        with open(MAPPING_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {}

def save_mapping(mapping):
    """
    保存ID映射表
    """
    os.makedirs(os.path.dirname(MAPPING_FILE), exist_ok=True)
    with open(MAPPING_FILE, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, ensure_ascii=False, indent=4)

def apply_id_mapping(player_id):
    """
    根据映射自动修正ID
    """
    mapping = load_mapping()
    return mapping.get(player_id, player_id)

def add_mapping(wrong_id, correct_id):
    """
    添加新的错误ID -> 正确ID 映射
    """
    mapping = load_mapping()
    mapping[wrong_id] = correct_id
    save_mapping(mapping)