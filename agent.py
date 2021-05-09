from RL_main import QLearningTable
from environment import Environment


class Agent:
    def __init__(self, agentAction):
        self.reinLearning = QLearningTable(agentAction)
        self.env = Environment()
        self.e = 5

    def training(self, envTypeArray):
        # initial structure
        # structure : hash or B+tree
        structure = self.env.reset()
        for episode in range(self.e):
            # initial structure
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
            print("agent training epsode " + str(episode) + " finished" + "\n")
        return structure

    def moniter(self, sign, table, column):
        """
            moniter open
        """
        if sign == 'open':
            num = 0
            while self.env.env_query_execute(num):
                envTypeArray = self.env.env_type_array(num)
                indexType = self.training(envTypeArray)
                print("index structure:" + indexType + "\n")
                self.env.update_index_structure(table, indexType, column)
                num += 1
        # moniter off
        elif sign == 'off':
            num = 0
            totalTime = 0
            while 1:
                result = self.env.env_query_execute(num)
                if result > 0:
                    num += 1
                    totalTime += result
                else:
                    break
            print("execute finished \n")
            print("total execute time :" + str(totalTime))
        else:
            print("signal not exist! \n")


if __name__ == '__main__':
    actions = ['toB+tree', 'toHash']
    Moniter = Agent(actions)
    table = 'city'
    column = 'population'
    Moniter.moniter('off', table, column)
