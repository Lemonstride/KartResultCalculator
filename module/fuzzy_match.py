# module/fuzzy_match.py
from rapidfuzz import process, fuzz

def fuzzy_match(current_id, known_ids, threshold=85):
    """
    使用模糊匹配算法，将OCR识别的ID与已知ID进行比对，自动归并相似ID
    :param current_id: OCR识别出来的玩家ID
    :param known_ids: 已知正确ID列表（历史+已绑定）
    :param threshold: 匹配阈值（默认85）
    :return: 匹配到的最佳ID或原ID
    """
    if not known_ids:
        return current_id

    match, score, _ = process.extractOne(current_id, known_ids, scorer=fuzz.ratio)
    if score >= threshold:
        return match
    return current_id