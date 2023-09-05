## agent class

class Agent:
    global Path
    def __init__(self, G, startNode, nextNode, endNode, V, behaviour, path, shortpath, time, N):
        self.CurrentNode=startNode
        self.NextNode=nextNode 
        self.EndNode=endNode
        self.MapG=G
        self.Velocity=V
        self.Behaviour=behaviour
        self.ShortPath=shortpath
        self.Path=path
        self.Time = time
        self.ANum = N
    
    def addPath(self, node):
        self.Path.append(node)
        
    def addCurrentNode(self, node):
        self.CurrentNode = node
    
    def addNextNode(self, node):
        self.NextNode = node
        
    def addMapG(self, G):
        self.MapG=G
        
    def addVelocity(self, V):
        self.Velocity=V
        
    def addBehaviour(self, behaviour):
        self.Behaviour=behaviour
        
    def addShortPath(self, shortpath):
        self.ShortPath=shortpath
        
    def addTime(self, time):
        self.Time += time
    
        
        
        

    