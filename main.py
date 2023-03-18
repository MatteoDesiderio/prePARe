"""

"""
import sys  
import time
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets as qtw 

def createMenus(mainMenu, names=["App Name", "File", "Edit", 
                                 "Namelists", "Window", "Help"]):
    """
    Helper function to create menus stored in easily accessible
    dictionary
    """
    fun = lambda n : "&" + n
    menus = {n : mainMenu.addMenu(fun(n)) for n in names}
    return menus

def assignActions(menus):
    pass

class Window(qtw.QMainWindow):
    def __init__(self, screensize):
        super().__init__()
        self.screensize = screensize

        # window size and position
        dx, dy = 500, 300 # size
        self.setGeometry(*self.getWinGeomFromScreen(dx, dy))
        # create a status bar in the main window
        self.statusBar() 
        # instantiate a menu bar
        mainMenu = self.menuBar() 
        mainMenu.setNativeMenuBar(False)

        menus = createMenus(mainMenu)

        # add some actions to the 

        self.show() # draw the main window

    def getWinGeomFromScreen(self, dx, dy):
        x, y = self.screensize.width(), self.screensize.height()
        return int((x - dx) / 2), int((y - dy) / 2), dx, dy 


def run():
    app = qtw.QApplication(sys.argv)
    screen = app.primaryScreen()
    GUI = Window(screen.size())
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()

