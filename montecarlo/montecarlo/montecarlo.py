import numpy as np
import pandas as pd



class Die():
    """docstring Class docstrings should describe 
    the general purpose of the class."""

    def __init__(self, faces):
        '''Method docstrings should describe the purpose of the 
        method, any input arguments, any return values if applicable, 
        and any changes to the object’s state that the user should 
        know about.'''
        weights = np.ones(faces)
        if len(np.unique(faces)) != len(faces):
              raise ValueError('Please enter unique side names.')
        if faces.dtype != [str,int]:
            raise TypeError
        _facesweights = pd.DataFrame(faces,weights)

    def set_weight(self,facevalue,newweight):
        '''Method docstrings should describe the purpose of the 
        method, any input arguments, any return values if applicable, 
        and any changes to the object’s state that the user should 
        know about.'''
        if facevalue not in self.faces:
            raise IndexError('The face value is not in the array of faces you input originally.')
        if newweight.dtype is not [int, float]:
            raise TypeError('The new weight is not an integer or float. Please input a float or integer for the new weight.')
        _facesweights = _facesweights.append(facevalue,newweight)
        pass

    def get_more_rolls(self,rolls = 1):
        '''Method docstrings should describe the purpose of the 
        method, any input arguments, any return values if applicable, 
        and any changes to the object’s state that the user should 
        know about.'''
        pass

    def get_dies_state(self):
        '''Method docstrings should describe the purpose of the 
        method, any input arguments, any return values if applicable, 
        and any changes to the object’s state that the user should 
        know about.'''
        return self._facesweights



class Game():
    """docstring Class docstrings should describe 
    the general purpose of the class.""" 
    def __init__(self):
        '''Method docstrings should describe the purpose of the 
        method, any input arguments, any return values if applicable, 
        and any changes to the object’s state that the user should 
        know about.'''
        pass



class Analyzer():
    """docstring Class docstrings should describe 
    the general purpose of the class."""
    def __init__(self):
        '''Method docstrings should describe the purpose of the 
        method, any input arguments, any return values if applicable, 
        and any changes to the object’s state that the user should 
        know about.'''
        pass
