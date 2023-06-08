from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow #, QWidget

#for command line args
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To Do Cat")
        button = QPushButton("Meow")
        
        #sets size restraints on the window
        #also setMax, setFixed
        #can resize any widget
        self.setMinimumSize(QSize(800, 600))


        #sets central widget of the window
        self.setCentralWidget(button)


#only need 1 Qapp instance per app
#pass sys.argv to allow command line arg for app
# if you know you wont use command line args, QApplication[] works too

app = QApplication(sys.argv)

#create a Qt widget, which will be the window

#window = QWidget() #for making only a window
#window = QPushButton("Kitty!") #creates a window wiht a button push
window = MainWindow()
window.show() #because windows are hidden by default

#start event loop
app.exec()

#your app wont reach here til you exit and the event loop has stopped

