"""
This part is Environment Function
""" 
def get_env_feedback(S, A):
    """
    action from ['BPLUS', 'HASH']
    present index structure from ['BPLUS', 'HASH']
    query type from [0:point query ,1:others]
    State : (present index structure ,query type)
            e.g. ('BPLUS', 1)
    """
    if A == 'HASH':
        if S[1] == 0:
            if S[0] == 'BPLUS':
                S_ = S 
                S_[0] = 'HASH'
                R = 1
            else S[0] == 'HASH':
                S_ = S
                R = 1
        else:
                S_ = S
                R = 0
    elif A == 'BPLUS':
        if S[1] == 1:
            if S[0] == 'HASH':
                S_ = S 
                S_[0] = 'BPLUS'
                R = 1
            else S[0] == 'BPLUS':
                S_ = S
                R = 1
        else:
                S_ = S
                R = 0
    return S_, R
def updata_index_structure(S):
    """
    change index structure
    """
    if S[0] == 'BPLUS':
        pass
    elif S[0] == 'HASH':
        pass
