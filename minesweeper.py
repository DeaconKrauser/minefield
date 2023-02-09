import random
from PyQt5 import QtWidgets, QtGui

class Minefield(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.grid = QtWidgets.QGridLayout()
        self.buttons = []
        self.mines = []
        
        for i in range(10):
            self.buttons.append([])
            for j in range(10):
                button = QtWidgets.QPushButton("", self)
                button.clicked.connect(lambda state, x=i, y=j: self.reveal(x, y))
                self.grid.addWidget(button, i, j)
                self.buttons[i].append(button)
        
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.centralWidget().setLayout(self.grid)
        
        self.place_mines()
        
    def place_mines(self):
        for i in range(10):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            self.mines.append((x, y))
            
    def reveal(self, x, y):
        if (x, y) in self.mines:
            self.buttons[x][y].setText("X")
            self.buttons[x][y].setEnabled(False)
            self.end_game()
        else:
            count = self.count_mines(x, y)
            self.buttons[x][y].setText(str(count))
            self.buttons[x][y].setEnabled(False)
            
    def count_mines(self, x, y):
        count = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if (i, j) in self.mines:
                    count += 1
        return count
    
    def end_game(self):
        for i in range(10):
            for j in range(10):
                self.buttons[i][j].setEnabled(False)
        
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle("Game Over")
        msg_box.setText("Você perdeu. Tente novamente.")
        msg_box.addButton(QtWidgets.QPushButton("Reiniciar"), QtWidgets.QMessageBox.YesRole)
        msg_box.exec_()
        
        if msg_box.clickedButton().text() == "Reiniciar":
            self.restart_game()
        
    def restart_game(self):
        for i in range(10):
            for j in range(10):
                self.buttons[i][j].setText("")
                self.buttons[i][j].setEnabled(True)
        self.mines.clear()
        self.place_mines()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Minefield()
    window.show()
    app.exec_()

