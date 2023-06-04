from PyQt6.QtWidgets import QApplication, QWidget

#for command line args
import sys

#only need 1 Qapp instance per app
#pass sys.argv to allow command line arg for app
# if you know you wont use command line args, QApplication[] works too
app = QApplication(sys.argv)

#create a Qt widget, which will be the window

window = QWidget()
window.show() #because windows are hidden by default

#start event loop
app.exec()

#your app wont reach here til you exit and the event loop has stopped

