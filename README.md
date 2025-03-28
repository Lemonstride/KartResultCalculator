# 🏎️ KartResultCalculator 自动识别积分系统（支持图形界面）

## 📋 项目简介
本项目为 **《跑跑卡丁车》** 等竞速游戏开发，基于截图自动识别玩家排名、计算积分、保存历史，并提供 **图形化界面（GUI）** 管理。

支持：

✅ 中文 / 英文 OCR \
✅ 自动处理“未完成(X)”  \
✅ 自动积分累计  \
✅ 图形化界面操作（PyQt5）\
✅ 手动修正错识别的ID，后续自动应用ID映射

---

## 📅 文件结构
```
KartResultCalculator/
👍 GUImain.py                  # 图形界面启动
👍 main.py                     # 控制台启动（可选）
👍 GUImodule/                  # 图形界面功能模块
👍 module/                     # 核心功能模块（OCR、积分等）
👍 ScreenShots/                # 游戏截图文件夹
👍 results/                    # 积分记录 CSV
👍 README.md
👍 requirements.txt
```

---

## ✨ 图形界面功能（PyQt5 实现）
- ✅ 实时积分表格显示
- ✅ 一键更新按钮（自动读取截图识别积分）
- ✅ 清空积分按钮
- ✅ 自动监听截图变化（可手动勾选开启）
- ✅ 完整兼容 Windows 10 / Windows 11

启动：
```bash
python GUImain.py
```

运行效果：
```
+--------+------------+--------+--------+
| 排名   | 玩家ID     | 本次得分 | 累计积分 |
+--------+------------+--------+--------+
| 1      | 南山Su1ka | 10     | 80     |
| 2      | 铭扬腊球   | 7      | 65     |
...
```

---

## 📊 积分规则
| 排名 | 积分  | 特殊 |
|----|-----|------|
| 1  | 10  |      |
| 2  | 7   |      |
| 3  | 5   |      |
| 4  | 4   |      |
| 5  | 3   |      |
| 6  | 1   |      |
| 7  | 0   |      |
| 8  | -1  |      |
| X（未完成） | -5 | 直接识别并扣分 |

---

## 💻 使用说明（GUI模式）
1. 游戏内截图（1924×1119）保存至 `ScreenShots/`目录，命名任意
2. 双击运行 `GUImain.py`（支持 .exe 版本）
3. 点击“手动更新”或勾选“自动监听刷新”
4. 查看积分表实时更新
5. 可随时点击“清空积分”重置
6. 支持手动修正错识别ID，输入错ID和正ID，后续识别自动使用

---

## 🔧 核心技术
- PaddleOCR（支持中英文识别）
- PyQt5（桌面图形界面）
- pandas（数据处理）
- OpenCV（图像预处理）
- JSON存储 ID 映射设置

---

## 📂 历史积分自动保存：
所有积分自动累加保存至：
```
results/results.csv
```

---

## 🚀 未来计划
- ✅ 支持导出为 Excel
- ✅ 增加玩家信息管理功能
- ✅ 自动截图监听（无需手动刷新）
- ✅ 多场次历史数据可视化
---

## 📥 运行环境
```bash
pip install -r requirements.txt
```
支持 Windows 10 / Windows 11

---

## 💾 打包运行（可选）
```bash
pyinstaller --noconsole --onefile GUImain.py
```
生成 `dist/KartResultCalculator.exe`，直接双击运行！

---

