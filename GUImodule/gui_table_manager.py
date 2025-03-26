# GUImodule/gui_table_manager.py
from PyQt5.QtWidgets import QTableWidgetItem
import pandas as pd
from PyQt5 import QtGui


class TableManager:
    def __init__(self, table_widget):
        self.table_widget = table_widget

    def update_table(self, df: pd.DataFrame):
        """
        更新表格内容
        """
        self.table_widget.clear()
        self.table_widget.setRowCount(len(df))
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["玩家", "累计积分"])

        for row in range(len(df)):
            player_item = QTableWidgetItem(str(df.iloc[row]['玩家']))
            score_item = QTableWidgetItem(str(df.iloc[row]['累计积分']))

            # 分数颜色高亮（正绿、负红）
            if int(df.iloc[row]['累计积分']) > 0:
                score_item.setForeground(QtGui.QColor('green'))
            elif int(df.iloc[row]['累计积分']) < 0:
                score_item.setForeground(QtGui.QColor('red'))

            self.table_widget.setItem(row, 0, player_item)
            self.table_widget.setItem(row, 1, score_item)

        self.table_widget.resizeColumnsToContents()

    def clear_table(self):
        """
        清空表格
        """
        self.table_widget.clear()
        self.table_widget.setRowCount(0)

    def get_all_players(self):
        """
        获取当前表格中所有玩家ID（用于模糊匹配）
        """
        players = []
        for row in range(self.table_widget.rowCount()):
            player_item = self.table_widget.item(row, 0)
            if player_item:
                players.append(player_item.text())
        return players