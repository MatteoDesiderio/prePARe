"""
The parameter file class
"""
import numpy as np
from collections import OrderedDict

def _get_fmt_(value):
    v = np.array([value])
    if v.dtype.type == np.str_:
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

def formatSingle(value, dtype):
    if dtype == str:
        s = "%s" % value
    elif dtype == bool:
        s = "%s" % ".true." if value else ".false."
    elif dtype == int:
        if value >= 1000:
            s = "%1.6e" % value
        else:
            s = "%i" % value
    elif dtype == float:
        if value >= 1000:
            s = "%1.6e" % value
        else:
            s = "%1.6f" % value
    else:
        raise TypeError("Value should be bool, int, float or str")
    return s

def formatArray(value, dtype):
    s = "%s, " * len(value)
    s = s[:-2]
    values = [formatSingle(v, dtype) for v in value]
    return s % (*values,)

class Formatter_:
    def __init__(self, value, name):
        self.value = value
        self.name = name
    
    def get_formatted(self):
        value = self.value
        name = self.name
        
        if isinstance(value, np.ndarray):
            if value.ndim == 1:
                n = ["%s(%i)" % (name, i + 1) for i in range(len(value))]
                s = [_get_fmt_(v) for v in value]
            elif value.ndim == 2:
                n = ["%s(:, %i)" % (name, i + 1) for i in range(len(value))]
                s = [", ".join([_get_fmt_(vv) for vv in v]) for v in value]
            else:
                raise NotImplementedError("ndim of parameter must be <= 2")
            
            _zip = zip(n, s)
            res = "\n".join(["%s=%s" % (nn, ss) for nn, ss in _zip])
            
        else:
            res = "%s=%s" % (name, _get_fmt_(value))
        
        return res

class Parameter:
    def __init__(self, name, value, parent_namelist):
        self.name = name
        self.value = value
        self.parent_namelist = parent_namelist


class ParameterSingle(Parameter):
    def __init__(self, name, value, parent_namelist, dtype):
        super().__init__(name, value, parent_namelist)
        self.dtype = dtype
        
        
    def __repr__(self):
        s = formatSingle(self.value, self.dtype)
        return "%s=%s" % (self.name,  s)

class ParameterArray(Parameter):
    def __init__(self, name, value, parent_namelist, dtype):
        super().__init__(name, value, parent_namelist)
        self.dtype = dtype

            
    def __repr__(self):
        s = formatArray(self.value, self.dtype)
        return "%s=%s" % (self.name,  s)