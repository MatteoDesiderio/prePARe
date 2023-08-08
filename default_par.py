"""
Simply create the the dfault par file
"""
from PyQt5 import QtWidgets as qtw
from objects.par import Par


class DefaultPar(Par):

    @staticmethod
    def default():
        par = DefaultPar()
        par.from_default("defaults_include")
        return par
