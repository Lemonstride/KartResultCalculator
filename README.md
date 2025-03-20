
# KartResultCalculator 🏎️📊

基于 OCR 的卡丁车比赛积分统计工具。自动识别游戏截图中的玩家 ID 和得分，生成 CSV 文件，支持累计更新积分。

## ✨ 功能特色
- 🎯 自动裁剪截图特定区域
- 🔍 OCR 识别玩家 ID（支持中文、英文、特殊符号）
- ❌ 特殊规则："X" 识别为 -5 分
- 📈 结果保存为 CSV
- 🔄 支持增量更新，自动累计积分

## 📂 文件结构
```
KartResultCalculator/
├── main.py                 # 主程序入口
├── requirements.txt        # 依赖文件
├── ScreenShots/            # 存放原始截图
├── cache/                  # 临时缓存（裁剪图、预处理图）
├── module/                 # 功能模块（OCR、裁剪、预处理等）
├── results/                # 最终输出 CSV
└── .idea/ / __pycache__/   # 开发环境和缓存（已加入 .gitignore）
```

## 🚀 使用方法
1. 安装环境依赖（建议 Python 3.8+）：
   ```bash
   pip install -r requirements.txt
   ```

2. 将游戏截图放入 `ScreenShots/` 文件夹（示例已提供）。

3. 运行主程序：
   ```bash
   python main.py
   ```

4. 识别结果将生成在：
   ```
   results/results.csv
   ```

## 🛠 后续计划（TODO）
- [ ] 图形界面（GUI）版本开发
- [ ] 自动读取最新截图功能
- [ ] 积分排行榜可视化展示

## 📜 License
MIT License

---
**Author:** LemonStride

欢迎 Star ⭐ & Fork！
