import cv2

def crop_image(image_path, x, y, w, h):
    """
    裁剪指定区域，直接返回裁剪后的cv2图像
    """
    image = cv2.imread(image_path)
    if image is None:
        print(f"[❌ 裁剪失败，图片读取失败] {image_path}")
        return None

    cropped = image[y:y + h, x:x + w]
    return cropped