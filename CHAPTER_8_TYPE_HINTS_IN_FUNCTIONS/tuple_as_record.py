
def take_tuple(user:tuple[int,int,int]):
    """Takes a simple tuple and prints"""
    print(user)


def multiple_type(user:tuple[int,float,str,list[int],dict[str,str],tuple[int,int]]):
    """takes a hatregenours tuple and prints it"""
    print(user)


take_tuple((10,20,30))
take_tuple((10,20.50,'ali',[1,2,3],{'name':'ali'}, (10,20)))
