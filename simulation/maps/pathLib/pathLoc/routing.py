##Routing func
import pathlib  # baraye adres dehi
import networkx as nx
from maps.pathLib.pathLoc import locLib,agent
import sys
import matplotlib.pyplot as plt
import random



        
def strToList(lst):
    lst = lst.replace("[", "").replace("]", "")
    lst = lst.split(",")
    # print(lst)
    return lst


def idList(locList, G):
    idL = []
    c = len(locList)
    for i in range(int(c/2)):
        idL += [int(locLib.findLoc(float(locList[i*2]), float(locList[i*2+1]), G))]
    # print(idL)
    return idL 
        
        

def nextShortPathV0(agent, MG, T):
    a = agent
    G = MG
    global sEdge
    havlen = sys.maxsize
    global neighbor
    if a.NextNode == -1 and a.CurrentNode != a.EndNode:##try if neighbors are null !!! end node = nest node?
        print("log0")
        for node in a.MapG.neighbors(str(a.CurrentNode)):
            print("log1")
            if  a.MapG[str(a.CurrentNode)][node]["havlen"] < havlen and a.MapG[str(a.CurrentNode)][node]["seen"] < 3 :## be node i ke oomade barnagare !!! neveshte nashode !!! baraye node flag gozashe she 
                print("log1-1")
                neighbor = node
                sEdge = a.MapG[str(a.CurrentNode)][node]
                havlen = a.MapG[str(a.CurrentNode)][node]['havlen']
        a.MapG[str(a.CurrentNode)][neighbor]["seen"] += 1
        a.MapG.nodes[neighbor]["seen"] = 1
        print("log2")
        if T*a.Velocity < havlen:
            print("log3")
            print(str(a.CurrentNode))
            a.NextNode = neighbor
            print(a.NextNode)
            print(a.MapG.has_edge(str(a.CurrentNode),a.NextNode))
            a.MapG[str(a.CurrentNode)][a.NextNode]['havlen'] = a.MapG[str(a.CurrentNode)][a.NextNode]['havlen'] - T*a.Velocity
            G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] = G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] + 1
            
        elif T*a.Velocity > havlen:
            print("log4")
            a.CurrentNode = neighbor
            a.NextNode = -1
            a.Path += [neighbor]
            T1 = (havlen/a.Velocity)
            T2 = T - T1
            a , G = nextShortPath(a, G, T2)##func az output add output to it 
            
        else :##T*a.Velocity = havlen
            print("log5")
            a.CurrentNode = neighbor
            a.NextNode = -1
            a.Path += [neighbor]
            
    elif a.NextNode != -1 and a.CurrentNode != a.EndNode :
        print("log6")
        print(a.NextNode)
        havlen = a.MapG[str(a.CurrentNode)][str(a.NextNode)]['havlen']
        if T*a.Velocity < havlen:
            a.MapG[str(a.CurrentNode)][str(a.NextNode)]['havlen'] = a.MapG[str(a.CurrentNode)][str(a.NextNode)]['havlen'] - T*a.Velocity
        elif T*a.Velocity > havlen:
            a.Path += [a.NextNode]
            G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] = G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] - 1
            a.CurrentNode = a.NextNode
            a.NextNode = -1
            T1 = (havlen/a.Velocity)
            T2 = T - T1
            a , G = nextShortPath(a, G, T2)##func az output add output to it 
        else :##T*a.Velocity = havlen
            G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] = G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] - 1
            a.CurrentNode = a.NextNode
            a.Path += [a.NextNode]
            a.NextNode = -1
    elif a.CurrentNode != a.EndNode:
        ##do nothing
        print("log9")
    return a, G

