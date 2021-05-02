from RL_main import QLearningTable
from environment import Environment

class Agent:
    def __init__(self, agentAction):
        self.reinLearning = QLearningTable(agentAction)
        self.env = Environment()
        self.e = 5

    def training(self, envTypeArray):
        for episode in range(self.e):
            # initial structure
            # structure : hash or B+tree
            structure = self.env.reset()
            # envTypeArray : query type array
            for i in range(len(envTypeArray)):
                # RL choose action based on structure
                Action = self.reinLearning.choose_action(str(structure))
                Str = [structure, int(envTypeArray[i])]
                # RL get environment feedback
                Str_, Reward = self.env.get_env_feedback(Str, Action)

                structure_ = Str_[0]
                # RL learn from this transition
                self.reinLearning.learn(str(structure), Action, Reward, str(structure_))

                # swap structure
                structure = structure_
                # print(i, structure)
            print("agent training epsode "+episode+" finished"+"\n")
        return structure
    
    def moniter(self, sign, table, column):
        """
            moniter open
        """
        if sign == 'open':
            while True:
                envTypeArray = self.env.env_type_array()
                indexType = self.training(envTypeArray)
                print("index structure:" + indexType + "\n")
                self.env.updata_index_structure(table, indexType, column)
                self.env.env_query_excute()
        else if sign == 'off':
            while True:
                self.env.env_query_excute()
        else:
            print("signal not exist! \n")


if __name__ == '__main__':
    actions = ['toB+tree', 'toHash']
    Moniter  = Agent(actions)
    Moniter.moniter('open', table, column)