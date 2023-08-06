"""
Simply create the the dfault par file
"""
from PyQt5 import QtWidgets as qtw
from namelistQScroll import NamelistQScroll 
from objects.par import Par

class DefaultPar(Par):
    
    @staticmethod
    def default():
        par = DefaultPar()
        par.from_default("defaults_include")
        return par
        
    def getNamelistScroll(self):
    
        scroll = NamelistQScroll()
        scroll.setWidgetResizable(True)
        
        scrollContent = qtw.QWidget(scroll)
        
        scrollLayout = qtw.QVBoxLayout(scrollContent)
        scrollContent.setLayout(scrollLayout)
        for namelist in self.namelists:
            button = qtw.QPushButton(namelist.name)
            button.setCheckable(True)
            scrollLayout.addWidget(button)
            
        scroll.setWidget(scrollContent)
        
        return scroll        
            
