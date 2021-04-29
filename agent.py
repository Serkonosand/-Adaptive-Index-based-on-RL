from RL_main import QLearningTable
from DB_action import DatabaseAction


class Agent:
    def __init__(self, agentAction):
        self.reinLearning = QLearningTable(agentAction)
        self.dbAction = DatabaseAction()

    def training(self):
        pass