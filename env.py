"""
This part is Environment Function
"""
from RL_main import QLearningTable

"""
用于文件操作
"""

FILEPATH = "./testdata/data.txt"


def get_env_feedback(S, A):
    """
    action from ['toBPLUS', 'toHASH']
    present index structure from ['BPLUS', 'HASH']
    query type from [0:point query ,1:others]
    State : [present index structure ,query type]
            e.g. ['BPLUS', 1]
    """
    if A == 'toHASH':
        if S[1] == 0:
            if S[0] == 'BPLUS':
                S_ = S
                S_[0] = 'HASH'
                R = 0
            elif S[0] == 'HASH':
                S_ = S
                R = 1
            else:
                S_ = S
                R = 0
        else:
            S_ = S
            R = 0
    elif A == 'toBPLUS':
        if S[1] == 1:
            if S[0] == 'HASH':
                S_ = S
                S_[0] = 'BPLUS'
                R = 0
            elif S[0] == 'BPLUS':
                S_ = S
                R = 1
            else:
                S_ = S
                R = 0
        else:
            S_ = S
            R = 0
    else:
        S_ = S
        R = 0
    return S_, R


def updata_index_structure(structure):
    """
    change index structure
    """
    if structure == 'BPLUS':
        print(structure)
    elif structure == 'HASH':
        print(structure)


if __name__ == '__main__':
    actions = ['toBPLUS', 'toHASH']
    RL = QLearningTable(actions)
    with open(FILEPATH, 'r') as f:
        tmpdata = f.read().splitlines()
    for episode in range(10):
        # initial structure
        structure = 'BPLUS'
        for i in range(100):
            # RL choose action based on structure
            Action = RL.choose_action(str(structure))
            Str = [structure, int(tmpdata[episode * 100 + i])]
            # RL get environment feedback
            Str_, Reward = get_env_feedback(Str, Action)

            structure_ = Str_[0]
            # RL learn from this transition
            RL.learn(str(structure), Action, Reward, str(structure_))

            # swap structure
            structure = structure_
            print(i, structure)
        RL.print_qtable()
        updata_index_structure(structure)
