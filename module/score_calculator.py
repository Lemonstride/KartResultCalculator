# module/score_calculator.py
import pandas as pd
import os

RESULT_FILE = './results/results.csv'
SCORE_RULE = [10, 7, 5, 4, 3, 1, 0, -1]  # 排名对应分数

def calculate_score(rank, status):
    """
    根据排名和完成状态计算得分
    """
    if status == '未完成':
        return -5
    if 1 <= rank <= 8:
        return SCORE_RULE[rank - 1]
    return 0

def update_total_score(pairs):
    """
    将一局比赛结果累加到总积分
    :param pairs: [(rank, player_id, status), ...]
    """
    if os.path.exists(RESULT_FILE):
        df = pd.read_csv(RESULT_FILE)
    else:
        df = pd.DataFrame(columns=["玩家", "累计积分"])

    for rank, player_id, status in pairs:
        score = calculate_score(rank, status)
        if player_id in df['玩家'].values:
            df.loc[df['玩家'] == player_id, '累计积分'] += score
        else:
            df = pd.concat([df, pd.DataFrame([[player_id, score]], columns=["玩家", "累计积分"])], ignore_index=True)

    df.to_csv(RESULT_FILE, index=False, encoding='utf-8-sig')
    print("[✅ 积分更新完成]")
    return df

def clear_scores():
    """
    清空累计积分
    """
    if os.path.exists(RESULT_FILE):
        os.remove(RESULT_FILE)
        print("[✅ 积分已清空]")