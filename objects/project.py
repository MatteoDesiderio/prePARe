"""
Project Class
"""
from helpers import _get_raw_lines
from .namelists import Namelist
from .par import Par


class Project:
    def __init__(self, par=Par()):
        self.par = par

    def save(self):
        pass

    def from_file(self, path):
        raw_lines = _get_raw_lines(path)
        def x(l): return l[:2] == "!&"
        names = filter(x, raw_lines)
        names = [n.replace("\n", "").replace("!&", "") for n in names]
        print(names)
        names[:2]
        namelists = [Namelist.from_file(path, n) for n in names]
        # self.par = Par(namelists)
        # TO DO some magic to read the file and store
        #			 	 each namelist as a sep class
        # join all namelists in a list
        # TO DO self.namelists = namelists


def create_new_project():
    print("I created a new project")
    proj = Project()
    proj.from_file("defaults_include")
