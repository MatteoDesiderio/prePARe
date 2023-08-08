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

    def getNamelistList(self):
        scroll = qtw.QListWidget()
        for namelist in self.namelists:
            scroll.addItem(namelist.name)

        return scroll
