from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow #, QWidget

#for command line args
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._buttonChecked = True
        self.setWindowTitle("To Do Cat")
        self._button = QPushButton("Meow")
        
        #sets size restraints on the window
        #also setMax, setFixed
        #can resize any widget
        self.setMinimumSize(QSize(800, 600))

        #sets central widget of the window
        
        self._button.setCheckable(True) #allows toggling of "Checked". Set to True = can toggle between T and F. Set to False = stays false.
        self._button.released.connect(self.buttonClicked)
        #self.button.released.connect(self.buttonReleased)
        #self.button.clicked.connect(self.buttonToggled) #slot 2 for BUTTON
        #self.button.setChecked(self._buttonChecked) #slot 1 for BUTTON

        self.setCentralWidget(self._button)

    def buttonClicked(self):
        print("Button clicked!")
        self._button.setText("Woof")
        self._button.setEnabled(False) #deactivates the button
        self.setWindowTitle("Sad Cat")

    def buttonToggled(self, checked): #check refers to the T or F checked state of the button
        self._buttonChecked = checked #this now changes the variable to T or F
        print("Checked?", self._buttonChecked)

    def buttonReleased(self):
        self.buttonChecked = self.button.isChecked()
        print("Release", self.buttonChecked)

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

