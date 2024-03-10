"""
Some helper functions
"""

from objects._shape_mappings import _shape_map
from objects.parameter import ParameterShape

def _get_raw_lines(path):
	"""
	Returns the whole defaults_include file as a list of lines.
	No blanks spaces, no empty lines, no comments
	"""
	with open(path, "r") as file:
		raw_lines = file.readlines()
	raw_lines = [l.replace(" ", "") for l in raw_lines]
	raw_lines = [l.replace("'", "\'") for l in raw_lines]
	raw_lines = [l for l in raw_lines if l != "" ]
	raw_lines = [l for l in raw_lines if l != "\n" ]
	raw_lines = [l.rsplit("!")[0] if l[0] != "!" else l for l in raw_lines]
	return raw_lines

def _get_names(path):
    """
	Returns the headings of the namelists found in the defaults_include
	"""
    raw_lines = _get_raw_lines(path)
    names = filter(lambda x: x[:2] == "!&", raw_lines)
    names = [n.replace("\n", "").replace("!&", "") for n in names]
    return names


def _fill_in_array_shapes(namelists):
    return namelists
    all_parameters = {p.name:p.value
                      for nl in namelists 
                      for p in nl.parameters}

    for namelist in namelists:
        for parameter in namelist.parameters:
            shape = _map_parameter_to_shape(parameter.name,
                                            _shape_map)
            pShape = ParameterShape(shape)
            parameter.shape = pShape
                
    return namelists
            
def _map_parameter_to_shape(name, _shape_map):
    shape = []
    for x in _shape_map[name]:
        shape.append(["", x])
        "what happens if x is a string????????"
    return shape
  
                
        
    
    
    
    

