import cv2

def preprocess_image(image):
    """
    图像预处理（CLAHE增强 + 高斯降噪），传cv2图像进来，返回处理后图
    """
    if image is None:
        print("[❌ 预处理失败，图像为空]")
        return None

    # 灰度
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # CLAHE增强
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)

    # 高斯模糊降噪
    blurred = cv2.GaussianBlur(enhanced, (3, 3), sigmaX=0)

    return blurred