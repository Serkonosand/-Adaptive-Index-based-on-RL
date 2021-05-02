import random
from database import Database
from benchmark import Benchmark
BENCHMARK_FILE_DATAPATH = ""


class Environment:
    def __init__(self):
        # self.actions = ['toB+tree', 'toHash']
        self.structure = ['hash', 'b+tree']
        self.preIndStructure = 'b+tree'
        self.db = Database()
        self.bm = Benchmark(BENCHMARK_FILE_DATAPATH)

    def __get_query(self):
        return self.bm.query_read()

    def reset(self):
        return self.structure[1]

    def updata_index_structure(self, table, type, column):
        if type == self.preIndStructure:
            pass
        else:
            self.db.modif_index(table, type, column)
        self.preIndStructure = type

    def get_env_feedback(self, S, A):
        """
        action from ['toB+tree', 'toHash']
        present index structure from ['b+tree', 'hash']
        query type from [0:point query ,1:others]
        State : [present index structure ,query type]
                e.g. ['BPLUS', 1]
        """
        if A == 'toHash':
            if S[1] == 0:
                if S[0] == 'b+tree':
                    S_ = S
                    S_[0] = 'hash'
                    R = 0
                elif S[0] == 'hash':
                    S_ = S
                    R = 1
                else:
                    S_ = S
                    R = 0
            else:
                S_ = S
                R = 0
        elif A == 'toB+tree':
            if S[1] == 1:
                if S[0] == 'hash':
                    S_ = S
                    S_[0] = 'b+tree'
                    R = 0
                elif S[0] == 'b+tree':
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

    def env_type_array(self):
        pass
    
    def env_query_excute(self):
        q = self.__get_query()
        print("excute query: "+ q + "\n")
        self.db.query_excute(q)

    
    