def nextShortPath(agent, MG, T):###start & end +path
    a = agent
    G = MG
    global sEdge
    havlen = sys.maxsize
    global neighbor
    trafficC = 10
    t = T
    # if a.Behaviour == 2 or a.Behaviour == 3:
    #     nodes = list(G.neighbors(str(a.CurrentNode)))
    #     nodesLn = len(nodes)
    #     if nodesLn != 0:
    #         nodeN = random.randint(0, nodesLn-1)
    #         print(nodeN)
    #         a.EndNode = nodes[nodeN]
        
    if a.NextNode == -1 and int(a.CurrentNode) != int(a.EndNode):##try if neighbors are null !!! end node = nest node?
        print("log0")
        
        ##
        # a.ShortPath = nx.shortest_path(G, source=str(a.CurrentNode), target=str(a.EndNode), weight='havlen')
        
        
        a.addShortPath(nx.shortest_path(G, source=str(a.CurrentNode), target=str(a.EndNode), weight='havlen'))
        for i in range(len(a.ShortPath)):
            print("log1")
            
            if int(a.ShortPath[i]) == int(a.CurrentNode):
                print("log1-1")
                neighbor = a.ShortPath[i+1]
                havlen = a.MapG[str(a.CurrentNode)][str(neighbor)]["havlen"]
                break
        
        a.MapG[str(a.CurrentNode)][neighbor]["seen"] = 1
        a.MapG.nodes[neighbor]["seen"] = 1
        print("log2")
        if T*a.Velocity < havlen:
            print("log3")
            a.addTime(t)
            # a.NextNode = neighbor
            G.nodes[str(a.CurrentNode)]["seen"] -=1
            a.addNextNode(neighbor)
            a.MapG[str(a.CurrentNode)][a.NextNode]['havlen'] = a.MapG[str(a.CurrentNode)][a.NextNode]['havlen'] - T*a.Velocity
            G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] = G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] + trafficC
            G[str(a.CurrentNode)][str(a.NextNode)]["trafficH"] = 1/(G[str(a.CurrentNode)][str(a.NextNode)]["traffic"])
            
        elif T*a.Velocity > havlen:
            print("log4")
            # a.CurrentNode = neighbor
            G.nodes[str(a.CurrentNode)]["seen"] -=1
            a.addCurrentNode(neighbor)
            # a.NextNode = -1
            G.nodes[str(a.CurrentNode)]["seen"] +=1
            a.addNextNode(-1)
            # a.Path += [neighbor]
            a.addPath(neighbor)
            T1 = (havlen/a.Velocity)
            T2 = T - T1
            a.addTime(T1)
            a , G = nextShortPath(a, G, T2)##func az output add output to it 
            
        else :##T*a.Velocity = havlen
            print("log5")
            # a.CurrentNode = neighbor
            G.nodes[str(a.CurrentNode)]["seen"] -=1
            a.addCurrentNode(neighbor)
            # a.NextNode = -1
            G.nodes[str(a.CurrentNode)]["seen"] +=1
            a.addNextNode(-1)
            # a.Path += [neighbor]
            a.addPath(neighbor)
            a.addTime(T)
            
    elif a.NextNode != -1 and a.CurrentNode != a.EndNode :
        print("log6")
        
        havlen = a.MapG[str(a.CurrentNode)][str(a.NextNode)]['havlen']
        if T*a.Velocity < havlen:
            print("log7")
            a.addTime(T)
            a.MapG[str(a.CurrentNode)][str(a.NextNode)]['havlen'] = a.MapG[str(a.CurrentNode)][str(a.NextNode)]['havlen'] - T*a.Velocity
        elif T*a.Velocity > havlen:
            print("log8")
            # a.Path += [a.NextNode]
            a.addPath(a.NextNode)
            G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] = G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] - trafficC
            G[str(a.CurrentNode)][str(a.NextNode)]["trafficH"] = 1/(G[str(a.CurrentNode)][str(a.NextNode)]["traffic"])
            a.MapG[str(a.CurrentNode)][a.NextNode]['havlen'] = G[str(a.CurrentNode)][a.NextNode]['havlen']
            # a.CurrentNode = a.NextNode
            a.addCurrentNode(a.NextNode)
            G.nodes[str(a.CurrentNode)]["seen"] +=1
            # a.NextNode = -1
            a.addNextNode(-1)
            T1 = (havlen/a.Velocity)
            T2 = T - T1
            a.addTime(T1)
            a , G = nextShortPath(a, G, T2)##func az output add output to it 
        else :##T*a.Velocity = havlen
            print(log9)
            G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] = G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] - trafficC
            G[str(a.CurrentNode)][str(a.NextNode)]["trafficH"] = 1/(G[str(a.CurrentNode)][str(a.NextNode)]["traffic"])
            a.MapG[str(a.CurrentNode)][a.NextNode]['havlen'] = G[str(a.CurrentNode)][a.NextNode]['havlen']
            # a.CurrentNode = a.NextNode
            a.addCurrentNode(a.NextNode)
            G.nodes[str(a.CurrentNode)]["seen"] +=1
            # a.Path += [a.NextNode]
            a.addPath(a.NextNode)
            # a.NextNode = -1
            a.addNextNode(-1)
            a.addTime(T)
    elif a.CurrentNode != a.EndNode:
        ##do nothing
        print("log10")
    return a, G

