import pathlib
import sys
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

def findLoc(lat , lng , G):##loction ro az roye naghshe be nazdiktarin loction roye rahha payda mikone.
    temp2 = 0
    locID = 0
    for n_id in G.nodes():
        if G.nodes[n_id]['lat'] == lat and G.nodes[n_id]['lon'] == lng: 
            locID = n_id
        temp1 = difLoc(lng, lat, G.nodes[n_id]['lon'], G.nodes[n_id]['lat'] )
        if temp2 == 0:
            temp2 = difLoc(lng, lat, G.nodes[n_id]['lon'], G.nodes[n_id]['lat'] )
        if temp1 <= temp2 :
            temp2 = temp1
            locID = n_id

    print(G.nodes[locID]['lon'])
    return locID