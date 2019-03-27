import unittest
import tictactoe


class TestTicTacToe(unittest.TestCase):
    def testWin(self):
        players = [1,2]
        for pi in range(2):
            player = players[pi]
            otherPlayer = players[(pi+1)%2]
            print(player)
            print(otherPlayer)
            print(" ")
            for i in range(3):
                ttt = tictactoe.tictactoe()
                self.assertFalse(ttt.detectWin())
                ttt.playMove(0, i, player=player)
                ttt.playMove(0, (i+1)%3, player=otherPlayer)
                self.assertFalse(ttt.detectWin())
                ttt.playMove(1, i,player=player)
                ttt.playMove(1, (i+1)%3, player=otherPlayer)
                self.assertFalse(ttt.detectWin())
                ttt.playMove(2, i, player=player)
                ttt.drawboard()
                self.assertTrue(ttt.detectWin())
            
            for i in range(3):
                ttt = tictactoe.tictactoe()
                self.assertFalse(ttt.detectWin())
                ttt.playMove(i, 0, player=player)
                self.assertFalse(ttt.detectWin())
                ttt.playMove(i, 1, player=player)
                self.assertFalse(ttt.detectWin())
                ttt.playMove(i, 2, player=player)
                self.assertTrue(ttt.detectWin())
            
            ttt = tictactoe.tictactoe()
            ttt2 = tictactoe.tictactoe()
            for i in range(3):
                self.assertFalse(ttt.detectWin())
                ttt.playMove(i, i, player=player)
                self.assertFalse(ttt2.detectWin())
                ttt2.playMove(i, 2 - i, player=player)
            self.assertTrue(ttt.detectWin())
            self.assertTrue(ttt2.detectWin())
    
    def test3row(self):
        for i in range(3):
            ttt = tictactoe.tictactoe()
            ttt.playMove(0, i)
            ttt.playMove(0, (i+1)%3,player=2)
            ttt.playMove(1, i)
            ttt.playMove(1, (i+1)%3, player=2)
            ttt.playMove(2, i)
            self.assertTrue(ttt.checkThree(0, i, down=1) == 1)

if __name__=="__main__":
    unittest.main()
