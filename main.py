"""
Main program
"""
import sys
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets as qtw
from menuActions import *
from default_par import DefaultPar
from PyQt5.QtGui import QPalette, QColor
from namelistsList import NamelistsList
from namelistStack import NamelistStack


def create_menus(mainMenu):
    """
    Helper function to create menus stored in easily accessible
    dictionary
    """
    names=["App Name", "File", "Edit", "Namelists", "Window", "Help"]
    menus = {n: mainMenu.addMenu("&" + n) for n in names}
    return menus


class Window(qtw.QMainWindow):
    def __init__(self, screensize):
        super().__init__()
        self.defaultPar = DefaultPar().default()
        self.available_namelists = self.defaultPar.namelists
        self.names = [n.name for n in self.available_namelists]
        
        
        self.screensize = screensize

        # window size and position
        whole_screen = self.get_geom_from_screen()
        self.setGeometry(*whole_screen)
        # create a status bar in the main window
        self.statusBar()
        # instantiate a menu bar
        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)

        menus = create_menus(mainMenu)
        # add some actions to each menu
        # App
        quit = quit_action(self)
        about = about_action(self)
        menus["App Name"].addAction(about)
        menus["App Name"].addAction(quit)
        # File
        new_file = new_file_action(self)
        save_file = save_file_action(self)
        menus["File"].addAction(new_file)
        menus["File"].addAction(save_file)

        mainStack = NamelistStack(self.defaultPar)
        # Uncomment to see the space taken:
        # mainStack.setFrameShape(qtw.QFrame.StyledPanel)

        leftList = NamelistsList(self.defaultPar, mainStack)
        # leftList.setFrameShape(qtw.QFrame.StyledPanel)

        splitter = qtw.QSplitter(QtCore.Qt.Horizontal)
        splitter.addWidget(leftList)
        splitter.addWidget(mainStack)
        #splitter.setStretchFactor(1, 5)
        dx = whole_screen[3]
        splitter.setSizes([int(dx / 100), int(67 * dx / 100)])

        self.setCentralWidget(splitter)
        self.show()  # draw the main window

    def get_geom_from_screen(self):
        dx, dy = self.screensize.width(), self.screensize.height()
        return 0, 0, dx, dy

    def close_application(self):
        """
        Method to close app
        """
        # Add cases: did you save the project yet?
        options = qtw.QMessageBox.No | qtw.QMessageBox.Yes
        choice = qtw.QMessageBox.question(self, "Leaving Application",
                                          "Are you sure?", options)

        if choice == qtw.QMessageBox.Yes:
            sys.exit()
        else:
            pass


def run():
    app = qtw.QApplication(sys.argv)
    screen = app.primaryScreen()
    GUI = Window(screen.size())
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
