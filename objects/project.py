"""
Project Class
"""
from helpers import _get_raw_lines
from .par import Par
from .namelist import Namelist
from default_par import _defaultPar_

class Project:
    def __init__(self, par=Par()):
        self.par = par

    def save(self):
        pass

def create_new_project():
    print("I created a new project")
    proj = Project()
    return proj