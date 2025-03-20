from PyQt5.QtWidgets import QTableWidgetItem
import pandas as pd
from module.save_results import load_scores

class TableManager:
    def __init__(self, table_widget):
        self.table = table_widget

    def load_scores(self):
        df = load_scores('./results/results.csv')
        if not df.empty:
            self.table.setRowCount(len(df))
            self.table.setColumnCount(len(df.columns))
            self.table.setHorizontalHeaderLabels(df.columns)
            for row in range(len(df)):
                for col in range(len(df.columns)):
                    self.table.setItem(row, col, QTableWidgetItem(str(df.iloc[row, col])))
        else:
            self.table.clear()
            self.table.setRowCount(0)