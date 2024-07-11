import numpy as np
import pandas as pd
import random
import itertools

class Die():
    """This class, Die, creates an n dimensional die with equal, defualt weights, 
    or better thought of as probabilities, that can be adjusted as needed. 
    Additionally, this die can be rolled n many times and the state of the die, 
    also known as the compiled list of the n rolls can be retrieved at any point."""

    def __init__(self, faces):
        '''
        PURPOSE: initializes the weights from the input face values.

        INPUT: a NumPy array of either strings or integers that will name the sides of the die
        OUTPUT: a private dataframe with faces in the index.
        '''
        self.faces = faces
        if isinstance(self.faces,np.ndarray) != True:
            raise TypeError('faces argument is not a NumPy array. Please enter a NumPy array')
        if len(np.unique(faces)) != len(faces):
              raise ValueError('Please enter unique face names.')
        for n in self.faces:
            if type(n) != np.str_ and type(n) != np.int_ and type(n) != np.float_:
                raise TypeError('faces data type is not a string or integer. Please only enter strings or integers.')
        self.weights = np.ones(len(self.faces))
        self._facesweights = pd.DataFrame(self.weights, index = self.faces)

    def set_weight(self,facevalue,newweight):
        '''PURPOSE: to change the weight of the faces for the die.

            INPUT: the face value that you want to change, which should be a string or integer, 
            and the new weight you want to assign it which should be an integer or float
            OUTPUT: an updated dataframe that has the new weight values for the faces you wanted to change
            '''
        if facevalue not in self.faces:
            raise IndexError('The face value is not in the array of faces you input originally.')
        if (type(newweight) != int and type(newweight) != float):
            raise TypeError('The new weight is not an integer or float. Please input a float or integer for the new weight.')
        try:
            self._facesweights.loc[facevalue] = newweight
            self.weights = self._facesweights['Weights']
        except: KeyError

    def roll_dice(self,rolls = 1):
        '''PURPOSE: to randomly sample the die, aka roll the die, while taking into consideration 
        the number of faces the die has and their respective weights. It adds the selection to a list.

            INPUT: number of rolls, otherwise defaults to 1 roll
            OUTPUT: It returns a list with the roll results.
            '''
        roll_list = np.random.choice(a=self.faces,p=[i/sum(self.weights) for i in self.weights],size=rolls)
        return roll_list.copy()

    def get_dies_state(self):
        '''PURPOSE: to see the state of die, which holds the faces and weights of the die.

        INPUT: no inputs
        OUTPUT: a dataframe of the faces and weights of the die.
        '''
        return self._facesweights

class Game():
    """This class, Game, rolls a list of instantiated die and only keep the results 
    of their most recent play. Each die has the same number of sides, and each game
    is initialized with a python list of one or more die.""" 
    def __init__(self, listofinstantiateddice):
        '''PURPOSE: Initializes a list of dice into the game method. 

            INPUT: the list of instatiated dice is a list with individual die
            OUTPUT: nothing
            '''
        self.listofinstantiateddice = listofinstantiateddice
        self._private_outcome_df = pd.DataFrame()
    
    def play_game(self,numberoftimes): 
        '''PURPOSE: this method rolls the die as many times as you want, but is defualted at 1 roll, for each 
        die in the list of die you originally input and then appends those results to the private dataframe.
         
            INPUT: the number of times you want to roll all your die. This will default to 1 roll if not specified
            OUTPUT: no output
        '''
        for i,x in enumerate(self.listofinstantiateddice):
            self._private_outcome_df[f' die number {i+1}'] = x.roll_dice(numberoftimes)
        
    def most_recent(self, form = 'wide'):
        '''PURPOSE: To show you your most recent results in the table format of your choosing, between 'narrow' and 'wide'.

            INPUT:  you can specify the format of the table that you want, if you dont specify 'narrow', the other option, 
            it will default to 'wide'
            OUTPUT: it will return the data frame of results from your play game method in the format of your choosing. 
            It will raise a valueerror if you dont enter a valid form argument.
            '''
        if form.lower() == 'narrow':
            return self._private_outcome_df.stack().copy()
        if form.lower() == 'wide':
            return self._private_outcome_df.copy()
        else:
            raise ValueError("Invalid option for dataframe form. Must be 'narrow' or 'wide'")

class Analyzer():
    """This class, the Analyzer class, will provide functions to determine whether you have gotten 
    a jackpot and evaluate the number of each face value in the most recent roll. Additionally, you 
    can see the number of times each possible combinations and permutations was rolled"""
    def __init__(self,gameobject):
        '''PURPOSE: to initialize a gameobject, a game that has been played with any number of die. 

            INPUT: a game object, which should be an instance from the Game class.
            OUTPUT: it will raise a ValueError if the gameobject is not from the Game class.
            '''
        if not isinstance(gameobject, Game):
            raise ValueError('This game object is not an instance of the Game class.')
        self.gameobject = gameobject

    def jackpot(self):
        '''PURPOSE: This method will tell you the number of jackpots you win, the same face value being shown on all die. 

        INPUT: no inputs
        OUTPUT: it returns a counter that goes through each of the rows in the dataframe and if the row has one unique 
        character, aka all the face values are the same, it adds one to the counter. 
        '''
        self.counter = 0
        for i in self.gameobject._private_outcome_df.index:
            i = i-1
            row = np.array(self.gameobject._private_outcome_df.iloc[i])
            if len(np.unique(row)) == 1:
                self.counter += 1
        return self.counter
        
    def facecounts_per_roll(self):
        '''PURPOSE: this will return a dataframe with how often each face value is rolled each roll for the game.

        INPUT: no inputs
        OUTPUT: a data frame with columns for each face values, the indices area the roll numbers, and the valeus 
        are how often that face value was shown in that one roll.
        '''
        return pd.DataFrame(self.gameobject.most_recent()).apply(pd.Series.value_counts,axis = 1).fillna(0)

    def combo_count(self):
        '''PURPOSE: this functions looks at all the possible combinations with the face values and appends that to a list. 
        Then creates a multiindex using the tuples of combinations and populates it with the number of times that combination
        was rolled in the game.

        INPUT: no inputs
        OUTPUT: a dataframe with one column of the frequency that combination was rolled in the game.
        '''
        combinationlist = list(itertools.combinations_with_replacement(
            list(self.gameobject.listofinstantiateddice[0].faces),
            len(self.gameobject.listofinstantiateddice)))
        combinationindex = pd.MultiIndex.from_tuples(combinationlist)
        combinationdf = pd.DataFrame(index=combinationindex)
        combinationdf['frequency'] = self.gameobject.most_recent().apply(lambda row: tuple(np.sort(row))).value_counts().to_frame()
        return combinationdf.fillna(0)

    def permutation_count(self):
        '''PURPOSE: this functions looks at all the possible permutations with the face values and appends that to a list. 
        Then creates a multiindex using the tuples of permutations and populates it with the number of times that permutation
        was rolled in the game.

        INPUT: no inputs
        OUTPUT: a dataframe with one column of the frequency that permutation was rolled in the game.
        '''
        permutationdf = self.gameobject.most_recent().apply(lambda row: tuple(row)).value_counts().to_frame()
        return permutationdf