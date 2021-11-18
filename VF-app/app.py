# import sys
# from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
# from PyQt5.QtGui import QPixmap
# from PyQt5 import QtGui, QtCore
# from PyQt5.QtGui import QCursor

import sys
from database import access
from PyQt5.QtWidgets import QMainWindow, QLabel, QComboBox, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Visual Finance'
        # self.left = 10
        # self.top = 10
        # self.width = 500
        # self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setStyleSheet("background: 'lightgrey';")
        self.main_layout = QGridLayout()
        self.get_existing_tables()
        self.tokenbox()
        self.textbox_button()
        self.drop_down_menu()
        self.main_layout.addWidget(self.tokenbox,0,1)
        self.main_layout.addWidget(self.tokenbox_name,0,0)
        self.main_layout.addWidget(self.selection_box, 1,0,1,2)
        # self.button.clicked.connect(self.on_click)
        self.setLayout(self.main_layout)
        self.show()

    def tokenbox(self):
        # Create textbox
        self.tokenbox_name = QLabel(self)
        self.tokenbox_name.setText('IEX Cloud Token:')
        self.tokenbox = QLineEdit(self)
        self.tokenbox.setStyleSheet("background: 'white';")
        self.tokenbox.move(150, 20)
        self.tokenbox.resize(300,40)
        self.tokenbox_name.move(20,20)
        self.tokenbox_name.resize(200, 40)

    def drop_down_menu(self):
        self.selection_box = QComboBox()
        self.selection_box.addItems(self.portfolio_tables)

    def textbox_button(self):
        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20,80)

    def get_existing_tables(self):
        db = access.portfolioDB()
        self.portfolio_tables = db.tables
        
        db = access.watchlistDB()
        self.watchlist_tables = db.tables

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.tokenbox.text()
        QMessageBox.question(self, 'Message', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.tokenbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


#
# #global dictionary of dynamically changing widgets
# widgets = {
#     "logo": [],
#     "button": [],
#     "score": [],
#     "question": [],
#     "answer1": [],
#     "answer2": [],
#     "answer3": [],
#     "answer4": []
# }
#
# #initiallize GUI application
# app = QApplication(sys.argv)
#
# #window and settings
# window = QWidget()
# window.setWindowTitle("Who wants to be a programmer???")
# window.setFixedWidth(1000)
# window.move(2700, 200)
# window.setStyleSheet("background: #161219;")
#
# #initialliza grid layout
# grid = QGridLayout()
#
# def clear_widgets():
#     ''' hide all existing widgets and erase
#         them from the global dictionary'''
#     for widget in widgets:
#         if widgets[widget] != []:
#             widgets[widget][-1].hide()
#         for i in range(0, len(widgets[widget])):
#             widgets[widget].pop()
#
# def show_frame1():
#     '''display frame 1'''
#     clear_widgets()
#     frame1()
#
# def start_game():
#     '''display frame 2'''
#     clear_widgets()
#     frame2()
#
# def create_buttons(answer, l_margin, r_margin):
#     '''create identical buttons with custom left & right margins'''
#     button = QPushButton(answer)
#     button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
#     button.setFixedWidth(485)
#     button.setStyleSheet(
#         #setting variable margins
#         "*{margin-left: " + str(l_margin) +"px;"+
#         "margin-right: " + str(r_margin) +"px;"+
#         '''
#         border: 4px solid '#BC006C';
#         color: white;
#         font-family: 'shanti';
#         font-size: 16px;
#         border-radius: 25px;
#         padding: 15px 0;
#         margin-top: 20px}
#         *:hover{
#             background: '#BC006C'
#         }
#         '''
#     )
#     button.clicked.connect(show_frame1)
#     return button
#
# def frame1():
#     #logo widget
#     image = QPixmap("logo.png")
#     logo = QLabel()
#     logo.setPixmap(image)
#     logo.setAlignment(QtCore.Qt.AlignCenter)
#     logo.setStyleSheet("margin-top: 100px;")
#     widgets["logo"].append(logo)
#
#     #button widget
#     button = QPushButton("PLAY")
#     button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
#     button.setStyleSheet(
#         '''
#         *{
#             border: 4px solid '#BC006C';
#             border-radius: 45px;
#             font-size: 35px;
#             color: 'white';
#             padding: 25px 0;
#             margin: 100px 200px;
#         }
#         *:hover{
#             background: '#BC006C';
#         }
#         '''
#     )
#     #button callback
#     button.clicked.connect(start_game)
#     widgets["button"].append(button)
#
#     #place global widgets on the grid
#     grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
#     grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)
#
# def frame2():
#     #score widget
#     score = QLabel("80")
#     score.setAlignment(QtCore.Qt.AlignRight)
#     score.setStyleSheet(
#         '''
#         font-size: 35px;
#         color: 'white';
#         padding: 15px 10px;
#         margin: 20px 200px;
#         background: '#64A314';
#         border: 1px solid '#64A314';
#         border-radius: 35px;
#         '''
#     )
#     widgets["score"].append(score)
#
#     #question widget
#     question = QLabel("Placeholder text will go here blah blah")
#     question.setAlignment(QtCore.Qt.AlignCenter)
#     question.setWordWrap(True)
#     question.setStyleSheet(
#         '''
#         font-family: Shanti;
#         font-size: 25px;"
#         color: 'white';"
#         padding: 75px;
#         '''
#     )
#     widgets["question"].append(question)
#
#     #answer button widgets
#     button1 = create_buttons("answer1", 85, 5)
#     button2 = create_buttons("answer2", 5, 85)
#     button3 = create_buttons("answer3", 85, 5)
#     button4 = create_buttons("answer4", 5, 85)
#
#     widgets["answer1"].append(button1)
#     widgets["answer2"].append(button2)
#     widgets["answer3"].append(button3)
#     widgets["answer4"].append(button4)
#
#     #logo widget
#     image = QPixmap("logo_bottom.png")
#     logo = QLabel()
#     logo.setPixmap(image)
#     logo.setAlignment(QtCore.Qt.AlignCenter)
#     logo.setStyleSheet("margin-top: 75px; margin-bottom: 30px;")
#     widgets["logo"].append(logo)
#
#     #place widget on the grid
#     grid.addWidget(widgets["score"][-1], 0, 1)
#     grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
#     grid.addWidget(widgets["answer1"][-1], 2, 0)
#     grid.addWidget(widgets["answer2"][-1], 2, 1)
#     grid.addWidget(widgets["answer3"][-1], 3, 0)
#     grid.addWidget(widgets["answer4"][-1], 3, 1)
#     grid.addWidget(widgets["logo"][-1], 4, 0, 1,2)
#
# #display frame 1
# frame1()
#
# window.setLayout(grid)
#
# window.show()
# sys.exit(app.exec()) #terminate the app
