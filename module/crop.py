import cv2

def crop_image(image_path, save_path):
    """ 读取并裁剪图片，截取指定区域 """
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("无法读取图片，请检查路径！")

    # 截取 (x=310, y=840, 宽=20, 高=270) 区域
    cropped_image = image[310:840, 20:270] #带白边
    #cropped_image = image[270:800, 20:230]  #不带白边

    # 保存裁剪后的图片
    cv2.imwrite(save_path, cropped_image)
