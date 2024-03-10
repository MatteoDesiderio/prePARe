from collections import OrderedDict
import numpy as np
from helpers import _get_raw_lines
from .parameter import Parameter
from .parameterFactory import dispatch


def _join_split_arrays(parameters):
    for p in parameters:
        splitname = p.name.rsplit("(")

class Namelist:
    def __init__(self, parameters=[]):
        if not isinstance(parameters, list):
            raise TypeError

        try:
            name = parameters[0].parent_namelist
            parent_names = np.r_[[p.parent_namelist for p in parameters]]
            if np.any(parent_names != name):
                raise ValueError("Attempting to join parameters from " +
                                 "different namelists")

        except IndexError:
            name = ""
            
        # dont remember what this is for - avoid duplicates?
        names_seen = []
        seen = []
        for p in parameters[::-1]:
            pn = p.name
            if not(pn in names_seen):
                seen += [p]
                names_seen += [pn]
        if seen:
            parameters = seen[::-1]
        # ------------------------------
        
        self.parameters = parameters
        self.name = name
    
    def __add__(self, other):
        if isinstance(other, Parameter):
            name = other.parent_namelist
            myname = self.name
            if myname == "":
                return Namelist([other])
            elif name == self.name:
                if not other in self.parameters: 
                    new = self.parameters + [other]
                return Namelist(new)
            else:
                raise ValueError("Attempting to join parameters from " +
                                 "different namelists")

        elif isinstance(other, Namelist):
            if self.name == other.name:
                new = self.parameters + other.parameters
                return Namelist(new)
            else:
                raise ValueError("Attempting to join different namelists")
                # return Par([self, other])


    def __repr__(self):
        name = self.name
        h = "&%s\n" % name
        b = "\n".join(["%s" % s for s in self.parameters])
        f = "\n&end"
        return h + b + f


    @staticmethod
    def from_default(path, name):
        raw_lines = _get_raw_lines(path)
        start = raw_lines.index("!&" + name + "\n") + 1
        sel_lines = []
        parameters = []
        for line in raw_lines[start:]:
            if line[:2] == "!&":
                break
            no_nline = line.replace("\n", "")
            if no_nline[0] != "!":
                sel_lines.append(no_nline)
                nameP, valueP = no_nline.rsplit("=")
                param = dispatch(nameP, valueP, name, parameters)
                parameters.append(param)
                      
        return Namelist(parameters)
                
    @staticmethod
    def from_par_file(path, name):
        """
        As from_default, but from an existing par file

        Parameters
        ----------
        path : TYPE
            DESCRIPTION.
        name : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """

        pass
