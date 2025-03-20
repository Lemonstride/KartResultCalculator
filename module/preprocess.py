import cv2

def preprocess_image(image_path, save_path):
    image = cv2.imread(image_path)
    # 使用CLAHE增强对比度（避免过曝）
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)
    # 轻量高斯模糊去噪
    blurred = cv2.GaussianBlur(enhanced, (3,3), 0)
    cv2.imwrite(save_path, blurred)
