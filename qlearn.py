import tictactoe
import abc
import random

class Qmodel(abc.ABC):
    def __init__(self, game):
        self.game = game

    @abc.abstractmethod
    def runAction(self, actionNumber):
        pass

class TictactoeQmodel(Qmodel):
    def __init__(self):
        self.resetGame()
        self.numActions = 18
        self.qtable = {}
        self.alpha = .1
    
    def resetGame(self):
        self.game = tictactoe.tictactoe()

    def actionToMove(self, actionNumber):
        numSpots = 9
        player = actionNumber // numSpots + 1
        spot = actionNumber % numSpots
        row = spot // 3
        column = spot % 3
        return (row, column, player)

    def runAction(self, actionNumber):
        move = self.actionToMove(actionNumber)
        self.game.playMove(*move)

    def validAction(self, actionNumber):
        move = self.actionToMove(actionNumber)
        return self.game.validMove(*move)

    def validActions(self):
        actions = list(range(self.game.numActions))
        return filter(lambda actionNumber:self.validAction(actionNumber), actions)

    def generateActions(self):
        va = self.validActions()
        for action in va:
            yield action

    def get_reward(self):
        if self.game.detectWin():
            if self.game.getTurn() == 1:
                return 100
            elif self.game.getTurn() == 2:
                return -100
            else:
                print("getTurn yieled value not 1 or 2")
        actions = list(self.validActions())
        if not actions:
            return 0
        return 0

    def train(self):
        actions = list(self.validActions())
        if not actions:
            return 0
        if not self.get_reward() == 0:
            return self.get_reward()

        nextAction = random.choice(actions)
        enviornment = self.game.hashState()
        if enviornment in self.qtable:
            oldValue = self.qtable[enviornment]
        else:
            oldValue = 0
        self.qtable[enviornment] = (1-self.alpha) * oldValue + self.alpha * ()



