Node=rit_lib.struct_type("Node", (object,'value'), ((Nonetype,Node),'rest'))

def index_of(value,lns):


def is_in(value,lns):
    if lns==None:
        return False
    else:
        if lns.value==value:
            return True
        else:
            return is_in(value, lns.rest)