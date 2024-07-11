# ds5100-finalproject-js7jx
final project repository

    Metadata: 
    - Author: Jonathan Swap
    - Name: Monte Carlo Simulator
    - Language: Python

    Synopsis:
    - The first class, Die, is meant to create an n-dimensional die with faces that are integers or strings. The second class, Game, can take a list of die objects, play a game, and ouput the results. The third class, Analyzer, takes in a game object and can show how many jackpots there were, how many times a face value was shown in a single roll in the game object.

    installation 
    - fork and clone the repo to your local computer. Open your terminal in VS Code, or any IDE or your local computer terminal, and then cd into your cloned repo. Then pip install . there. If it successfully imports, it should print 'The function was imported successfully' and the version number is '0.1.0'. There is example code for the montecarlo simulation below:
    
    ```python
    from montecarlo.montecarlo import Die, Game, Analyzer

    ## DIE CLASS DEMONSTRATION
    #this create a six sided die with equal weight/probabilities
    die = Die(np.array([1,2,3,4,5,6]))
    #altering the weight to make 2 and 3 more likely to be picked  and checking the weights
    die.set_weight(2,2)
    die.set_weight(3,2)
    die.get_dies_state()
    #roll the dice for n many times and see the list of results
    die.roll_dice(5)

    ## GAME CLASS DEMONSTRATION
    #creates 3 fair die and instantiate that list
    die = Die(np.array([1,2,3,4,5,6]))
    game = Game([die,die,die])
    #plays a game with 5 rolls for rolling all 3 die and view the dataframe of results
    game.play_game(5)
    game.most_recent(form='wide')


    ## ANALYZER CLASS DEMONSTRATION
    #instantiate a gameobject, check for number of jackpots, and then check how many face values were rolled each roll
    die = Die(np.array([1,2,3,4,5,6]))
    game = Game([die,die,die])
    game.play_game(5)
    game.most_recent(form='wide')
    analyzer = Analyzer(game)
    analyzer.jackpots()
    analyzer.facecounts_per_roll()
    #look at the number of possible combinations and permutation
    analyzer.combo_count()
    analyzer.permutation_count()
    ```


    API Description:
    ```python
    #DIE
    """This class, Die, creates an n dimensional die with equal, defualt weights, 
    or better thought of as probabilities, that can be adjusted as needed. 
    Additionally, this die can be rolled n many times and the state of the die, 
    also known as the compiled list of the n rolls can be retrieved at any point."""

    '''__init__(self, faces)

        PURPOSE: initializes the weights from the input face values.

        INPUT: a NumPy array of either strings or integers that will name the sides of the die
        OUTPUT: a private dataframe with faces in the index.
        '''

    '''set_weight(self,facevalue,newweight)
        
        PURPOSE: to change the weight of the faces for the die.

            INPUT: the face value that you want to change, which should be a string or integer, 
            and the new weight you want to assign it which should be an integer or float
            OUTPUT: an updated dataframe that has the new weight values for the faces you wanted to change
            '''

    '''roll_dice(self,rolls = 1)
        
        PURPOSE: to randomly sample the die, aka roll the die, while taking into consideration 
        the number of faces the die has and their respective weights. It adds the selection to a list.

            INPUT: number of rolls, otherwise defaults to 1 roll
            OUTPUT: It returns a list with the roll results.
            '''


    '''get_dies_state(self)
        
        PURPOSE: to see the state of die, which holds the faces and weights of the die.

        INPUT: no inputs
        OUTPUT: a dataframe of the faces and weights of the die.
        '''

    #GAME:

    """This class, Game, rolls a list of instantiated die and only keep the results 
    of their most recent play. Each die has the same number of sides, and each game
    is initialized with a python list of one or more die.""" 

    '''__init__(self, listofinstantiateddice)
        
        PURPOSE: Initializes a list of dice into the game method. 

            INPUT: the list of instatiated dice is a list with individual die
            OUTPUT: nothing
            '''

    '''play_game(self,numberoftimes)
    
    PURPOSE: this method rolls the die as many times as you want, but is defualted at 1 roll, for each 
        die in the list of die you originally input and then appends those results to the private dataframe.
         
            INPUT: the number of times you want to roll all your die. This will default to 1 roll if not specified
            OUTPUT: no output
        '''

    '''most_recent(self, form = 'wide')
        
        PURPOSE: To show you your most recent results in the table format of your choosing, between 'narrow' and 'wide'.

            INPUT:  you can specify the format of the table that you want, if you dont specify 'narrow', the other option, 
            it will default to 'wide'
            OUTPUT: it will return the data frame of results from your play game method in the format of your choosing. 
            It will raise a valueerror if you dont enter a valid form argument.
            '''

    #ANALYZER:

    """This class, the Analyzer class, will provide functions to determine whether you have gotten 
    a jackpot and evaluate the number of each face value in the most recent roll. Additionally, you 
    can see the number of times each possible combinations and permutations was rolled"""

    '''__init__(self,gameobject)
        
        PURPOSE: to initialize a gameobject, a game that has been played with any number of die. 

            INPUT: a game object, which should be an instance from the Game class.
            OUTPUT: it will raise a ValueError if the gameobject is not from the Game class.
            '''

    '''jackpot(self)
        
        PURPOSE: This method will tell you the number of jackpots you win, the same face value being shown on all die. 

        INPUT: no inputs
        OUTPUT: it returns a counter that goes through each of the rows in the dataframe and if the row has one unique 
        character, aka all the face values are the same, it adds one to the counter. 
        '''

    '''facecounts_per_roll(self)
        
        PURPOSE: this will return a dataframe with how often each face value is rolled each roll for the game.

        INPUT: no inputs
        OUTPUT: a data frame with columns for each face values, the indices area the roll numbers, and the valeus 
        are how often that face value was shown in that one roll.
        '''

    '''combo_count(self):
        
        PURPOSE: this functions looks at all the possible combinations with the face values and appends that to a list. 
        Then creates a multiindex using the tuples of combinations and populates it with the number of times that combination
        was rolled in the game.

        INPUT: no inputs
        OUTPUT: a dataframe with one column of the frequency that combination was rolled in the game.
        '''

    '''permutation_count(self):
        
        PURPOSE: this functions looks at all the possible permutations with the face values and appends that to a list. 
        Then creates a multiindex using the tuples of permutations and populates it with the number of times that permutation
        was rolled in the game.

        INPUT: no inputs
        OUTPUT: a dataframe with one column of the frequency that permutation was rolled in the game.
        '''
    ```