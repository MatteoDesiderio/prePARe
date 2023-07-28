"""
The par file class
"""


class Par:
    def __init__(self, namelists=[]):
        self.namelists = namelists
        
    def __repr__(self):
        namelists = ["%s"%n for n in self.namelists]
        s = "\n\n".join(namelists)
        return s
    
    def from_file(self, path):
        pass
        # instantiate Namelist for each namelist in the par file
        # 