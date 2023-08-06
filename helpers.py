"""
Some helper functions
"""

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

