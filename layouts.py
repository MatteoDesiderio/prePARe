from PyQt5 import QtWidgets as qtw

def build_tabs(titles, widgets):
    # a tab widget does all the work for you
    tab = qtw.QTabWidget()
    # set position
    tab.setTabPosition(qtw.QTabWidget.North)
    # can we arrange the tabs?
    tab.setMovable(True)
    # Only makes a difference on Mac
    # tab.setDocumentMode(True)
    
    for t, w in zip(titles, widgets):
        # then a simple method is enough to add options to
        # to the tab widget
        tab.addTab(w, t)
    
    return tab