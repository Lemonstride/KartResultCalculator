# module/save_results.py
import pandas as pd
import os

RESULT_FILE = './results/results.csv'

def load_scores():
    """
    加载已保存的总积分结果CSV
    """
    if os.path.exists(RESULT_FILE):
        return pd.read_csv(RESULT_FILE)
    else:
        return pd.DataFrame(columns=["玩家", "累计积分"])

def export_to_csv(df, export_path):
    """
    导出当前积分DataFrame为CSV
    """
    df.to_csv(export_path, index=False, encoding='utf-8-sig')
    print(f"[导出成功] {export_path}")

def clear_results():
    """
    清空结果CSV文件
    """
    if os.path.exists(RESULT_FILE):
        os.remove(RESULT_FILE)
        print("[积分记录已清空]")