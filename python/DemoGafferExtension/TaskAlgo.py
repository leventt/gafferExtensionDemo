import GafferDispatch
import Gaffer.NodeAlgo


def __recursiveChildren( root ):

    result = [root]
    if hasattr( root, "children" ):
        for child in root.children():
            result += __recursiveChildren( child )
    
    return result


def __upstreamFileNames( taskPlug ):

    # ASK: may not be appropriate to handle gracefully
    # in case argument isn't a TaskPlug
    result = []
    if isinstance( taskPlug, GafferDispatch.TaskNode.TaskPlug ):
        parentNode = taskPlug.parent()
        nodes = Gaffer.NodeAlgo.upstreamNodes( parentNode ) + [parentNode]

        children = []
        for node in nodes:
            if isinstance( node, Gaffer.Box ):
                continue
            children += __recursiveChildren( node )
        
        result = filter(
            lambda x: "fileName" in x,
            children
        )
        result = map(
            lambda x: x["fileName"].getValue(),
            result
        )

    return result


# gathers all fileName parameters
# from all the upstream nodes including parent
# ASK: fileName parameter seems to be the convention
# but it feels like there is a more generic way to get
# FileSystemPath parameters somehow...
# so it may need improvement
def getTaskFiles( taskPlug ):
    
    __upstreamFileNames( taskPlug )
