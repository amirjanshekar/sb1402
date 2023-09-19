import pathlib  # baraye adres dehi
from maps.pathLib.pathLoc import locLib, routing, agent
import sys
import networkx as nx
import random as r


def strToList(lst):
    lst = lst.replace("[", "").replace("]", "")
    lst = lst.split(",")
    print(lst)
    return lst


def idList(locList, G):
    idL = []
    c = len(locList)
    for i in range(int(c / 2)):
        idL += [int(locLib.findLoc(float(locList[i * 2]), float(locList[i * 2 + 1]), G))]
    print(idL)
    return idL


def pathArr(startLoc, endLocs, emergencyLocs, dangerLocs):  # convert input from str to arr
    root_folder = pathlib.Path(__file__).parent / '..'
    root_folder = root_folder.resolve()

    sys.path.append(root_folder.as_posix())

    data_folder = root_folder / 'data'
    local_graph_file = data_folder / 'graphmap.gexf'

    G = nx.read_gexf(local_graph_file)
    for u, v, data in G.edges(data=True):
        G[u][v]["traffic"] = 1
        G[u][v]["trafficH"] = 1
        G[u][v]["seen"] = 0
    for u in G.nodes():
        G.nodes[u]["seen"] = 0

    time = 5
    pathL = []
    trafficPath = []
    trafficNodes = []
    path = []
    agnt = []
    startLL = strToList(startLoc)
    startId = idList(startLL, G)
    endLL = strToList(endLocs)
    endId = idList(endLL, G)
    startC = len(startId)
    endC = len(endId)
    ShPath = []
    endCap = []
    cntr = 0
    for endCC in range(endC):
        endCap.append(0)
        print("endcc")

    # for sNC in range(startC):
    #     G.nodes[str(startId[sNC])]["seen"] = 1

    for c in range(startC):
        smpl = r.sample(list(G.nodes), 1)
        eLId = 0
        if False:
            for eC1 in range(endC):
                if endCap[eLId] <= (startC / endC) + 1:
                    d1 = locLib.difLoc(G.nodes[str(startId[c])]['lat'], G.nodes[str(startId[c])]['lon'],
                                       G.nodes[str(endId[eLId])]['lat'], G.nodes[str(endId[eLId])]['lon'])
                    break
                else:
                    eLId += 1

        if False:  # 1
            d1 = locLib.difLoc(G.nodes[str(startId[c])]['lat'], G.nodes[str(startId[c])]['lon'],
                               G.nodes[str(endId[eLId])]['lat'], G.nodes[str(endId[eLId])]['lon'])

        if False:
            for ec in range(endC):
                d2 = locLib.difLoc(G.nodes[str(startId[c])]['lat'], G.nodes[str(startId[c])]['lon'],
                                   G.nodes[str(endId[ec])]['lat'], G.nodes[str(endId[ec])]['lon'])
                if d2 <= d1 and endCap[ec] <= (startC / endC) + 1:
                    d1 = d2
                    eLId = ec
                    print("help")
                print(eLId)
            print(endCap[eLId])
            endCap[eLId] = endCap[eLId] + 1

        if False:  # 1
            for ec in range(endC):
                d2 = locLib.difLoc(G.nodes[str(startId[c])]['lat'], G.nodes[str(startId[c])]['lon'],
                                   G.nodes[str(endId[ec])]['lat'], G.nodes[str(endId[ec])]['lon'])
                if d2 <= d1:
                    d1 = d2
                    eLId = ec
                print(eLId)
            endCap[eLId] = endCap[eLId] + 1

        if True:  # amoozesh
            b1 = r.random()
            if b1 <= (5.57 / 7):
                if nx.has_path(G, str(startId[c]), str(endId[0])):
                    agnt.append(agent.Agent(G, startId[c], -1, endId[0], 13, 2, [str(startId[c])], [], 0, c))
            elif b1 > (5.57 / 7):
                b2 = r.random()
                if b2 <= (4.4 / 7):  ## sabok
                    ### random az rah sabok
                    while True:
                        if nx.has_path(G, str(startId[c]), str(smpl[0])):
                            break
                        else:
                            smpl = r.sample(G.nodes, 1)
                    agnt.append(agent.Agent(G, startId[c], -1, smpl[0], 13, 1, [str(startId[c])], [], 0, c))
                    print("random az rah sabok 1")
                elif b2 > (4.4 / 7):  ## sangin
                    ### random az rah sangin
                    while True:
                        if nx.has_path(G, str(startId[c]), str(smpl[0])):
                            break
                        else:
                            smpl = r.sample(G.nodes, 1)
                    agnt.append(agent.Agent(G, startId[c], -1, smpl[0], 13, 0, [str(startId[c])], [], 0, c))
                    print("random az rah sangin 0")

        if False:  # baraye payan moshkhas - pishnehadi
            if nx.has_path(G, str(startId[c]), str(endId[0])):
                agnt.append(agent.Agent(G, startId[c], -1, endId[0], 13, 2, [str(startId[c])], [], 0, c))

        if False:  # nazar sanji
            a1 = r.random()
            ##az pish taeen shode
            if a1 <= (5.5 / 7):  ##bale
                ##modiriat bohran
                a2 = r.random()
                if a2 <= (3.25 / 7):  ## bale
                    ##mored etminan
                    a3 = r.random()
                    if a3 <= (5.2 / 7):  ## bale
                        ##masir ra midanid
                        a4 = r.random()
                        if a4 <= (2.8 / 7):  ##bale
                            ### maghsad modiriat bohran
                            if nx.has_path(G, str(startId[c]), str(endId[0])):
                                agnt.append(
                                    agent.Agent(G, startId[c], -1, endId[0], 13, 2, [str(startId[c])], [], 0, c))
                            print("maghsad modiriat bohran 2")
                        elif a4 > (2.8 / 7):  ##keyr
                            ## sabok ya sangin
                            a5 = r.random()
                            if a5 <= (4.4 / 7):  ## sabok
                                ### maghsad bohran az rah sabok 
                                if nx.has_path(G, str(startId[c]), str(endId[0])):
                                    agnt.append(
                                        agent.Agent(G, startId[c], -1, endId[0], 13, 4, [str(startId[c])], [], 0, c))
                                print("maghsad bohran az rah sabok 4")
                            elif a5 > (4.4 / 7):  ## sangin
                                ### maghsad bohran az rah sangin 
                                if nx.has_path(G, str(startId[c]), str(endId[0])):
                                    agnt.append(
                                        agent.Agent(G, startId[c], -1, endId[0], 13, 5, [str(startId[c])], [], 0, c))
                                print("maghsad bohran az rah sangin 5")
                    elif a3 > (5.2 / 7):  ## kheyr
                        ### be makanhaye mored nazar khod ## gereftan makanhaye jadid
                        if nx.has_path(G, str(startId[c]), str(endId[eLId])):
                            agnt.append(agent.Agent(G, startId[c], -1, endId[eLId], 13, 3, [str(startId[c])], [], 0, c))
                            # else:
                        #     agnt.append(agent.Agent(G, startId[c], -1 , G.neighbors(str(startId[c])) , 13, 2, [str(startId[c])], [], 0, c))
                        print("be makanhaye mored nazar khod 3")
                elif a2 > (3.25 / 7):
                    ### be makanhaye mored nazar khod
                    if nx.has_path(G, str(startId[c]), str(endId[eLId])):
                        agnt.append(agent.Agent(G, startId[c], -1, endId[eLId], 13, 3, [str(startId[c])], [], 0, c))
                    # else: 
                    #     agnt.append(agent.Agent(G, startId[c], -1 , G.neighbors(str(startId[c])) , 13, 2, [str(startId[c])], [], 0, c))
                    print("be makanhaye mored nazar khod 3")
            elif a1 > (5.5 / 7):  ##kheyr
                ##sabok ya sangin
                a6 = r.random()
                if a6 <= (4.4 / 7):  ## sabok
                    ### random az rah sabok
                    while True:
                        if nx.has_path(G, str(startId[c]), str(smpl[0])):
                            break
                        else:
                            smpl = r.sample(G.nodes, 1)
                    agnt.append(agent.Agent(G, startId[c], -1, smpl[0], 13, 1, [str(startId[c])], [], 0, c))
                    print("random az rah sabok 1")
                elif a6 > (4.4 / 7):  ## sangin
                    ### random az rah sangin
                    while True:
                        if nx.has_path(G, str(startId[c]), str(smpl[0])):
                            break
                        else:
                            smpl = r.sample(G.nodes, 1)
                    agnt.append(agent.Agent(G, startId[c], -1, smpl[0], 13, 0, [str(startId[c])], [], 0, c))
                    print("random az rah sangin 0")
        cntr += 1

    # pos=nx.spring_layout(G, seed=100)
    # nx.draw(G,pos)
    maxTraffic = 0
    sumTraffic = 0
    maxSumTraffic = 0
    trafficCount = 0
    maxSeen = 0
    sumSeen = 0
    maxSumSeen = 0
    seenCount = 0
    GTemp = nx.read_gexf(local_graph_file)
    for i in range(500):  ##time * 5min ##time 100 change in front
        for a in agnt:
            if a.Behaviour == 0:  # bi maghsad sangin
                print("B0")
                a, G = routing.heaviestTraffic(a, G, time)
            if a.Behaviour == 1:  # bi maghsad sabok
                print("B1")
                a, G = routing.lightestTraffic(a, G, time)
            if a.Behaviour == 2:  # ba maghsad ba masir ba bohran
                print("B2")
                a, G = routing.nextShortPath(a, G, time)
            if a.Behaviour == 3:  # ba maghsad bi bohran
                print("B3")
                a, G = routing.nextShortPath(a, G, time)
            if a.Behaviour == 4:  ### maghsad bohran az rah sabok
                print("B4")
                a, G = routing.lightestTraffic(a, G, time)
            if a.Behaviour == 5:  ### maghsad bohran az rah sangin
                print("B5")
                a, G = routing.heaviestTraffic(a, G, time)

        sumTraffic = 0
        tC = 0
        for u, v, data in G.edges(data=True):
            if (G[u][v]["traffic"] - 1) / 10 > maxTraffic:
                maxTraffic = (G[u][v]["traffic"] - 1) / 10
            if (G[u][v]["traffic"] - 1) / 10 > 3:
                trafficPath += [[
                    G.nodes[u]['lat'],
                    G.nodes[u]['lon'],
                    G.nodes[v]['lat'],
                    G.nodes[v]['lon'],
                    G[u][v]["traffic"],
                    i
                ]]

            sumTraffic += ((G[u][v]["traffic"] - 1) / 10)  # test
            if (G[u][v]["traffic"] - 1) / 10 > 1:
                tC += 1

        if sumTraffic > maxSumTraffic:
            maxSumTraffic = sumTraffic
        if trafficCount < tC:
            trafficCount = tC

        sumSeen = 0
        sC = 0

        for u in GTemp.nodes():
            GTemp.nodes[u]["seen"] = 0

        for a in agnt:
            if a.NextNode == -1:
                GTemp.nodes[str(a.CurrentNode)]["seen"] += 1
                print(GTemp.nodes[str(a.CurrentNode)]["seen"])

        for u in GTemp.nodes():
            if GTemp.nodes[u]["seen"] > maxSeen:
                maxSeen = GTemp.nodes[u]["seen"]
            if GTemp.nodes[u]["seen"] > 1:
                trafficNodes += [[
                    GTemp.nodes[u]['lat'],
                    GTemp.nodes[u]['lon'],
                    GTemp.nodes[u]["seen"],
                    i
                ]]

            if GTemp.nodes[u]["seen"] > 0:
                sumSeen += GTemp.nodes[u]["seen"]
            if GTemp.nodes[u]["seen"] > 0:
                sC += 1

        if sumSeen > maxSumSeen:
            maxSumSeen = sumSeen
        if seenCount < sC:
            seenCount = sC

    for z in range(len(agnt)):
        for node in agnt[z].Path:
            lat = G.nodes[node]['lat']
            lon = G.nodes[node]['lon']
            pathL += [[lat, lon, z]]

    startAgntC = len(agnt)

    B0 = 0
    T0 = 0
    B1 = 0
    T1 = 0
    B2 = 0
    T2 = 0
    B3 = 0
    T3 = 0
    B4 = 0
    T4 = 0
    B5 = 0
    T5 = 0

    # gereftan etelaat
    for a in agnt:
        if a.Behaviour == 0:
            B0 += 1
            if a.Time > T0:
                T0 = a.Time
        if a.Behaviour == 1:
            B1 += 1
            if a.Time > T1:
                T1 = a.Time
        if a.Behaviour == 2:
            B2 += 1
            if a.Time > T2:
                T2 = a.Time
        if a.Behaviour == 3:
            B3 += 1
            if a.Time > T3:
                T3 = a.Time
        if a.Behaviour == 4:
            B4 += 1
            if a.Time > T4:
                T4 = a.Time
        if a.Behaviour == 5:
            B5 += 1
            if a.Time > T5:
                T5 = a.Time

    print("B0=", B0, " ",
          "B1=", B1, " ",
          "B2=", B2, " ",
          "B3=", B3, " ",
          "B4=", B4, " ",
          "B5=", B5, "\n")

    print("T0=", T0, " ",
          "T1=", T1, " ",
          "T2=", T2, " ",
          "T3=", T3, " ",
          "T4=", T4, " ",
          "T5=", T5, "\n")

    # maxTraffic = 0
    # sumTraffic = 0
    # maxSumTraffic = 0
    # maxSeen = 0
    # sumSeen = 0
    # maxSumSeen = 0

    print("max Sum Seen = ", maxSumSeen, " ", "seen Count = ", seenCount)
    print("max Seen = ", maxSeen)
    print("max Sum Traffic = ", maxSumTraffic, " ", "traffic Count = ", trafficCount)
    print("max Traffic = ", maxTraffic)
    print("end capacity =", endCap)

    return pathL, trafficPath, trafficNodes, startAgntC