def lightestTraffic(agent, MG, T):
    a = agent
    G = MG
    global sEdge
    havlen = sys.maxsize
    global neighbor
    trafficC = 10

            
    if a.NextNode == -1 and int(a.CurrentNode) != int(a.EndNode):##try if neighbors are null !!! end node = nest node?
        print("log0")
        
        ##
        # a.ShortPath = nx.shortest_path(G, source=str(a.CurrentNode), target=str(a.EndNode), weight='traffic')
        a.addShortPath(nx.shortest_path(G, source=str(a.CurrentNode), target=str(a.EndNode), weight='traffic'))
        for i in range(len(a.ShortPath)):
            print("log1")
            
            if int(a.ShortPath[i]) == int(a.CurrentNode):
                print("log1-1")
                neighbor = a.ShortPath[i+1]
                havlen = a.MapG[str(a.CurrentNode)][str(neighbor)]["havlen"]
                break
        
        a.MapG[str(a.CurrentNode)][neighbor]["seen"] = 1
        a.MapG.nodes[neighbor]["seen"] = 1
        print("log2")
        if T*a.Velocity < havlen:
            print("log3")
            a.addTime(T)
            # a.NextNode = neighbor
            G.nodes[str(a.CurrentNode)]["seen"] -=1
            a.addNextNode(neighbor)
            a.MapG[str(a.CurrentNode)][a.NextNode]['havlen'] = a.MapG[str(a.CurrentNode)][a.NextNode]['havlen'] - T*a.Velocity
            G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] = G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] + trafficC
            G[str(a.CurrentNode)][str(a.NextNode)]["trafficH"] = 1/(G[str(a.CurrentNode)][str(a.NextNode)]["traffic"])
            
        elif T*a.Velocity > havlen:
            print("log4")
            # a.CurrentNode = neighbor
            G.nodes[str(a.CurrentNode)]["seen"] -=1
            a.addCurrentNode(neighbor)
            # a.NextNode = -1
            G.nodes[str(a.CurrentNode)]["seen"] +=1
            a.addNextNode(-1)
            # a.Path += [neighbor]
            a.addPath(neighbor)
            T1 = (havlen/a.Velocity)
            T2 = T - T1
            a.addTime(T1)
            a , G = lightestTraffic(a, G, T2)##func az output add output to it 
            
        else :##T*a.Velocity = havlen
            print("log5")
            # a.CurrentNode = neighbor
            G.nodes[str(a.CurrentNode)]["seen"] -=1
            a.addCurrentNode(neighbor)
            # a.NextNode = -1
            G.nodes[str(a.CurrentNode)]["seen"] +=1
            a.addNextNode(-1)
            # a.Path += [neighbor]
            a.addPath(neighbor)
            a.addTime(T)
            
    elif a.NextNode != -1 and a.CurrentNode != a.EndNode :
        print("log6")
        
        havlen = a.MapG[str(a.CurrentNode)][str(a.NextNode)]['havlen']
        if T*a.Velocity < havlen:
            print("log7")
            a.addTime(T)
            a.MapG[str(a.CurrentNode)][str(a.NextNode)]['havlen'] = a.MapG[str(a.CurrentNode)][str(a.NextNode)]['havlen'] - T*a.Velocity
        elif T*a.Velocity > havlen:
            print("log8")
             # a.Path += [a.NextNode]
            a.addPath(a.NextNode)
            G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] = G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] - trafficC
            G[str(a.CurrentNode)][str(a.NextNode)]["trafficH"] = 1/(G[str(a.CurrentNode)][str(a.NextNode)]["traffic"])
            a.MapG[str(a.CurrentNode)][a.NextNode]['havlen'] = G[str(a.CurrentNode)][a.NextNode]['havlen']
             # a.CurrentNode = a.NextNode
            a.addCurrentNode(a.NextNode)
            G.nodes[str(a.CurrentNode)]["seen"] +=1
            # a.NextNode = -1
            a.addNextNode(-1)
            T1 = (havlen/a.Velocity)
            T2 = T - T1
            a.addTime(T1)
            a , G = lightestTraffic(a, G, T2)##func az output add output to it 
        else :##T*a.Velocity = havlen
            print("log9")
            G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] = G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] - trafficC
            G[str(a.CurrentNode)][str(a.NextNode)]["trafficH"] = 1/(G[str(a.CurrentNode)][str(a.NextNode)]["traffic"])
            a.MapG[str(a.CurrentNode)][a.NextNode]['havlen'] = G[str(a.CurrentNode)][a.NextNode]['havlen']
            # a.CurrentNode = a.NextNode
            a.addCurrentNode(a.NextNode)
            G.nodes[str(a.CurrentNode)]["seen"] +=1
            # a.Path += [a.NextNode]
            a.addPath(a.NextNode)
            # a.NextNode = -1
            a.addNextNode(-1)
            a.addTime(T)
    elif a.CurrentNode != a.EndNode:
        ##do nothing
        print("log10")
        print(a.Time)
    return a, G



