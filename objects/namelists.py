from collections import OrderedDict
from helpers import _get_raw_lines
from .par import Par
from .parameter import Parameter
import numpy as np

class Namelist:
    def __init__(self, parameters=[]):
        
        if not isinstance(parameters, list):
            raise TypeError
            
        try:
            name = parameters[0].parent_namelist
            parent_names = np.r_[[p.parent_namelist for p in parameters]]
            if np.any(parent_names != name):
                raise ValueError("Attempting to join parameters from "+
                                 "different namelists")
            
        except IndexError:
            name = ""
        
        names_seen = []
        seen = []
        for p in parameters[::-1]:
            pn = p.name
            if not( pn in names_seen):
                seen += [p]
                names_seen += [pn]
                
        if seen:         
            parameters = seen[::-1]
        
        self.parameters = parameters
        self.name = name
        
        
    @staticmethod
    def from_file(path, name):
        raw_lines = _get_raw_lines(path)
        start = raw_lines.index("!&" + name + "\n") + 1
        sel_lines = []
        for line in raw_lines[start:]:
            if line[:2] == "!&":
                break
            no_nline = line.replace("\n", "")
            if no_nline[0] != "!":
                sel_lines.append(no_nline)
        # instantiate Namelist for each namelist in the par file

        # return Namelist(name, parameters)

    def __add__(self, other):
        if isinstance(other, Parameter):
            name = other.parent_namelist
            myname = self.name
            if myname == "":
                return Namelist([other])
            elif name == self.name:
                new = self.parameters + [other]
                return Namelist(new)
            else:
                raise ValueError("Attempting to join parameters from "+
                                 "different namelists")
                
        elif isinstance(other, Namelist):
            if self.name == other.name:
                new = self.parameters + other.parameters
                return Namelist(new)
            else:
                return Par([self, other])
    
    def __repr__(self):
        name = self.name
        h = "&%s\n" % name
        b = "\n".join(["%s"%s for s in self.parameters ])
        f = "\n&end"
        return h + b + f
        
