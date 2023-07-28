"""
Actions for the menu bar
"""
from PyQt5 import QtWidgets as qtw 
from objects.project import create_new_project

# App actions
def quit_action(mainWindow):
	quit = qtw.QAction("&Quit", mainWindow) # instantiate
	quit.setShortcut("Ctrl+Alt+Q") # assign shortcut
	quit.setStatusTip("Leave application") # assign a status bar tip
	quit.triggered.connect(mainWindow.close_application) # what it does
	return quit

def about_action(mainWindow):
	about = qtw.QAction("&About", mainWindow) # instantiate
	about.setStatusTip("About this Application") # assign a status bar tip
	# show a window with info  about version ecc
	#quit.triggered.connect(mainWindow.close_application) # what it does
	return about 

# File actions
def new_file_action(mainWindow):
	new_file = qtw.QAction("&New File", mainWindow) # instantiate
	new_file.setShortcut("Ctrl+N") # assign shortcut
	new_file.setStatusTip("Create New Project") # assign a status bar tip
	new_file.triggered.connect(create_new_project)
	return new_file

def save_file_action(mainWindow):
	save_file = qtw.QAction("&Save File", mainWindow) # instantiate
	save_file.setShortcut("Ctrl+S") # assign shortcut
	save_file.setStatusTip("Save Current Project") # assign a status bar tip
	#save_file.triggered.connect(save_project)
	return save_file

# Edit actions

# Namelists actions 

# Window actions

# Help actions