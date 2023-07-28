"""
Same thing as before, but using OOP
"""
import sys
import time
from PyQt5 import QtGui, QtCore  # the latter is for handling events
from PyQt5 import QtWidgets as qtw


class Window(qtw.QMainWindow):
    """
    """

    def __init__(self):

        super().__init__()
        # then we design our window
        self.setGeometry(0, 0, 300, 500)
        self.setWindowTitle("Finestra Principale")
        self.setWindowIcon(QtGui.QIcon("logo.png"))

        # define an action, that can be triggered by a menu
        # (might be better practice to define a function in another file
        quitAction = qtw.QAction("&Quit MyApp", self)  # instantiate
        quitAction.setShortcut("Ctrl+Alt+Q")  # assign shortcut
        # assign a status bar tip
        quitAction.setStatusTip("Leave this application")
        quitAction.triggered.connect(self.close_application)  # what it does
        self.statusBar()  # create a status bar in the main window

        # instantiate a menu bar
        # (might be better practice to define a function in another file
        mainMenu = self.menuBar()  # instantiate the menu bar
        mainMenu.setNativeMenuBar(False)
        fileMenu = mainMenu.addMenu('&File')  # add the "File" menu
        fileMenu.addAction(quitAction)  # attach action to the "File" menu

        # instantiate another menu bar 4 fun
        fileMenu = mainMenu.addMenu('&CozzePelose')  # add this menu
        fileMenu.addAction(quitAction)  # attach action to this menu

        # bellurie
        self.home()  # draw the main window

    def home(self):
        """
        Design/show the main window appearance
        """
        btn = qtw.QPushButton("Quit", self)
        # you can put your custom "quit" function here
        btn.clicked.connect(self.close_application)
        btn.move(0, 200)
        btn.resize(100, 50)

        quitAction = qtw.QAction(QtGui.QIcon("icon.png"), "Nooo", self)
        quitAction.triggered.connect(self.close_application)

        self.toolBar = self.addToolBar("My Tool Bar")
        self.toolBar.addAction(quitAction)

        # checkbox
        checkBox = qtw.QCheckBox("Resize", self)
        checkBox.move(100, 100)
        checkBox.stateChanged.connect(self.enlarge_window)
        checkBox.toggle()
        # progress bar
        self.progress = qtw.QProgressBar(self)
        self.progress.setGeometry(100, 249, 100, 10)
        # button for progress
        self.btn = qtw.QPushButton("Download", self)
        self.btn.move(100, 260)
        self.btn.clicked.connect(self.download)

        # Multiple choice button
        items = qtw.QStyleFactory.keys()
        self.cbox = qtw.QComboBox(self)
        self.cbox.setGeometry(210, 200, 150, 50)
        self.cbox.addItems(items)
        # the dict syntax allows you to choose the type
        # of parameter passed onto the connected function
        # (str or int). In other words, if we pass the
        # index (int) of the selected item in the combo box
        # or the actual name of the item (str)

        self.cbox.activated[str].connect(self.change_style)

        self.show()

    def change_style(self, text):
        qtw.QApplication.setStyle(qtw.QStyleFactory.create(text))

    def download(self):
        completed = 0.0
        self.progress.setValue(completed)
        while completed < 100:
            # needed for some reason in the loop
            # otherwise it's gonna get stuck
            # and get unstuck only when the
            # loop is exited
            qtw.QApplication.processEvents()
            completed += 1
            self.progress.setValue(completed)
            time.sleep(.01)

    def close_application(self):
        options = qtw.QMessageBox.No | qtw.QMessageBox.Yes
        choice = qtw.QMessageBox.question(self, "Exiting",
                                          "Sicuro sicuro?", options)

        if choice == qtw.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(0, 0, 500, 700)
        else:
            self.setGeometry(0, 0, 300, 500)


def run():
    app = qtw.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
