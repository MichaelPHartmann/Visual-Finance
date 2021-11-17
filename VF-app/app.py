import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtGui, QtCore

widgets = {
"logo": [],
"button": [],
"score": [],
"question": [],
"answer1":[],
"answer2":[],
"answer3":[]}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Visual Finance")
# window.setFixedWidth(1000)
window.move(200, 200)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()
window.setLayout(grid)

class VisualFinance():
    def __init__(self):
        self.app_name = "Visual Finance"

        app = QApplication(sys.argv)
        window = QWidget()
        window.setWindowTitle(self.app_name)
        # window.setFixedWidth(1000)
        window.move(200, 200)
        window.setStyleSheet("background: #161219;")
        grid = QGridLayout()
        window.setLayout(grid)

def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

def start_game():
    clear_widgets()
    frameTwo()

def show_frame_one():
    clear_widgets()
    frameOne()

def create_buttons(answer):
    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(100)
    button.setStyleSheet(
    "*{border: 4px solid '#BC006C';"+
    "color: white;"+
    "font-family: 'shanti';"+
    "font-size: 16px;"+
    "border-radius: 25px;"+
    "padding: 25px 0;"+
    "margin-top: 20px;}"+
    "*:hover{background: '#BC006C';}"
    )
    button.clicked.connect(show_frame_one)
    return button

def frameOne():
    # Display Logo
    pixmap = QPixmap('FinMesh_Logo.png')
    image = pixmap.scaled(250, 250, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-bottom: 5px")
    window.resize(image.width()+50,image.height()+100)
    widgets["logo"].append(logo)


    # Button Widget
    button = QPushButton("Play")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
    "*{border: 4px solid '#BC006C';" +
    "border-radius: 45px;" +
    "font-size: 35px;" +
    "color: white;" +
    "padding: 25px 0;" +
    "margin: 50px 50px;}" +
    "*:hover{background: '#BC006C';}")

    button.clicked.connect(start_game)
    widgets["button"].append(button)
    # button.setHover

    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)

def frameTwo():
    score = QLabel("80")
    score.setAlignment(QtCore.Qt.AlignRight)
    score.setStyleSheet(
    "font-size: 35px;"+
    "color: 'white';"+
    "padding: 20px 10px;"+
    "margin: 20px 50px;"+
    "background: '#64A314';"+
    "border: 1px solid '#64A314';"+
    "border-radius: 40px;"+
    "text-align: left;"
    )
    widgets["score"].append(score)

    question = QLabel("Placeholder text will go here")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
    "font-family: Shanti;"+
    "font-size: 25px;"+
    "color: 'white';"+
    "padding: 75px;"
    )
    widgets["question"].append(question)

    button1 = create_buttons("Answer1")
    button2 = create_buttons("Answer2")
    button3 = create_buttons("Answer3")

    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)
    widgets["answer3"].append(button3)

    grid.addWidget(widgets["score"][-1], 0, 1)
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["answer1"][-1], 2, 0)
    grid.addWidget(widgets["answer2"][-1], 2, 1)


frameOne()
# frameTwo()
window.show()

sys.exit(app.exec())
