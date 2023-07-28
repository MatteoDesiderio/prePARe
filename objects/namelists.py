from collections import OrderedDict
from helpers import _get_raw_lines
from .par import Par
from .parameter import Parameter


class Namelist(OrderedDict):
    def __init__(self, name="", parameters=OrderedDict()):
        if not isinstance(parameters, OrderedDict):
            raise TypeError
        self[name] = parameters

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

        # return Namelist(name, parameters)

    def __add__(self, other):
        if isinstance(other, Parameter):
            name = other.parent_namelist
            self[name].update(other)
        elif isinstance(other, Namelist):
            return Par([self, other])
