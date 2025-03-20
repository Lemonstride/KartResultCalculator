from paddleocr import PaddleOCR

def get_ocr_raw_output(image_path):
    ocr = PaddleOCR(use_angle_cls=True, lang='ch')
    results = ocr.ocr(image_path, cls=True)
    raw_output = []
    for line in results:
        for box, (text, prob) in line:
            raw_output.append({'box': box, 'text': text.strip(), 'prob': prob})
    return raw_output

def process_ocr_output(raw_output):
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
            pairs.append((current_rank, player_text.strip(), '未完成'))
            current_rank += 1
            i += 2
        else:
            pairs.append((current_rank, text.strip(), '完成'))
            current_rank += 1
            i += 1
    return pairs

# ✅ 直接添加这段！
def ocr_and_process(image_path):
    raw_results = get_ocr_raw_output(image_path)
    return process_ocr_output(raw_results)