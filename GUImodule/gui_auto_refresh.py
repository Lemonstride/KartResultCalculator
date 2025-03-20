from PyQt5.QtCore import QTimer

class AutoRefresh:
    def __init__(self, callback, interval=3000):
        self.timer = QTimer()
        self.timer.timeout.connect(callback)
        self.interval = interval

    def start(self):
        self.timer.start(self.interval)

    def stop(self):
        self.timer.stop()