"""
The par file class
"""
from helpers import _get_names
from .namelist import Namelist

class Par:
    def __init__(self, namelists=[]):
        self.namelists = namelists
        
    def __repr__(self):
        namelists = ["%s"%n for n in self.namelists]
        s = "\n\n".join(namelists)
        return s
    
    def from_default(self, path):
        names = _get_names(path)
        self.namelists = [Namelist.from_default(path, n) for n in names]
    
    def from_file(self, path):
        """
        Clone Par from existing file

        Parameters
        ----------
        path : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """   
        names = _get_names(path)
        self.namelists = [Namelist.from_par_file(path, n) for n in names]
    
    
        
        
        