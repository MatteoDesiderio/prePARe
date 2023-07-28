"""
The parameter file class
"""
import numpy as np
from collections import OrderedDict

def _get_fmt(value):
    v = np.r_[value]
    if v.dtype == str:
        s = "%s" % value
    elif v.dtype == bool:
        s = "%s" % ".true." if value else ".false."
    elif v.dtype == int:
        if value >= 1000:
            s = "%1.6e" % value
        else:
            s = "%i" % value
    elif v.dtype == float:
        if value >= 1000:
            s = "%1.6e" % value
        else:
            s = "%1.6f" % value
    else:
        raise TypeError("Value should be bool, int, float or str")
    return s

class Formatter:
    def __init__(self, value, name):
        self.value = value
        self.name = name
    
    def get_formatted(self):
        value = self.value
        name = self.name
        
        if isinstance(value, np.ndarray):
            if value.ndim == 1:
                n = ["%s(%i)" % (name, i + 1) for i in range(len(value))]
                s = [_get_fmt(v) for v in value]
            elif value.ndim == 2:
                n = ["%s(:, %i)" % (name, i + 1) for i in range(len(value))]
                s = [", ".join([_get_fmt(vv) for vv in v]) for v in value]
            else:
                raise NotImplementedError("ndim of parameter must be <= 2")
            
            _zip = zip(n, s)
            res = "\n".join(["%s=%s" % (nn, ss) for nn, ss in _zip])
            
        else:
            res = "%s=%s" % (name, _get_fmt(value))
        
        return res
            
        

class Parameter():
    def __init__(self, name, value, parent_namelist):
        self.name = name
        self.value = value
        self.parent_namelist = parent_namelist
    
    def __repr__(self):

        f = Formatter(self.value, self.name)
        s = f.get_formatted()
        # s = "%s=%s" % (self.name, self.value)
        return s  
