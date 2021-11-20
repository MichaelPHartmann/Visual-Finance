# import sys
# from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
# from PyQt5.QtGui import QPixmap
# from PyQt5 import QtGui, QtCore
# from PyQt5.QtGui import QCursor

import sys
from database import access
from PyQt5.QtWidgets import QRadioButton, QCheckBox, QMainWindow, QLabel, QComboBox, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class selectionScreenVF(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Visual Finance - Portfolio and Watchlist Viewer'
        self.setWindowTitle(self.title)
        self.setStyleSheet("background: 'lightgrey';")
        self.main_layout = QGridLayout()
        self.init_selection()

    def init_selection(self):
        # Create the elements for the initial page
        # Get the available tables from the SQL databases
        self.get_existing_tables()
        # Create the token entry box and label
        self.tokenbox()
        # Define simple elements
        self.sandbox_state = QCheckBox("SandBox Mode")
        self.portfolio_radio = QRadioButton("Portfolios")
        self.watchlist_radio = QRadioButton("Watchlists")
        self.selection_box = QComboBox()
        # Add elements to layout
        self.main_layout.addWidget(self.tokenbox_name,0,0)
        self.main_layout.addWidget(self.tokenbox,0,1)
        self.main_layout.addWidget(self.sandbox_state,0,2)
        self.main_layout.addWidget(self.selection_box, 1,0)
        self.main_layout.addWidget(self.portfolio_radio, 1,1)
        self.main_layout.addWidget(self.watchlist_radio, 1,2)
        # Set behaviour for toggling between the desired database
        self.portfolio_radio.toggled.connect(lambda:self.database_state(self.portfolio_radio))
        self.watchlist_radio.toggled.connect(lambda:self.database_state(self.watchlist_radio))
        # self.button.clicked.connect(self.on_click)
        self.setLayout(self.main_layout)
        self.show()

    def tokenbox(self):
        # Create text box for the IEX Cloud token to be entered into
        self.tokenbox_name = QLabel(self)
        self.tokenbox_name.setText('IEX Cloud Token:')
        self.tokenbox = QLineEdit(self)
        self.tokenbox.setStyleSheet("background: 'white';")
        # self.tokenbox.move(150, 20)
        self.tokenbox.resize(300,40)
        # self.tokenbox_name.move(20,20)
        self.tokenbox_name.resize(200, 40)

    def database_state(self, radio_button):
        if radio_button.text() == "Portfolios":
            if radio_button.isChecked() == True:
                self.selection_box.clear()
                self.selection_box.addItems(self.portfolio_tables)
                self.database_displayed = "Portfolio"
        if radio_button.text() == "Watchlists":
            if radio_button.isChecked() == True:
                self.selection_box.clear()
                self.selection_box.addItems(self.watchlist_tables)
                self.database_displayed = "Watchlist"

    def get_existing_tables(self):
        # Find all the table names in the portfolio database
        db = access.portfolioDB()
        self.portfolio_tables = db.tables
        # Find all the table names in the portfolio database
        db = access.watchlistDB()
        self.watchlist_tables = db.tables

class additionScreenVF(QWidget):
    def __init__(self):
        super().__init__()
        self.get_existing_tables()
        self.title = 'Visual Finance - Add to a Portfolio or Watchlist'
        self.setWindowTitle(self.title)
        self.setStyleSheet("background: 'lightgrey';")
        self.main_layout = QGridLayout()
        self.database_chosen = 'None'
        self.init_addition()
        self.show_addition_fields()

    def init_addition(self):
        self.sandbox_state = QCheckBox("SandBox Mode")
        self.portfolio_radio = QRadioButton("Portfolios")
        self.watchlist_radio = QRadioButton("Watchlists")
        self.selection_box = QComboBox()
        self.main_layout.addWidget(self.selection_box, 0,0)
        self.main_layout.addWidget(self.portfolio_radio, 0,1)
        self.main_layout.addWidget(self.watchlist_radio, 0,2)
        self.ticker_label = QLabel(self)
        self.ticker_label.setText('Ticker:')
        self.ticker_entry = QLineEdit(self)
        self.ticker_entry.setStyleSheet("background: 'white';")
        self.quantity_label = QLabel(self)
        self.quantity_label.setText('Quantity:')
        self.quantity_entry = QLineEdit(self)
        self.quantity_entry.setStyleSheet("background: 'white';")
        self.basis_label = QLabel(self)
        self.basis_label.setText('Basis Price:')
        self.basis_entry = QLineEdit(self)
        self.basis_entry.setStyleSheet("background: 'white';")
        self.enter_button = QPushButton("Save")
        # Set behaviour for toggling between the desired database
        self.portfolio_radio.toggled.connect(lambda:self.database_state(self.portfolio_radio))
        self.watchlist_radio.toggled.connect(lambda:self.database_state(self.watchlist_radio))
        self.setLayout(self.main_layout)
        self.show()

    def get_existing_tables(self):
        # Find all the table names in the portfolio database
        db = access.portfolioDB()
        self.portfolio_tables = db.tables
        # Find all the table names in the portfolio database
        db = access.watchlistDB()
        self.watchlist_tables = db.tables


    def database_state(self, radio_button):
        if radio_button.text() == "Portfolios":
            if radio_button.isChecked() == True:
                self.selection_box.clear()
                self.selection_box.addItems(self.portfolio_tables)
                self.database_chosen = "Portfolio"
                self.main_layout.addWidget(self.ticker_label,1,0)
                self.main_layout.addWidget(self.ticker_entry,1,1)
                self.main_layout.addWidget(self.quantity_label,2,0)
                self.main_layout.addWidget(self.quantity_entry,2,1)
                self.main_layout.addWidget(self.basis_label,3,0)
                self.main_layout.addWidget(self.basis_entry,3,1)
        else:# radio_button.text() == "Watchlists":
            if radio_button.isChecked() == True:
                self.selection_box.clear()
                self.selection_box.addItems(self.watchlist_tables)
                self.main_layout.addWidget(self.ticker_label,1,0)
                self.main_layout.addWidget(self.ticker_entry,1,1)
                self.database_chosen = "Watchlist"


    def show_addition_fields(self):

        self.main_layout.addWidget(self.enter_button,4,0,1,2)
        self.enter_button.clicked.connect(self.send_information)

    def send_information(self):
        ticker = self.ticker_entry.text().upper()
        quantity = int(self.quantity_entry.text())
        price_basis = float(self.basis_entry.text())
        # if database_chosen == 'Portfolio'

class App(selectionScreenVF, additionScreenVF):
    def __init__(self):
        additionScreenVF.__init__(self)


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
