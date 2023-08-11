from PyQt5 import QtWidgets as qtwfrom PyQt5.QtCore import Qtfrom objects.namelist import Namelist class ParametersView(qtw.QFrame):    def __init__(self, default_namelist):        super().__init__()        self.default_namelist = default_namelist        self.default_parameters = default_namelist.parameters        self.namelist = Namelist()        self.boxes = {p.name:parameterBox(p) for p in self.default_parameters}        self.layout = qtw.QVBoxLayout()        for p in self.boxes:            self.layout.addWidget(self.boxes[p])        self.layout.addStretch()        self.layout.setSpacing(5)        self.setLayout(self.layout)    def show(self, name):        box = self.boxes[name]        if box.isHidden():            box.show()                def hide(self, name):        box = self.boxes[name]        if not box.isHidden():            box.hide()class parameterBox(qtw.QGroupBox):    def __init__(self, parameter):        super().__init__()        #self.setFixedHeight(45)        self.parameter = parameter        self.layout = qtw.QHBoxLayout()        self.layout.addWidget(qtw.QLabel(self.parameter.name))        self.setLayout(self.layout)        # self.layout.setContentsMargins(0, 0, 0, 0)        # self.setContentsMargins(0, 0, 0, 0)        self.hide()    