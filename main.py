from module.crop import crop_image
from module.preprocess import preprocess_image
from module.ocr_processing import process_ocr_output, get_ocr_raw_output
from module.save_results import save_to_csv
import os

if __name__ == "__main__":
    screenshot = './ScreenShots/test_image.png'
    cropped = './cache/croppedImage/cropped.png'
    preprocessed = './cache/preprocessedImage/preprocessed.png'
    result_csv = './results/results.csv'

    if not os.path.exists(screenshot):
        print("❌ 没有找到截图！请放截图到 screenshots 文件夹")
        exit()

    # 1️⃣ 裁剪
    crop_image(screenshot, cropped)
    print("✅ 裁剪完成")

    # 2️⃣ 图像预处理
    preprocess_image(cropped, preprocessed)
    print("✅ 图像预处理完成")

    # 3️⃣ OCR识别 + 处理排名、未完成
    raw_output = get_ocr_raw_output(preprocessed)
    pairs = process_ocr_output(raw_output)

    print("✅ 排名 - 玩家ID - 状态")
    for r, p, s in pairs:
        print(f"{r} - {p} - {s}")

    # 4️⃣ 积分计算并保存
    save_to_csv(pairs, result_csv)