def heaviestTraffic(agent, MG, T):
    a = agent
    G = MG
    global sEdge
    havlen = sys.maxsize
    global neighbor
    trafficC = 10
    
    
    if a.NextNode == -1 and int(a.CurrentNode) != int(a.EndNode):##try if neighbors are null !!! end node = nest node?
        print("log0")
        
        ##
        # a.ShortPath = nx.shortest_path(G, source=str(a.CurrentNode), target=str(a.EndNode), weight='traffic')
        a.addShortPath(nx.shortest_path(G, source=str(a.CurrentNode), target=str(a.EndNode), weight='trafficH'))
        for i in range(len(a.ShortPath)):
            print("log1")
            
            if int(a.ShortPath[i]) == int(a.CurrentNode):
                print("log1-1")
                neighbor = a.ShortPath[i+1]
                havlen = a.MapG[str(a.CurrentNode)][str(neighbor)]["havlen"]
                break
        
        a.MapG[str(a.CurrentNode)][neighbor]["seen"] = 1
        a.MapG.nodes[neighbor]["seen"] = 1
        print("log2")
        if T*a.Velocity < havlen:
            print("log3")
            a.addTime(T)
            # a.NextNode = neighbor
            G.nodes[str(a.CurrentNode)]["seen"] -=1
            a.addNextNode(neighbor)
            a.MapG[str(a.CurrentNode)][a.NextNode]['havlen'] = a.MapG[str(a.CurrentNode)][a.NextNode]['havlen'] - T*a.Velocity
            G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] = G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] + trafficC
            G[str(a.CurrentNode)][str(a.NextNode)]["trafficH"] = 1/(G[str(a.CurrentNode)][str(a.NextNode)]["traffic"])
            
        elif T*a.Velocity > havlen:
            print("log4")
            # a.CurrentNode = neighbor
            G.nodes[str(a.CurrentNode)]["seen"] -=1
            a.addCurrentNode(neighbor)
            # a.NextNode = -1
            G.nodes[str(a.CurrentNode)]["seen"] +=1
            a.addNextNode(-1)
            # a.Path += [neighbor]
            a.addPath(neighbor)
            T1 = (havlen/a.Velocity)
            T2 = T - T1
            a.addTime(T1)
            a , G = heaviestTraffic(a, G, T2)##func az output add output to it 
            
        else :##T*a.Velocity = havlen
            print("log5")
            # a.CurrentNode = neighbor
            G.nodes[str(a.CurrentNode)]["seen"] -=1
            a.addCurrentNode(neighbor)
            # a.NextNode = -1
            G.nodes[str(a.CurrentNode)]["seen"] +=1
            a.addNextNode(-1)
            # a.Path += [neighbor]
            a.addPath(neighbor)
            a.addTime(T)
            
    elif a.NextNode != -1 and a.CurrentNode != a.EndNode :
        print("log6")
        
        havlen = a.MapG[str(a.CurrentNode)][str(a.NextNode)]['havlen']
        if T*a.Velocity < havlen:
            print("log7")
            a.addTime(T)
            a.MapG[str(a.CurrentNode)][str(a.NextNode)]['havlen'] = a.MapG[str(a.CurrentNode)][str(a.NextNode)]['havlen'] - T*a.Velocity
        elif T*a.Velocity > havlen:
            print("log8")
             # a.Path += [a.NextNode]
            a.addPath(a.NextNode)
            G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] = G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] - trafficC
            G[str(a.CurrentNode)][str(a.NextNode)]["trafficH"] = 1/(G[str(a.CurrentNode)][str(a.NextNode)]["traffic"])
            a.MapG[str(a.CurrentNode)][a.NextNode]['havlen'] = G[str(a.CurrentNode)][a.NextNode]['havlen']
             # a.CurrentNode = a.NextNode
            a.addCurrentNode(a.NextNode)
            G.nodes[str(a.CurrentNode)]["seen"] +=1
            # a.NextNode = -1
            a.addNextNode(-1)
            T1 = (havlen/a.Velocity)
            T2 = T - T1
            a.addTime(T1)
            a , G = heaviestTraffic(a, G, T2)##func az output add output to it 
        else :##T*a.Velocity = havlen
            print("log9")
            G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] = G[str(a.CurrentNode)][str(a.NextNode)]["traffic"] - trafficC
            G[str(a.CurrentNode)][str(a.NextNode)]["trafficH"] = 1/(G[str(a.CurrentNode)][str(a.NextNode)]["traffic"])
            a.MapG[str(a.CurrentNode)][a.NextNode]['havlen'] = G[str(a.CurrentNode)][a.NextNode]['havlen']
            # a.CurrentNode = a.NextNode
            a.addCurrentNode(a.NextNode)
            G.nodes[str(a.CurrentNode)]["seen"] +=1
            # a.Path += [a.NextNode]
            a.addPath(a.NextNode)
            # a.NextNode = -1
            a.addNextNode(-1)
            a.addTime(T)
    elif a.CurrentNode != a.EndNode:
        ##do nothing
        print("log10")
        print(a.Time)
    return a, G

def shortestPath(sourceC, G, startLoc, endLocs):
    startLL = strToList(startLoc)
    startId = idList(startLL, G)
    endLL = strToList(endLocs)
    endId = idList(endLL, G)
    pathL = []
    path = []
    startC = len(startId)
    endC = len(endId)
    sourceList = startId
    targetList = endId
    flag = 0
    pathS = []
    pathLenS = sys.maxsize
    c = sourceC
    for i in range(endC):
        try:
            path = nx.shortest_path(G, source=str(sourceList[c]), target=str(targetList[i]), weight='havlen')
            pathLen = nx.shortest_path_length(G, source=str(sourceList[c]), target=str(targetList[i]), weight='havlen')
            # print("path:/n")
            # print(path)
            # print("path length:/n")
            # print(pathLen)
            if pathLen <= pathLenS:
                pathS = path
                pathLenS = pathLen
                flag = 1
        except Exception as e:
            print(e)
            print('1')
    if flag == 1:    
        for node in pathS:
            lat = G.nodes[node]['lat']
            lon = G.nodes[node]['lon']
            pathL += [[lat, lon, c]]
    # print(pathL)
    return pathL
