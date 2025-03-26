from paddleocr import PaddleOCR
from module.id_mapping import apply_id_mapping
from module.fuzzy_match import fuzzy_match
from module.crop import crop_image
from module.preprocess import preprocess_image

ocr_model = PaddleOCR(use_angle_cls=True, lang='ch')

def get_ocr_raw_output(image_path):
    """
    读取图片 -> 裁剪目标区域 -> 预处理 -> OCR识别
    """
    # ✅ 裁剪图片区域（这里可以自定义区域）
    cropped_img = crop_image(image_path, x=20, y=310, w=250, h=830)
    if cropped_img is None:
        print(f"[❌ 裁剪失败] {image_path}")
        return []

    # ✅ 预处理增强
    preprocessed_img = preprocess_image(cropped_img)
    if preprocessed_img is None:
        print(f"[❌ 预处理失败] {image_path}")
        return []

    # ✅ OCR识别（直接传入处理好的图）
    results = ocr_model.ocr(preprocessed_img, cls=True)

    # 整理输出
    raw_output = []
    for line in results:
        for box, (text, prob) in line:
            raw_output.append({'box': box, 'text': text.strip(), 'prob': prob})
    return raw_output

def process_ocr_output(raw_output, known_players=None):
    """
    处理OCR结果，排序+ID映射+模糊匹配
    """
    extracted = []
    for item in raw_output:
        y_top = min([point[1] for point in item['box']])
        extracted.append((y_top, item['text'], item['prob']))
    extracted.sort(key=lambda x: x[0])

    pairs, i, current_rank = [], 0, 1
    while i < len(extracted):
        _, text, prob = extracted[i]
        if prob < 0.4:
            i += 1
            continue

        if text == 'X' and i + 1 < len(extracted):
            _, player_text, next_prob = extracted[i + 1]
            player_text = apply_id_mapping(player_text.strip())
            if known_players:
                player_text = fuzzy_match(player_text, known_players)
            pairs.append((current_rank, player_text, '未完成'))
            current_rank += 1
            i += 2
        else:
            player_text = apply_id_mapping(text.strip())
            if known_players:
                player_text = fuzzy_match(player_text, known_players)
            pairs.append((current_rank, player_text, '完成'))
            current_rank += 1
            i += 1
    return pairs

def ocr_and_process(image_path, known_players=None):
    """
    全流程：裁剪 -> 预处理 -> OCR -> 处理ID
    """
    raw_results = get_ocr_raw_output(image_path)
    return process_ocr_output(raw_results, known_players)