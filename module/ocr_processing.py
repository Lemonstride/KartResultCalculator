from paddleocr import PaddleOCR

def get_ocr_raw_output(image_path):
    """
    原始 PaddleOCR 输出（带坐标、置信度）
    """
    ocr = PaddleOCR(use_angle_cls=True, lang='ch')
    results = ocr.ocr(image_path, cls=True)

    raw_output = []
    for line in results:
        for box, (text, prob) in line:
            raw_output.append({'box': box, 'text': text.strip(), 'prob': prob})
    return raw_output

def process_ocr_output(raw_output):
    """
    排序 + 处理X标记未完成 + 生成(rank, player, status)
    """
    # 提取 y 坐标用于排序
    extracted = []
    for item in raw_output:
        y_top = min([point[1] for point in item['box']])
        extracted.append((y_top, item['text'], item['prob']))

    # 排序（从上往下）
    extracted.sort(key=lambda x: x[0])

    # 生成 (rank, player, status)
    pairs = []
    i = 0
    current_rank = 1
    while i < len(extracted):
        _, text, prob = extracted[i]
        if prob < 0.4:  # 放宽中文识别置信度
            i += 1
            continue

        if text == 'X':
            # 绑定X后玩家为未完成
            if i + 1 < len(extracted):
                _, player_text, next_prob = extracted[i + 1]
                pairs.append((current_rank, player_text.strip(), '未完成'))
                current_rank += 1
                i += 2
                continue
            i += 1
        else:
            pairs.append((current_rank, text.strip(), '完成'))
            current_rank += 1
            i += 1

    return pairs
