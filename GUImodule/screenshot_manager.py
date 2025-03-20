import os

def get_latest_screenshot(folder):
    files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.png')]
    return max(files, key=os.path.getctime) if files else None