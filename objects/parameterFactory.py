import numpy as npfrom .parameter import ParameterArray, ParameterSingledef dispatch(name, value, parent_namelist):    isArray = _isArray(name)    valueRead =  _getValue(value, isArray)    selectedDispatcher = _getDispatcher(isArray)    return selectedDispatcher(name, valueRead, parent_namelist)def _getValue(value, isArray):    """    Reads line as an array or single value    """    sanitized = np.array(value.replace("(/","").replace("/)", "").rsplit(","))            if isArray:        return sanitized    else:        return sanitized[0]        def _isArray(name):    """    Checks if array    """    if name.count(":") >= 1:        return True    else:        return Falsedef _getDispatcher(isArray):    """    Returns correct dispatcher    """    if isArray:        return _dispatchArray    else:        return _dispatchSingleVal    def _dispatchSingleVal(name, value, parent_namelist):    """    Returns a single parameter class instance    """    dtype = _getdType(value)    value = value.replace("d", "e") if dtype == float else value    return ParameterSingle(name, dtype(value), parent_namelist, dtype)def _dispatchArray(name, value, parent_namelist):    """    Returns an array-like parameter class instance    """    dtype = _getdTypeArray(value)    return ParameterArray(name, value.astype(dtype),                           parent_namelist, dtype)def _getOnlyAlNum(value):    return "".join(c for c in value if c.isalnum()).replace("e", "")    def _getdType(value):    if value == ".true." or value == ".false.":        _type = bool    elif value.isdigit():        _type = int    else:        string = _getOnlyAlNum(value)        if string.isdigit():            _type = float        elif string.isalnum() or string == "":            _type = str        else:            _type = float    return _type        def _getdTypeArray(value):    types = np.array([_getdType(v) for v in value])        if np.any(types == bool):        _type = bool    elif np.any(types == str):        _type = str    elif np.any(types == int):        _type = int    else:         _type = float               return _type