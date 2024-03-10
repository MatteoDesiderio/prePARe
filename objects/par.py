"""
The par file class
"""
from helpers import _get_names, _fill_in_array_shapes
from .namelist import Namelist

class Par:
    def __init__(self, namelists=[]):
        self.namelists = namelists
        
    def __repr__(self):
        namelists = ["%s"%n for n in self.namelists]
        s = "\n\n".join(namelists)
        return s
    
    def from_file(self, path):
        names = _get_names(path)
        namelists = [Namelist.from_file(path, n) for n in names]
        
        self.namelists = _fill_in_array_shapes(namelists)
