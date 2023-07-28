"""
Some helper functions
"""

def _get_raw_lines(path):
	"""
	Returns the whole par file as a list of lines: 
	No blanks spaces, no empty lines, no comments
	"""
	with open(path, "r") as file:
		raw_lines = file.readlines()
	raw_lines = [l.replace(" ", "") for l in raw_lines]
	raw_lines = [l for l in raw_lines if l != "" ]
	raw_lines = [l for l in raw_lines if l != "\n" ]
	raw_lines = [l.rsplit("!")[0] if l[0] != "!" else l for l in raw_lines]
	return raw_lines

def _parse(parameter_list):
	parameters = {}
	for p in parameter_list:
		key, val = p.rsplit("=")
		if val == ".true.":
			val = True
		elif val == ".false.":
			val = False
		parameters[key] = val
	# transform it into a dictionary file
	return parameters
