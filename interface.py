import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget

class MinesweeperWindow(QMainWindow):
    def __init__(self, size, mines):
        super().__init__()
        self.size = size
        self.mines = mines
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100, 100, 500, 500)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(central_widget)

        self.labels = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                label = QLabel(" ", central_widget)
                grid_layout.addWidget(label, i, j)
                row.append(label)
            self.labels.append(row)

        self.show()

app = QApplication(sys.argv)
window = MinesweeperWindow(8, 10)
sys.exit(app.exec_())