import unittest
from montecarlo.montecarlo import Die, Game, Analyzer
import numpy as np
import pandas as pd

class montecarloTest_die(unittest.TestCase): 
    
    def test_initialization(self):
        list_1 = [1,2,3,4,5,6]

        with self.assertRaises(TypeError):
            die1 = Die(list_1)

        die = Die(np.array([1,2,3,4,5,6]))
        self.assertIs(type(die._facesweights),pd.DataFrame)
    

    def test_set_weight(self):
        die = Die(np.array([1,2,3,4,5,6]))
        die.set_weight(1,5)
        self.assertTrue(die._facesweights[0][1]==5)
        
    def test_roll_dice(self):
        die = Die(np.array([1,2,3,4,5,6]))
        self.assertTrue(type(die.roll_dice(rolls=5)),list)

    def test_get_dies_state(self):
        die = Die(np.array([1,2,3,4,5,6]))
        self.assertIs(type(die.get_dies_state()),pd.DataFrame)
    

class montecarloTest_game(unittest.TestCase): 

    def test_initialization(self):
        die = Die(np.array([1,2,3,4,5,6]))
        listofdice = [die,die,die]
        game = Game(listofdice)
        self.assertIs(type(game._private_outcome_df),pd.DataFrame)
        self.assertIs(type(game),Game)
        self.assertIs(type(listofdice),list)
    
    def test_play_game(self):
        die = Die(np.array([1,2,3,4,5,6]))
        listofdice = [die,die,die]
        game = Game(listofdice)
        game.play_game(numberoftimes=6)
        self.assertTrue(game._private_outcome_df.shape[0] == 6)

    def test_most_recent(self):
        die = Die(np.array([1,2,3,4,5,6]))
        listofdice = [die,die,die]
        game = Game(listofdice)
        game.most_recent()
        self.assertIs(type(game._private_outcome_df),pd.DataFrame)
    
   
class montecarloTest_analyzer(unittest.TestCase): 

    def test_initialization(self):
        die = Die(np.array([1,2,3,4,5,6]))
        listofdice = [die,die,die]
        game = Game(listofdice)
        analyzer = Analyzer(game)
        self.assertIs(type(analyzer),Analyzer)
    
    def test_jackpot(self):
        die = Die(np.array([1,2,3,4,5,6]))
        listofdice = [die,die,die]
        game = Game(listofdice)
        analyzer = Analyzer(game)
        self.assertIs(type(analyzer.jackpot()),int)

    def test_facecounts_per_roll(self):
        die = Die(np.array([1,2,3,4,5,6]))
        listofdice = [die,die,die]
        game = Game(listofdice)
        analyzer = Analyzer(game)
        self.assertIs(type(analyzer.facecounts_per_roll()),pd.DataFrame)

    def test_combo_count(self):
        die = Die(np.array([1,2,3,4,5,6]))
        listofdice = [die,die,die]
        game = Game(listofdice)
        analyzer = Analyzer(game)
        self.assertIs(type(analyzer.combo_count()),pd.DataFrame)
    
    def test_permutation_count(self):
        die = Die(np.array([1,2,3,4,5,6]))
        listofdice = [die,die,die]
        game = Game(listofdice)
        analyzer = Analyzer(game)
        self.assertIs(type(analyzer.permutation_count()),pd.DataFrame)

if __name__ == '__main__': unittest.main(verbosity=3)