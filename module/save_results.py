import pandas as pd
import os

# 计分规则
SCORE_MAPPING = {1: 10, 2: 7, 3: 5, 4: 4, 5: 3, 6: 1, 7: 0, 8: -1}
DEFAULT_SCORE = -5  # “X” 记为 -5 分

def save_to_csv(processed_pairs, csv_path):
    """ 计算积分并保存至 CSV """
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        score_dict = dict(zip(df["玩家"], df["累计积分"]))
    else:
        score_dict = {}

    ranking = []
    for rank, player, status in processed_pairs:
        if status == '未完成':
            score = DEFAULT_SCORE
        else:
            score = SCORE_MAPPING.get(rank, DEFAULT_SCORE)

        # 积分累加
        score_dict[player] = score_dict.get(player, 0) + score
        ranking.append((rank, player, score, score_dict[player]))

    result_df = pd.DataFrame(ranking, columns=["排名", "玩家", "本次得分", "累计积分"])
    result_df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    print(f"✅ 已保存积分到 {csv_path}")
