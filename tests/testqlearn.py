import unittest
import qlearn

class TestQlearn(unittest.TestCase):
    def testRunAction(self):
        tql = qlearn.TictactoeQmodel()
        turn = 0
        for i in range(9):
            self.assertTrue(tql.game.board[i//3][i%3] == 0)
            tql.runAction(i + turn * 9)
            self.assertTrue(tql.game.board[i//3][i%3] == turn + 1)
            turn = (turn+1)%2
    
    def test_valid_actions(self):
        tql = qlearn.TictactoeQmodel()
        invalidActions = [0,1,3,5,6]
        for ia in invalidActions:
            tql.runAction(ia)
        actions = tql.validActions()
        for action in actions:
            self.assertFalse(action in invalidActions)
    
    def test_valid_action(self):
        tql = qlearn.TictactoeQmodel()
        turn = 0
        for i in range(9):
            actionNum = i + turn*9
            self.assertTrue(tql.validAction(actionNum))
            tql.runAction(actionNum)
            self.assertFalse(tql.validAction(actionNum))
            tql.validAction(actionNum)
            turn = (turn+1)%2

    def test_train(self):
        tql = qlearn.TictactoeQmodel()
        #tql.train()
    
    def test_get_reward(self):
        tql = qlearn.TictactoeQmodel()
        print(tql.get_reward())
        tql.runAction(0)
        tql.runAction(1)
        tql.runAction(2)
        tql.game.drawboard()
        print(tql.get_reward())
        tql = qlearn.TictactoeQmodel()
        tql.runAction(0+9)
        tql.runAction(1+9)
        tql.runAction(2+9)
        tql.game.drawboard()
        print(tql.get_reward())

if __name__ == "__main__":
    unittest.main()