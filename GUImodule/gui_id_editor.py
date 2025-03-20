from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit
from module.id_mapping import add_mapping

class IdEditDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("手动更正ID映射")
        self.resize(450, 300)

        layout = QVBoxLayout()

        self.old_id_label = QLabel("识别错误的ID（可直接从表格复制）：")
        self.old_id_input = QLineEdit()
        layout.addWidget(self.old_id_label)
        layout.addWidget(self.old_id_input)

        self.correct_id_label = QLabel("正确的ID（请输入修正后的ID）：")
        self.correct_id_input = QLineEdit()
        layout.addWidget(self.correct_id_label)
        layout.addWidget(self.correct_id_input)

        self.hint_label = QLabel("提示：保存后，后续所有相同错误ID将自动替换为正确ID")
        layout.addWidget(self.hint_label)

        self.save_btn = QPushButton("保存映射")
        self.save_btn.clicked.connect(self.save_mapping)
        layout.addWidget(self.save_btn)

        self.setLayout(layout)

    def save_mapping(self):
        wrong_id = self.old_id_input.text().strip()
        correct_id = self.correct_id_input.text().strip()
        if wrong_id and correct_id:
            add_mapping(wrong_id, correct_id)
            QMessageBox.information(self, "成功", f"已将 '{wrong_id}' 映射为 '{correct_id}'")
            self.accept()
        else:
            QMessageBox.warning(self, "输入错误", "请填写完整后再保存")
