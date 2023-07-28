"""
The parameter file class
"""
from collections import OrderedDict
# from .namelists import Namelist


class Parameter(OrderedDict):
    def __init__(self, name=None, value=None, parent_namelist=None):
        self[name] = value
        self.parent_namelist = parent_namelist
    """
    def __add__(self, other):
        errmsg = "Namelists are not compatible"
        if isinstance(other, self):
            if other.parent_namelist == self.parent_namelist:
                parameters = OrderedDict()
                parameters.update(self)
                parameters.update(other)
                return Namelist(name=self.parent_namelist,
                                parameters=parameters)
            else:
                raise ValueError(errmsg)
    """
