import pathlib
import sys
import matplotlib.pyplot as plt
import networkx as nx
from math import radians, cos, sin, asin, sqrt

#for test before run in django

def diste(lng1, lat1, lng2, lat2, unit_m=True):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    default unit : km
    """
    # convert decimal degrees to radians
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])

    # haversine formula
    dlng = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlng / 2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of the Earth in kilometers. Use 3956 for miles
    if unit_m:
        r *= 1000
    return c * r

def difLoc(lng1, lat1, lng2, lat2): ##ekhtelaf beyen 2 noghte
    dif = diste(lng1, lat1, lng2, lat2, True)
    return dif

def findLoc(lat , lon):##loction ro az roye naghshe be nazdiktarin loction roye rahha payda mikone.
    temp2 = 0
    locID = 0
    for n_id in G.nodes():
        if G.nodes[n_id]['lat'] == lat and G.nodes[n_id]['lon'] == lon: 
            locID = n_id
        temp1 = difLoc(lon, lat, G.nodes[n_id]['lon'], G.nodes[n_id]['lat'] )
        if temp2 == 0:
            temp2 = difLoc(lon, lat, G.nodes[n_id]['lon'], G.nodes[n_id]['lat'] )
        if temp1 <= temp2 :
            temp2 = temp1
            locID = n_id
    return locID
            
        
        

    

root_folder = pathlib.Path(__file__).parent / '..'
root_folder = root_folder.resolve()

sys.path.append(root_folder.as_posix())

data_folder = root_folder / 'data'
local_graph_file = data_folder / 'graphmap.gexf'

G = nx.read_gexf(local_graph_file)
# pos = nx.spring_layout(G)
# path = nx.shortest_path(G, source='426566201', target='4470168551')#my alg will come here!!! for finding the path

# pathLoc = []

# for node in path:
#     lat = G.nodes[node]['lat']
#     lon = G.nodes[node]['lon']
#     pathLoc += [[lat , lon]]
# for nId in G.nodes():
#     print(G.nodes[nId]['label'])

print(findLoc(35.78631, 51.347))



# print(G.nodes(data=True))

# path_edges = zip(path,path[1:])
# path_edges = set(path_edges)

# nx.draw(G,pos=pos)
# nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
# nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=2)
# plt.show()